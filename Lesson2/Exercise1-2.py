from netmiko import Netmiko
from getpass import getpass

nxos1 = {

'username' : 'pyclass',
'device_type' : 'cisco_nxos',
'password' : getpass(),
'host': 'nxos1.lasthop.io',
'session_log' : 'hc.txt'

}


nxos2 = { 
  
'username' : 'pyclass',
'device_type' : 'cisco_nxos',
'password' : getpass(),
'host': 'nxos2.lasthop.io',
'session_log' : 'hc.txt'
 
}

NXOS = [nxos1, nxos2]

for device in NXOS:
    net_conn = Netmiko(**device)
    print(net_conn.find_prompt())



