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
        return f"PortInfo(service={self.service}, product={self.product}, version={self.version}, extrainfo={self.extrainfo})"

def run_nmap(target):
    # Run nmap with service version detection and XML output
    xml_output_file = "nmap_output.xml"
    try:
        subprocess.run(["nmap", "-sV", "-oX", xml_output_file, target], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running nmap: {e}")
        sys.exit(1)
    return xml_output_file

def parse_nmap_xml(xml_file):
    port_map = {}
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # Find the host element
        host = root.find("host")
        if host is None:
            print("No host found in nmap output.")
            return port_map
        
        # Find ports
        ports = host.find("ports")
        if ports is None:
            print("No ports found in nmap output.")
            return port_map
        
        for port_elem in ports.findall("port"):
            state_elem = port_elem.find("state")
            if state_elem is not None and state_elem.get("state") == "open":
                port_id = port_elem.get("portid")
                protocol = port_elem.get("protocol")
                
                service_elem = port_elem.find("service")
                if service_elem is not None:
                    service = service_elem.get("name")
                    product = service_elem.get("product")
                    version = service_elem.get("version")
                    extrainfo = service_elem.get("extrainfo")
                    
                    # Create PortInfo object
                    info = PortInfo(service=service, product=product, version=version, extrainfo=extrainfo)
                    port_map[port_id] = info
    
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
    finally:
        # Clean up XML file
        if os.path.exists(xml_file):
            os.remove(xml_file)
    
    return port_map

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python enumerate.py <target_ip>")
        sys.exit(1)
    
    target = sys.argv[1]
    xml_file = run_nmap(target)
    port_map = parse_nmap_xml(xml_file)
    
    # Print the results for demonstration
    print("Enumerated Ports:")
    for port, info in sorted(port_map.items(), key=lambda x: int(x[0])):
        print(f"Port {port}: {info}")
