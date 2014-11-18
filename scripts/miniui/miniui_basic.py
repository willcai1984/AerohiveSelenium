# -*- coding: UTF-8 -*-

#python cwp_login_positive.py -r http://${sta.ip}:4444/wd/hub -t ie -f logFile --parameters
from AerohiveSelenium.scripts.miniui import miniui 

def miniui_basic():
    con = miniui()
    if con.w.get_value("visit.is_valid")=="true":
        con.unit_login(con.w.get_value("visit.url"), con.w.get_value("login.username"), con.w.get_value("login.password"))
        if con.w.get_value("config.mode") == "local":
            con.unit_local_modify(con.w.get_value("local.mode"), con.w.get_value("local.dns"), con.w.get_value("local.ip"), con.w.get_value("local.netmask"), con.w.get_value("local.gateway"))
        elif con.w.get_value("config.mode") == "hm":
            con.unit_hm(con.w.get_value("hm.is_para"), con.w.get_value("hm.is_http"), con.w.get_value("hm.is_proxy"), con.w.get_value("hm.para_ip"), con.w.get_value("hm.para_port"), con.w.get_value("hm.proxy_ip"), con.w.get_value("hm.proxy_port"), con.w.get_value("hm.is_auth"), con.w.get_value("hm.user"), con.w.get_value("hm.passwd"))
    else:
        con.unit_invalid(con.w.get_value("visit.url"))
if __name__ == '__main__':
    miniui_basic()
