import subprocess

import Constants

def enumerate_http_target(target, port):
    print('******************** PRINT HTTP HEADERS ********************')
    http_url = str(target) + ':' + str(port)
    header_info = subprocess.run(['curl', '-v', http_url])
    print(header_info)

    print('******************** PRINT BANNER ********************')
    banner_info = subprocess.run(['nc', target, port])
    print(banner_info)

    print('******************** PRINTING CGI-BIN  ********************')
    http_url = str(target) + ':' + str(port) + '/cgi-bin/'
    cgibin_info = subprocess.run(['curl', '-v', http_url])
    print(cgibin_info)

    print('******************** PRINTING ROBOTS.txt  ********************')
    http_url = str(target) + ':' + str(port) + '/robots.txt'
    robotstxt_info = subprocess.run(['curl', '-v', http_url])
    print(robotstxt_info)

    print('******************** RUNNING DIRECTORY SCAN | WFUZZ ********************')
    wfuzz_command = Constants.WFUZZ_COMMAND + str(target) + ':' + str(port) + '/FUZZ'
    wfuzz_info = subprocess.run(wfuzz_command)
    print(wfuzz_info)

    print('******************** RUNNING DIRECTORY SCAN |  Gobuster ********************')
    gobuster_command = 'gobuster dir -u ' + str(target) + str(port) + '-w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 40 -x .sh,.txt,.html,.pdf,.php'
    gobuster_info = subprocess.run(gobuster_command)
    print(gobuster_info)

    print('******************** RUNNING NIKTO SCAN ********************')
    nikto_command = 'nikto -h' + str(target) + str(port)
    nikto_info = subprocess.run(nikto_command)
    print(nikto_info)


def enumerate_wordpress(target, port):
    print('**********************************************************')
    print('******************** WORDPRESS THEMES ********************')
    wordpress_theme_command = 'wpscan --url '+ str(target) + ':' + str(port) + '/wordpress/ --enumerate t'
    wordpress_theme_info = subprocess.run(wordpress_theme_command)
    print(wordpress_theme_info)

    print('*********************************************************')
    print('******************** WORDPRESS USERS ********************')
    wordpress_users_command = 'wpscan --url ' + str(target) + ':' + str(port) + '/wordpress/ --enumerate u'
    wordpress_users_info = subprocess.run(wordpress_users_command)
    print(wordpress_users_info)

    # TODO: Parse the list of user(s) to the password command
    print('*************************************************************')
    print('******************** WORDPRESS PASSWORDS ********************')
    wordpress_password_command = 'wpscan --url ' + str(target) + ':' + str(port) + '/wordpress/ --usernames USERNAME --passwords /usr/share/wordlists/rockyou.txt'
    wordpress_password_info = subprocess.run(wordpress_password_command)
    print(wordpress_password_info)

    print('***********************************************************')
    print('******************** WORDPRESS PLUGINS ********************')
    wordpress_plugins_command = 'wpscan --url ' + str(target) + ':' + str(port) + '/wordpress/ --enumerate vp'
    wordpress_plugins_info = subprocess.run(wordpress_plugins_command)
    print(wordpress_plugins_info)
    print('**********************************************************')

    print('***********************************************************')
    print('******************** WORDPRESS PLUGINS | MIXED ********************')
    wordpress_plugins_command = 'wpscan --url ' + str(target) + ':' + str(port) + '/wordpress/ --plugins-detection mixed'
    wordpress_plugins_info = subprocess.run(wordpress_plugins_command)
    print(wordpress_plugins_info)
    print('**********************************************************')

    print('***********************************************************')
    print('******************** WORDPRESS PLUGINS | PASSIVE ********************')
    wordpress_plugins_command = 'wpscan --url ' + str(target) + ':' + str(
        port) + '/wordpress/ --plugins-detection passive'
    wordpress_plugins_info = subprocess.run(wordpress_plugins_command)
    print(wordpress_plugins_info)
    print('**********************************************************')

    print('***********************************************************')
    print('******************** WORDPRESS PLUGINS | AGGRESSIVE ********************')
    wordpress_plugins_command = 'wpscan --url ' + str(target) + ':' + str(
        port) + '/wordpress/ --plugins-detection aggressive'
    wordpress_plugins_info = subprocess.run(wordpress_plugins_command)
    print(wordpress_plugins_info)
    print('**********************************************************')


