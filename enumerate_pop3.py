import subprocess


def enumerate_pop3(target,port):
    print('*************************************************************')
    print('******************** POP3 NMAP Scripts  ********************')
    pop3_nmap_script = 'nmap --script "pop3-capabilities or pop3-ntlm-info" -sV -port ' + str(port) + ' ' + str(target) #All are default scripts
    pop3_nmap_info = subprocess.run(pop3_nmap_script)
    print(pop3_nmap_info)
