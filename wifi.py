import subprocess

class Wifi(object):
    def getSSID(self):
        out = subprocess.check_output("netsh wlan show interfaces")
        out = out.decode("ascii")
        out = out.replace("\r", "")
        out = out.replace(" ", "")
        ls = out.split("\n")
        ls = ls[4:]
        x = 0
        for elem in ls:
            key = elem.split(':')[0]
            value = elem.split(':')[1]
            if(key == "SSID"):
                return value
        return None