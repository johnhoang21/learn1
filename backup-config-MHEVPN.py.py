import netmiko
import time
from netmiko import ConnectHandler
# devices = '''
## 10.20.111.178
# '''.strip().splitlines()

devices = '''
10.20.111.172
10.20.111.170
10.20.111.178
10.20.111.177
10.20.111.194
10.20.111.195
10.20.111.171
'''.strip().splitlines()

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
     #   print(connection.send_command("show clock"))
        hostname = connection.send_command("show running-config switch-attributes host-name").split()[2]
     #   hostname = hostname[2]
        name = time.ctime().split()[4]+time.ctime().split()[1]+time.ctime().split()[2]+"-"+hostname
     #   print("%s" %name)
        connection.send_command("copy running-config scp://releaseuser:releaseuser@10.31.2.101//home/releaseuser/defects/minhoang/X/%s" %name)
        print("done copying running %s config to tftp" %hostname)
    except netmiko.ssh_exception.NetMikoAuthenticationException:
        print('Authentication failed to ', device)