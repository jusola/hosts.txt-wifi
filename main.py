import configparser
from hosts import hosts
import wifi
import time
import os



config = configparser.ConfigParser()
config.read('config.ini')

if os.name == 'nt':
    hosts_path = os.path.join(os.environ['SYSTEMROOT'], 'system32/drivers/etc/hosts')
elif os.name == 'posix':
    hosts_path = '/etc/hosts'
else:
    raise Exception('Unsupported OS: %s' % os.name)


iface = wifi.Wifi()
hosts_manager = hosts.Hosts(hosts_path)

curSSID = iface.getSSID()
if (not curSSID is None):
    if(curSSID == config['hostsmanager']['SSID']):
        hosts_manager.set_one(config['hostsmanager']['hostname'], config['hostsmanager']['target'])
        hosts_manager.write(hosts_path)
    else:
        hosts_manager.remove_one(config['hostsmanager']['host'], False)
        hosts_manager.write(hosts_path)
else:
    hosts_manager.remove_one(config['hostsmanager']['host'], False)
    hosts_manager.write(hosts_path)