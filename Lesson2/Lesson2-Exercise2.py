from getpass import getpass
from netmiko import Netmiko
from pprint import pprint
from datetime import datetime

nxos2 = {

"device_type":"cisco_nxos",
"host":"nxos2.lasthop.io",
"username":"pyclass",
"password" : getpass(),
"global_delay_factor" : 2,
"fast_cli" : False
}

net_conn = Netmiko(**nxos2)
print(net_conn.find_prompt())

print("Executing command first time")
print("^"*40)
start = datetime.now()
output1 = net_conn.send_command("show lldp neighbors detail")
end = datetime.now()
execution_time1 = end - start
print(execution_time1)
print(output1)



print("Executing command second time")
print("^"*40)
start = datetime.now()
output2 = net_conn.send_command("show lldp neighbors detail", delay_factor = 8)
end = datetime.now()
execution_time2 = end - start
print(execution_time2)
print(output2)
