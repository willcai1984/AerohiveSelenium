# -*- coding: UTF-8 -*-
#login_auth
from selenium.webdriver.common.by import By
# url :https://192.168.91.178/index.php5

#login page
login_username_txt = (By.XPATH, '//input[@name="userName"]')
login_passwd_txt = (By.XPATH, '//input[@name="password"]')
login_login_btn = (By.XPATH, '//a')
invalid_url_txt = (By.XPATH, '//td[text()="404 Not Found"]')

#top menu
top_admin_link = (By.XPATH, '//a[text()="Admin"]')

#left menu
left_local_link = (By.XPATH, '//a[@id="selectedFeatures"]')
left_hivemanager_link = (By.XPATH, '//a[text()="HiveManager Configuration"]')
left_upgrade_link = (By.XPATH, '//a[text()="Upgrade HiveOS Software"]')

#Local network setting
local_dhcp_checkbox = (By.XPATH, '//input[@id="dhcpClient"]/..')
local_static_checkbox = (By.XPATH, '//input[@id="staticIp"]/..')
local_static_ip_txt = (By.XPATH, '//div[label="Interface IP Address"]/div/input')
local_static_netmask_txt = (By.XPATH, '//div[label="Netmask"]/div/input')
local_static_gateway_txt = (By.XPATH, '//div[label="Gateway"]/div/input')
local_static_dns_txt = (By.XPATH, '//div[label="DNS Server"]/div/input')

local_apply_btn = (By.XPATH, '//button[text()="Apply"]')

#HiveManager Configuration
hm_para_checkbox = (By.XPATH, '//input[@id="chkHiveManagment"]/..')
hm_para_checkboxdiv = (By.XPATH, '//input[@id="chkHiveManagment"]/../..')
hm_http_checkbox = (By.XPATH, '//input[@id="chkTransportHttp"]/..')
hm_http_checkboxdiv = (By.XPATH, '//input[@id="chkTransportHttp"]/../..')
hm_proxy_checkbox = (By.XPATH, '//input[@id="chkHttpProxy"]/..')
hm_proxy_checkboxdiv = (By.XPATH, '//input[@id="chkHttpProxy"]/../..')
hm_proxy_auth_checkbox = (By.XPATH, '//input[@id="chkHttpProxyAuth"]/..')
hm_proxy_auth_checkboxdiv = (By.XPATH, '//input[@id="chkHttpProxyAuth"]/../..')
hm_para_ip_txt = (By.XPATH, '//input[@name="hiveManagementIpAddr"]')
hm_para_port_txt = (By.XPATH, '//input[@name="txtHmServerPort"]')
hm_proxy_ip_txt = (By.XPATH, '//input[@name="txtHttpProxy"]')
hm_proxy_port_txt = (By.XPATH, '//input[@name="txtHttpProxyPort"]')
hm_proxy_auth_user_txt = (By.XPATH, '//input[@name="txtHttpProxyUserName"]')
hm_proxy_auth_pwd_txt = (By.XPATH, '//input[@name="txtHttpProxyPwd"]')

hm_apply_btn = (By.XPATH, '//button[text()="Apply"]')

#Upgrade HiveOS Software
#upgrade_image_file
#upgrade_time_checkbox = (By.XPATH, '//input[@name="activeAP"]/..')
#upgrade_next_checkbox = (By.XPATH, '//input[@name="activeAP"]/..')

upgrade_apply_btn = (By.XPATH, '//button[text()="Apply"]')

#Information
info_ok_btn = (By.XPATH, '//button[text()="OK"]')

info_continue_btn = (By.XPATH, '//button[text()="Continue"]')
