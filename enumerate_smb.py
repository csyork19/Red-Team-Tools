import subprocess


def enumerate_smb(target, port):
    print('******************** SMB | enum4linux ********************')
    enum4linux_command = 'enum4linux -a ' + str(target)
    enum4linux_info = subprocess.run(enum4linux_command)
    print(enum4linux_info)

    print('******************** SMB | smbClient ********************')
    enum4linux_command = 'smbclient -L ' + str(target)
    enum4linux_info = subprocess.run(enum4linux_command)
    print(enum4linux_info)

    print('******************** SMB | guest login attempt ********************')
    smb_guest_command = 'smbclint -L //' + str(target) + '-U guest'
    smb_guest_info = subprocess.run(smb_guest_command)
    smb_guest_login_successful = False
    if smb_guest_info.returncode == 200:
        smb_guest_login_successful = True
    print('SMB guest login successful: ' + str(smb_guest_login_successful))

    print('******************** SMB | guest login attempt ********************')
    smb_admin_command = 'smbclint -L //' + str(target) + '-U admin'
    smb_admin_info = subprocess.run(smb_admin_command)
    smb_admin_login_successful = False
    if smb_admin_info.returncode == 200:
        smb_admin_login_successful = True
    print('SMB guest login successful: ' + str(smb_admin_login_successful))

    print('******************** SMB | anonymous login attempt ********************')
    smb_anonymous_command = 'smbclint -L //' + str(target) + '-U anonymous'
    smb_anonymous_info = subprocess.run(smb_anonymous_command)
    smb_anonymous_login_successful = False
    if smb_anonymous_info.returncode == 200:
        smb_anonymous_login_successful = True
    print('SMB guest login successful: ' + str(smb_anonymous_login_successful))




