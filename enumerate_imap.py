import subprocess


def enumerate_imap(target, port):
    print('*************************************************************')
    print('******************** IMAP Banner Grabbing  ********************')
    imap_banner_script = 'nc -nv ' + str(target) + ' 143'
    imap_banner_grabbing_info = subprocess.run(imap_banner_script)
    print(imap_banner_grabbing_info)

    print('*************************************************************')
    print('******************** IMAP Openssl Banner Grabbing  ********************')
    imap_openssl_banner_script = 'openssl s_client -connect ' + str(target) + ':993 -quiet'
    imap_openssl_grabbing_info = subprocess.run(imap_openssl_banner_script)
    print(imap_openssl_grabbing_info)


    #
    print('*************************************************************')
    print('******************** NTLM Auth - Information disclosure  ********************')
    ntlm_auth_script = 'telnet ' + str(target) + ' 143'
    ntlm_auth_info = subprocess.run(ntlm_auth_script)
    print(ntlm_auth_info)

