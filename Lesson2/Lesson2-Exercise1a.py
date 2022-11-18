from netmiko import Netmiko
from getpass import getpass
from pprint import pprint

device = {

"device_type" : "cisco_ios",
"host" : "cisco4.lasthop.io",
"username" : "pyclass",
"password" : getpass(),
"session_log" : "ping.txt"

}

net_conn = Netmiko(**device)
print(net_conn.find_prompt())
output = net_conn.send_command_timing("ping", strip_prompt = False, strip_command = False)
output = net_conn.send_command_timing("ip", strip_prompt = False, strip_command = False)
output += net_conn.send_command_timing("8.8.8.8", strip_prompt = False, strip_command = False)
output += net_conn.send_command_timing("100", strip_prompt = False, strip_command = False)
output += net_conn.send_command_timing("100", strip_prompt = False, strip_command = False)
output += net_conn.send_command_timing("2", strip_prompt = False, strip_command = False)
output += net_conn.send_command_timing("n", strip_prompt = False, strip_command = False)
output += net_conn.send_command_timing("n", strip_prompt = False, strip_command = False)
print(output)
