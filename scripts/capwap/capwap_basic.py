# -*- coding: UTF-8 -*-

#python cwp_login_positive.py -r http://${sta.ip}:4444/wd/hub -t ie -f logFile --parameters
from AerohiveSelenium.scripts.capwap import capwap 

def capwap_basic():
    con = capwap()
    if con.w.get_value("update.is_check") == 'false' and not con.w.session_id:
        con.w.info("Enter to new session mode and not check update state mode")
        con.unit_login(con.w.get_value("visit.url"), con.w.get_value("login.username"), con.w.get_value("login.password"))
        con.unit_monitor_modify(con.w.get_value("device.mac"), con.w.get_value("device.mode"))
        con.unit_monitor_update(con.w.get_value("device.mac"), con.w.get_value("update.mode"))
    if con.w.get_value("update.is_check") == 'true' and not con.w.session_id:
        con.w.info("Enter to new session and check update state mode")
        con.unit_login(con.w.get_value("visit.url"), con.w.get_value("login.username"), con.w.get_value("login.password"))
        con.unit_monitor_state(con.w.get_value("device.mac"))
    if con.w.get_value("update.is_check") == 'true' and con.w.session_id:
        con.w.info("Enter to inherit session and check update state mode")
        con.unit_monitor_state(con.w.get_value("device.mac"))
    con.w.quit()
if __name__ == '__main__':
    capwap_basic()
