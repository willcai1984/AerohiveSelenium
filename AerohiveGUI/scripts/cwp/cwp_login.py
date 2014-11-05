# -*- coding: UTF-8 -*-

#python cwp_login_positive.py -r http://${sta.ip}:4444/wd/hub -t ie -f logFile --parameters
from AerohiveGUI.scripts.cwp import CWP 
import time
def cwp_login():
    cwp = CWP()
    if cwp.w.get_value("login.is_permit") == "true":
        cwp.unit_walled_garden(cwp.w.get_value("visit.permit_url"))
    if cwp.w.get_value("login.mode") == "normal":
        cwp.unit_login(cwp.w.get_value("visit.url"), cwp.w.get_value("visit.permit_url"),cwp.w.get_value("login.username"), cwp.w.get_value("login.password"))
    elif cwp.w.get_value("login.mode") == "register":
        cwp.unit_reg(cwp.w.get_value("visit.url"), cwp.w.get_value("register.firstname"), cwp.w.get_value("register.lastname"), cwp.w.get_value("register.email"), cwp.w.get_value("register.phone"), cwp.w.get_value("register.visiting"), cwp.w.get_value("register.reason"))
    elif cwp.w.get_value("login.mode") == "accept":
        cwp.unit_accept(cwp.w.get_value("visit.url"))
    elif cwp.w.get_value("login.mode") == "ecwp":
        cwp.unit_ecwp(cwp.w.get_value("visit.url"),cwp.w.get_value("login.username"), cwp.w.get_value("login.password"))
    elif cwp.w.get_value("login.mode") == "mutiurl":
        cwp.unit_mutiurl(cwp.w.get_value("visit.url"))
    else:
        print "Error mode, your mode is '%s', Expect is normal/register/ecwp/accept" % cwp.w.get_value("login.mode")
    if cwp.w.get_value("login.is_result") == "true":#only muti-url mode needn't login result page(success or fail).
        cwp.unit_login_result(cwp.w.get_value("login.is_success"),cwp.w.get_value("login.is_redirect"))
    if cwp.w.get_value("login.is_redirect")=="success_orginal":
        cwp.unit_success_redirect_orginal()
    if cwp.w.get_value("login.is_ppsk")=="true":
        cwp.unit_ppsk_login_result(cwp.w.get_value("login.is_ppsk_success"))
    cwp.w.quit()
if __name__ == '__main__':
    cwp_login()
