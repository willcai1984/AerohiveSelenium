# -*- coding: UTF-8 -*-

#python cwp_login_positive.py -r http://${sta.ip}:4444/wd/hub -t ie -f logFile --parameters
from AerohiveGUI.scripts.cwp import CWP 
import time
def cwp_access_Internet():#login success，could access Internet
    cwp = CWP()
    if cwp.w.get_value("login.is_success")=="true" or cwp.w.get_value("login.is_success")=="True":#login success，could access Internet
        time.sleep(2)
        cwp.unit_access_internet(cwp.w.get_value("visit.permit_url"))
    cwp.w.quit()
if __name__ == '__main__':
    cwp_access_Internet()