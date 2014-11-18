# -*- coding: UTF-8 -*-

#python cwp_login_positive.py -r http://${sta.ip}:4444/wd/hub -t ie -f logFile --parameters
from AerohiveSelenium.scripts.configrollback import ConfigRollBack 

def configrollback_basic():
    con = ConfigRollBack ()
    con.unit_login(con.w.get_value("visit.url"), con.w.get_value("login.username"), con.w.get_value("login.password"))
    con.unit_monitor_modify(con.w.get_value("device.mac"),con.w.get_value("device.mode"))
    con.unit_monitor_update(con.w.get_value("device.mac"), con.w.get_value("update.mode"))
if __name__ == '__main__':
    configrollback_basic()
