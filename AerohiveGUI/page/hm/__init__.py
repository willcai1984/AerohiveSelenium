# -*- coding: UTF-8 -*-
#login_auth
from selenium.webdriver.common.by import By

#login page
login_title = 'HiveManager Login'
login_username_txt = (By.XPATH, '//input[@id="userName"]')
login_passwd_txt = (By.XPATH, '//input[@id="authenticateFormID_password"]')
login_login_btn = (By.XPATH, '//tr/td/a')
login_success_title = 'Dashboard'

top_home_link = (By.XPATH, '//td[@class="top_menu_bg"][1]/table/tbody/tr/td[2]/a')
top_dashboard_link = (By.XPATH, '//td[@class="top_menu_bg"][1]/table/tbody/tr/td[3]/a')
top_monitor_link = (By.XPATH, '//td[@class="top_menu_bg"][1]/table/tbody/tr/td[4]/a')
top_report_link = (By.XPATH, '//td[@class="top_menu_bg"][1]/table/tbody/tr/td[6]/a')
top_maps_link = (By.XPATH, '//td[@class="top_menu_bg"][1]/table/tbody/tr/td[8]/a')
top_config_link = (By.XPATH, '//td[@class="top_menu_bg"][1]/table/tbody/tr/td[10]/a')
top_tool_link = (By.XPATH, '//td[@class="top_menu_bg"][1]/table/tbody/tr/td[12]/a')
    
config_n_ok_btn=(By.XPATH,'//span[@id="selectNetWorkPolicySpanId"]')
config_i_ctn_btn=(By.XPATH,'//span[@id="netWorkPolicySpanId"]')
config_u_setting_btn=(By.XPATH,'//a[@title="Settings"]')
config_u_setting_complete=(By.XPATH,'//label[.="Complete Upload"]')
config_u_setting_delta=(By.XPATH,'//label[starts-with(text(),"Delta Upload (Compare with the run")]')
config_u_setting_save=(By.XPATH,'//a[@title="Save"]')

config_u_update_btn=(By.XPATH,'//a[@id="updateMenu"]')

config_u_update_device_btn=(By.XPATH,'//a[.="Update Devices"]')

config_u_update_filter_none_option=(By.XPATH,'//option[.="None"]')

config_u_update_confirm_yes_btn=(By.XPATH,'//button[@id="yui-gen13-button"]')

config_u_update_complete_checkbox = (By.XPATH, '//input[@id="simplly_update_complete_config"]')
config_u_update_update_btn = (By.XPATH, '//input[@onclick="submitSimplifiedUpdate();"]')
config_u_update_cancel_btn = (By.XPATH, '//input[@onclick="hideSimpllyUpdatePanel();"]')

config_u_update_reboot_auto_checkbox = (By.XPATH, '//input[@id="rebootAtOnce"]')
config_u_update_reboot_manual_checkbox = (By.XPATH, '//input[@id="rebootManually"]')
config_u_update_reboot_ok_btn = (By.XPATH, '//input[@onclick="submitDeviceRebootOpt();"]')
config_u_update_reboot_cancel_btn = (By.XPATH, '//input[@onclick="hideRebootPanel();"]')


