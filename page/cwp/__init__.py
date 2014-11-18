# -*- coding: UTF-8 -*-
#login_auth
from selenium.webdriver.common.by import By
login_auth_title = 'Login'
login_auth_username_txt = (By.XPATH,'//input[@name="username"]')
login_auth_password_txt = (By.XPATH,'//input[@name="password"]')
login_auth_login_btn = (By.XPATH,'//input[@class="login_button"]')
#login_self
login_auth_first_name_txt = (By.XPATH,'//input[@placeholder="first name*"]')
login_auth_last_name_txt = (By.XPATH,'//input[@placeholder="last name*"]')
login_auth_email_txt = (By.XPATH,'//input[@placeholder="email*"]')
login_auth_phone_txt = (By.XPATH,'//input[@placeholder="phone"]')
login_auth_visiting_txt =(By.XPATH,'//input[@placeholder="visiting*"]')
login_auth_reason_txt = (By.XPATH,'//input[@placeholder="reason"]')
login_auth_register_btn = (By.XPATH,'//input[@class="reg_button"]')
#login_acceptance
login_auth_accept_title = (By.XPATH,'//div[@id="h2Title"]')
login_auth_accept_btn = (By.XPATH,'//input[@id="SubmitButton"]')
#login_mutiurl,/html/body/table/tbody/tr[2]/td[1]/div/form/img
login_auth_mutiurl_img = (By.XPATH,'//img[@src="apple.png"]')
#login_ecwp
login_auth_ecwp_title = (By.XPATH,'//label[@for="ID_formeb956bcf_username"]')
login_auth_ecwp_username = (By.XPATH,'//input[@name="username"]')
login_auth_ecwp_password = (By.XPATH,'//input[@id="ID_formeb956bcf_password"]')
login_auth_ecwp_login_btn = (By.XPATH,'//input[@id="ID_formeb956bcf_submit"]')

#login_success
login_success_title = 'Login Successful'
login_success_info=(By.XPATH,'//div[@id="regularTitle"]')
login_success_icon=(By.XPATH,'//div[@id="h2Title"]')
#login_failed
login_failed_title = 'Login Unsuccessful'
login_failed_info = (By.XPATH,'//div[h2="Login Failed!"]')
login_failed_reason = (By.XPATH,'//div[@id="reason"]')

#logout_popup
logout_popup_title_part = 'Network Access Timer'
logout_popup_left_div = ('id', 'left')
logout_popup_btn = (By.XPATH,'//input[@value="Log Out"]')

#logout_success
logout_success_title = 'Logging out'

#walled-garden page
access_Internet_ip_page = (By.XPATH,'//input[@id="userName"]')
#ppsk_login_success
ppsk_login_success_info = (By.XPATH,'//p[@id="thanksNote"]')
ppsk_login_success_ssid = (By.XPATH,'//span[@id="ppsk_ssid"]')
ppsk_login_success_key = (By.XPATH,'//span[@id="ppsk_pwd"]')
ppsk_login_fail_reason = (By.XPATH,'//div[@id="reason"]')
