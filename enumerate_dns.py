import subprocess

def enumerate_dns(target, domain_name,port):
    print('*************************************************************')
    print('******************** DNS A RECORD - IPv4 ********************')
    a_record_command = 'host ' + str(target)
    a_record_info = subprocess.run(a_record_command)
    print(a_record_info)

    print('****************************************************************')
    print('******************** DNS AAAA RECORD - IPv6 ********************')
    aaaa_record_command = 'host -t aaaa' + str(target)
    aaaa_record_info = subprocess.run(aaaa_record_command)
    print(aaaa_record_info)

    print('**********************************************************************')
    print('******************** DNS MX RECORD - Mail Records ********************')
    mx_record_command = 'host -t mx' + str(target)
    mx_record_info = subprocess.run(mx_record_command)
    print(mx_record_info)

    print('*************************************************************************')
    print('******************** DNS PTR RECORD - Reverse Lookup ********************')
    dns_record_command = 'host -t ptr' + str(target)
    dns_record_info = subprocess.run(dns_record_command)
    print(dns_record_info)

    print('******************************************************************************')
    print('******************** DNS CNAME RECORD - Alias host record ********************')
    dns_record_command = 'host -t cname' + str(target)
    dns_record_info = subprocess.run(dns_record_command)
    print(dns_record_info)

    print('******************************************************************************************')
    print('******************** DNS TXT RECORD - Text records for arbitrary data ********************')
    dns_record_command = 'host -t txt' + str(target)
    dns_record_info = subprocess.run(dns_record_command)
    print(dns_record_info)

    print('******************************************************************************************')
    print('******************** DNS zone transfer ********************')
    dns_zone_transfer_command = 'dig axfr ' + str(domain_name) + '@' + str(target)
    dns_zone_transfer_info = subprocess.run(dns_zone_transfer_command)
    print(dns_zone_transfer_info)

    print('******************************************************')
    print('******************** dnsenum tool ********************')
    dns_record_command = 'dnsenum' + str(target)
    dns_record_info = subprocess.run(dns_record_command)
    print(dns_record_info)






