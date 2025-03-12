import re

# This class is a utility class for common methods being used
def parse_nmap_response(nmap_output):
    if nmap_output is None:
        return "No NMAP OUTPUT"

    map_of_nmap_output = {}

    # Regex to capture port, service, and version
    pattern = r'(\d+)/tcp\s+open\s+(\S+)\s+(\S+\s+\S+)'  # Matches port, service, and version
    matches = re.findall(pattern, nmap_output)

    # Create a dictionary with port as key and (service, version) as value
    for match in matches:
        port, service, version = match
        map_of_nmap_output[int(port)] = (service, version)

    return map_of_nmap_output
