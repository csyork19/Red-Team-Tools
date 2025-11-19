import subprocess
import xml.etree.ElementTree as ET
import sys
import os


class PortInfo:
    def __init__(self, service=None, product=None, version=None, extrainfo=None):
        self.service = service
        self.product = product
        self.version = version
        self.extrainfo = extrainfo

    def __repr__(self):
        return (
            f"PortInfo(service={self.service}, product={self.product}, "
            f"version={self.version}, extrainfo={self.extrainfo})"
        )


def run_nmap(target):
    xml_output_file = "nmap_output.xml"
    try:
        subprocess.run(
            ["nmap", "-sV", "-oX", xml_output_file, target],
            check=True,
            capture_output=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error running nmap: {e}")
        sys.exit(1)
    return xml_output_file


def parse_nmap_xml(xml_file):
    port_map = {}
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        host = root.find("host")
        if host is None:
            return port_map

        ports = host.find("ports")
        if ports is None:
            return port_map

        for port_elem in ports.findall("port"):
            state_elem = port_elem.find("state")
            if state_elem is not None and state_elem.get("state") == "open":
                port_id = port_elem.get("portid")
                service_elem = port_elem.find("service")

                if service_elem is not None:
                    info = PortInfo(
                        service=service_elem.get("name"),
                        product=service_elem.get("product"),
                        version=service_elem.get("version"),
                        extrainfo=service_elem.get("extrainfo")
                    )
                    port_map[port_id] = info

    finally:
        if os.path.exists(xml_file):
            os.remove(xml_file)

    return port_map


# ----------------------------------------------------------
# NEW: Run Gobuster if the service is HTTP/S
# ----------------------------------------------------------

def run_gobuster(ip, port):
    print(f"\n[+] HTTP detected on port {port}. Running Gobuster...\n")

    cmd = [
        "gobuster", "dir",
        "-u", f"http://{ip}:{port}",
        "-w", "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt",
        "-t", "40",
        "-x", ".sh,.txt,.html,.pdf,.php"
    ]

    try:
        process = subprocess.Popen(cmd)
        process.communicate()
    except Exception as e:
        print(f"Error running Gobuster: {e}")


def check_for_http_and_run_gobuster(ip, port_map):
    http_keywords = ["http", "http-alt", "https"]

    for port, info in port_map.items():
        if info.service and any(keyword in info.service for keyword in http_keywords):
            run_gobuster(ip, port)


# ----------------------------------------------------------

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python enumerate.py <target_ip>")
        sys.exit(1)

    target = sys.argv[1]
    xml_file = run_nmap(target)
    port_map = parse_nmap_xml(xml_file)

    print("\nEnumerated Ports:")
    for port, info in sorted(port_map.items(), key=lambda x: int(x[0])):
        print(f"Port {port}: {info}")

    # NEW: auto run Gobuster for any detected HTTP service
    check_for_http_and_run_gobuster(target, port_map)
