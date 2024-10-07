import subprocess

def enumerate_ldap(target,port):
    print('*************************************************************')
    print('******************** LDAPSEARCH Script ********************')
    ldap_ldapsearch_command = 'ldapsearch -x -H ldap://' + str(target) + ' -b "dc=<domain>,dc=com"'
    ldap_ldapsearch_info = subprocess.run(ldap_ldapsearch_command)
    print(ldap_ldapsearch_info)

    print('*************************************************************')
    print('******************** NMAP Script ********************')
    ldap_nmap_command = 'nmap -p' + str(port) + ' --script=ldap-search ' + str(target)
    ldap_nmap_info = subprocess.run(ldap_nmap_command)
    print(ldap_nmap_info)

    print('*************************************************************')
    print('******************** Service Principal Names ********************')
    ldap_spn_command = 'ldapsearch -x -H ldap://' + str(target) +  '-b "dc=<domain>,dc=com" "(&(objectClass=person)(servicePrincipalName=*))" sAMAccountName servicePrincipalName'
    ldap_spn_info = subprocess.run(ldap_spn_command)
    print(ldap_spn_info)

