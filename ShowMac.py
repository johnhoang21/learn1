import netmiko
import time
import re
from netmiko import ConnectHandler
devices = '''
10.20.111.178
'''.strip().splitlines()

# devices = '''
# 10.20.111.172
# 10.20.111.170
# 10.20.111.178
# 10.20.111.177
# 10.20.111.194
# 10.20.111.195
# 10.20.111.171
# '''.strip().splitlines()

print(devices)

#-> create a list of mgmt ip

device_type = "cisco_xr"
username = "admin"
password = "password"

for device in devices:
    try:
        print("~"*79)
        print('connecting to ', device)
        connection = netmiko.ConnectHandler(ip=device, device_type=device_type, username = username, password = password)
        MacTable = connection.send_command("show mac")
        MacTable = MacTable.splitlines()
        count = 0
        for line in MacTable:
            if re.search("EVPN",line) != None:
                print (line)
                count = count + 1

        print(count)

        # del MacTable[:5]
        # del MacTable[-1:]
        #
        # for item in MacTable:
        #     if item.split()[3] == "EVPN-Static":
        #         print(item)

        #print(MacTable)
    except netmiko.ssh_exception.NetMikoAuthenticationException:
        print('Authentication failed to ', device)