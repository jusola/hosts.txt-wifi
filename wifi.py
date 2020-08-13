import pywifi

wifi = pywifi.PyWiFi()


ifaces = wifi.interfaces()
if(len(ifaces) <= 0):
    raise SystemError('No wifi interface found')

iface = wifi.interfaces()[0]

class Wifi(object):
    def getSSID(self):
        print(iface)
        print(iface.status())
        return iface.status()

test = Wifi()
test.getSSID()