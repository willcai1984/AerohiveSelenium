# -*- coding: UTF-8 -*-

#python cwp_login_positive.py -r http://${sta.ip}:4444/wd/hub -t ie -f logFile --parameters
from AerohiveSelenium.scripts.hm import hm

def hm_update():
    con = hm()
    con.unit_login(con.w.get_value("visit.url"), con.w.get_value("login.username"), con.w.get_value("login.password"))
    con.unit_config_update(con.w.get_value("policy.name"),con.w.get_value("device.mac"), con.w.get_value("update.mode"))
if __name__ == '__main__':
    hm_update()
