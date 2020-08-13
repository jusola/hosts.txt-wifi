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

def removeHosts():
    for hostname in config['hostmanager']['hostnames']:
        hosts_manager.remove_one(hostname)
    hosts_manager.write(hosts_path)

def addHosts():
    for hostname, target in config.items("rules"):
        hosts_manager.set_one(hostname, target)
    hosts_manager.write(hosts_path)

curSSID = iface.getSSID()
if (not curSSID is None):
    if(curSSID == config['hostsmanager']['SSID']):
        addHosts()
    else:
        removeHosts()
else:
    removeHosts()