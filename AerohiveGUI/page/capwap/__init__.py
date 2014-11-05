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

monitor_title = 'All Devices'
monitor_modify_button = (By.XPATH, '//input[@value="Modify"]')
monitor_update_button = (By.XPATH, '//input[@value="Update..."]')
monitor_update_device_option = (By.XPATH, '//a[.="Update Devices"]')

monitor_utilities_button = (By.XPATH, '//input[@value="Utilities..."]')
monitor_device_button = (By.XPATH, '//input[@value="Device Inventory..."]')


modify_title = 'All Devices'
modify_save_button = (By.XPATH, '''//input[@value="Save"][@onclick="submitAction('update2');"]''')
modify_cancel_button = (By.XPATH, '''//input[@value="Cancel"][@onclick="submitAction('cancel');"]''')
modify_networkpolicy_droplist = (By.XPATH, '//select[@id="hiveAp_configTemplate"]')
modify_networkpolicy_ap_option = (By.XPATH, '//select[@id="hiveAp_configTemplate"]/option[.="def-ap"]')
modify_networkpolicy_router_option = (By.XPATH, '//select[@id="hiveAp_configTemplate"]/option[.="def-router"]')
modify_credentials_button = (By.XPATH, '''//span[@onclick="alternateFoldingContent('credentials');"]''')
modify_credentials_primary_droplist = (By.XPATH, '//select[@id="capwapSelect"]')
modify_credentials_primary_default_option = (By.XPATH, '//select[@id="capwapSelect"]/option[.="1.1.1.1"]/../option[1]')
modify_credentials_primary_hm1_option = (By.XPATH, '//select[@id="capwapSelect"]/option[.="192.168.10.201"]')
modify_credentials_backup_droplist = (By.XPATH, '//select[@id="capwapBackupSelect"]')
modify_credentials_backup_default_option = (By.XPATH, '//select[@id="capwapBackupSelect"]/option[.="2.2.2.2"]/../option[1]')


update_complete_checkbox = (By.XPATH, '//input[@id="simplly_update_complete_config"]')
update_update_button = (By.XPATH, '//input[@onclick="submitSimplifiedUpdate();"]')
update_cancel_button = (By.XPATH, '//input[@onclick="hideSimpllyUpdatePanel();"]')

reboot_auto_checkbox = (By.XPATH, '//input[@id="rebootAtOnce"]')
reboot_manual_checkbox = (By.XPATH, '//input[@id="rebootManually"]')
reboot_ok_button = (By.XPATH, '//input[@onclick="submitDeviceRebootOpt();"]')
reboot_cancel_button = (By.XPATH, '//input[@onclick="hideRebootPanel();"]')






