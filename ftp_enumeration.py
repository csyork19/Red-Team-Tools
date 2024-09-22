import subprocess


def enumerate_ftp(target):
    print('******************** RUNNING NMAP SCRIPTS FOR FTP ********************')
    nmap_results = subprocess.run(['nmap', '--script', 'ftp-*', '-p21', '-vv', target])
    print(nmap_results)

    print('******************** TRYING ANONYMOUS LOGIN  ********************')
    anonymous_login = subprocess.run(['ftp', target])
    anonymous_login_successful = False
    if anonymous_login.returncode == 0: anonymous_login_successful == True
    print('ANONYMOUS LOGIN: ' + str(anonymous_login_successful))
