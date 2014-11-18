# -*- coding: UTF-8 -*-

#python cwp_logout_positive.py -r http://${sta.ip}:4444/wd/hub -t ie -f logFile --parameters
from AerohiveSelenium.scripts.cwp import CWP 

def cwp_logout():
    cwp = CWP()
    cwp.unit_logout(cwp.w.get_value("logout.title"), cwp.w.get_value("logout.timeout") )
    cwp.w.quit()
if __name__ == '__main__':
    cwp_logout()
