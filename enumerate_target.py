import re
import sys
import subprocess



def run_nmap_scan(target_ip):
    nmap_command = ["nmap", "-sV", "-sV", target_ip]
    nmap_result = subprocess.run(nmap_command, capture_output=True, text=True)
    return parse_nmap_output(nmap_result)

def parse_nmap_output(self):
    # Initialize the dictionary to store the parsed data
    port_info = {}

    # Regular expression to match the relevant lines in the nmap output
    regex = re.compile(r"(\d+)/tcp\s+(\w+)\s+(\w+)\s*(.*)")

    # Iterate over each line in the output
    for line in self.splitlines():
        match = regex.match(line)
        if match:
            port, state, service, version = match.groups()
            port_info[port] = [service, version.strip()]

    return port_info

def enumerate_http_webserver():
    #   TODO: Print webserver header info
    #   TODO: Print service version - if any version is available
    #   TODO: Directory Scan/FUZZ
    #   TODO: Any templates or powered by listed in the header or footer
    #   TODO: Search the service on github or a google dork and open a link and get the title of the exploit. MAybe search on explloit db?
    #   TODO: Try LFI for a windows or linux machine




    return ""
def enumerate_ftp():
    # TODO: Try anonymous login
    # TODO: Try admin login
    # TODO: Try guest login
    return ""


def enumerate_dns():
    return ""


def enumerate_smb():
    return ""

def enumerate_smnp():
    return ""

def enumerate_smtp():
    return ""


def enumerate_nfs():
    return ""


target_ip_address = sys.argv[0]
print(run_nmap_scan('76.36.18.6'))
