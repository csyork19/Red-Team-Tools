class Constants:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def get_wfuzz_command(self):
        return f'sudo wfuzz -c -f sub-fighter.txt -Z -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt --sc 200,202,204,301,302,307,403 http://{self.ip_address}'

    def get_enum4linux_command(self):
        return f'enum4linux -U {self.ip_address}'

    def get_nmap_command(self):
        return f'nmap -sC -sV {self.ip_address}'









