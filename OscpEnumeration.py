import subprocess

import RedTeamToolsUtil
from Constants import Constants


class OscpEnumeration:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def nmap_scan(self):
        global nmap_scan_result
        try:
            nmap_scan_result = subprocess.run([Constants.get_nmap_command(self.ip_address)])
        except Exception as e:
            print(f" An error occurred while performing an nmap scan: {e}")

        return perform_enumeration(RedTeamToolsUtil.parse_nmap_response(nmap_scan_result))

    def perform_enumeration(nmap_ouput):
        target_enumeration = {}

        # TODO: Iterate over the nmap output and enumerate services (concurrently)









