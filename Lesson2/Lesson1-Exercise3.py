from netmiko import Netmiko
from pprint import pprint
from getpass import getpass

device = {

'host' : 'cisco3.lasthop.io',
'username' : 'pyclass',
'password' : getpass(),
'device_type' : 'cisco_ios'

}

net_conn = Netmiko(**device)
print(net_conn.find_prompt())

output = net_conn.send_command("show version")
print(output)

f = open("output.txt", 'w')
f.write(output)
f.close()


