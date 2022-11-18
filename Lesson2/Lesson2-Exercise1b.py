from netmiko import Netmiko
from pprint import pprint
from getpass import getpass

device = {

"device_type" : "cisco_ios",
"host" : "cisco4.lasthop.io",
"username" : "pyclass",
"password" : getpass(),
"session_log" : "ping-1b.txt"

}

net_conn = Netmiko(**device)
print(net_conn.find_prompt())

output = net_conn.send_command("ping", expect_string = ":",strip_prompt = False, strip_command = False)
output += net_conn.send_command("ip", expect_string = ":",strip_prompt = False, strip_command = False)
output += net_conn.send_command("8.8.8.8", expect_string = ":",strip_prompt = False, strip_command = False)
output += net_conn.send_command("\n", expect_string = ":",strip_prompt = False, strip_command = False)
output += net_conn.send_command("\n", expect_string = ":",strip_prompt = False, strip_command = False)
output += net_conn.send_command("\n", expect_string = ":",strip_prompt = False, strip_command = False)
output += net_conn.send_command("\n", expect_string = ":",strip_prompt = False, strip_command = False)
output += net_conn.send_command("\n", expect_string = ":",strip_prompt = False, strip_command = False)
print(output)
