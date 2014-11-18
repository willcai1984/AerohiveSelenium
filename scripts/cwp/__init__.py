# -*- coding: UTF-8 -*-

from AerohiveSelenium import WebGUI, _timeout
from AerohiveSelenium.page.cwp import *
import time

class CWP(object):
    def __init__(self):
        self.w = WebGUI()
        
    def unit_login(self, url, permit_url, user, passwd):
        self.w.driver.get(url)
        self.w.wait_until_element_displayed(login_auth_username_txt)
        self.w.info('''Before Authentication, redirect-url is "%s"''' % self.w.current_url())
        self.w.clear(login_auth_username_txt)
        self.w.input(login_auth_username_txt, user)
        self.w.clear(login_auth_password_txt)
        self.w.input(login_auth_password_txt, passwd)
        self.w.info('handle login form', True)
        self.w.click(login_auth_login_btn)
 #       self.w.driver.get(permit_url)
#        self.w.info("access Internet",True)
#        self.w.wait_until_element_displayed(access_Internet_ip_page)

    def unit_reg(self, url, first, last, email, phone, visiting, reason):
        self.w.driver.get(url)
        self.w.wait_until_element_displayed(login_auth_first_name_txt)
        self.w.info('''Before Authentication, redirect-url is "%s"''' % self.w.current_url())
        self.w.clear(login_auth_first_name_txt)
        self.w.input(login_auth_first_name_txt, first)
        self.w.clear(login_auth_last_name_txt)
        self.w.input(login_auth_last_name_txt, last)
        self.w.clear(login_auth_email_txt)
        self.w.input(login_auth_email_txt, email)
        self.w.clear(login_auth_phone_txt)
        self.w.input(login_auth_phone_txt, phone)
        self.w.clear(login_auth_visiting_txt)
        self.w.input(login_auth_visiting_txt, visiting)     
        self.w.clear(login_auth_reason_txt)
        self.w.input(login_auth_reason_txt, reason)
        self.w.info('handle register form', True)
        self.w.click(login_auth_register_btn)
        
    def unit_accept(self, url):
        self.w.driver.get(url)
        self.w.wait_until_element_displayed(login_auth_accept_btn)
        self.w.info('handle login form', True)
        self.w.click(login_auth_accept_btn)
    def unit_mutiurl(self, url):
        self.w.driver.get(url)
        self.w.wait_until_element_displayed(login_auth_mutiurl_img)
        self.w.info('handle login form', True)
        self.w.click(login_auth_mutiurl_img)
        self.w.info('''After Authentication, redirect-url is "%s"''' % self.w.current_url())
    def unit_ecwp(self, url, user, passwd):
        self.w.driver.get(url)
        time.sleep(1)
        self.w.driver.get(url)
        self.w.wait_until_element_displayed(login_auth_ecwp_username)
        self.w.info('''Before Authentication, redirect-url is "%s"''' % self.w.current_url(), True)
        self.w.clear(login_auth_ecwp_username)
        self.w.input(login_auth_ecwp_username, user)
        self.w.clear(login_auth_ecwp_password)
        self.w.input(login_auth_ecwp_password, passwd)
        self.w.info('handle login form', True)
        self.w.click(login_auth_ecwp_login_btn)
        
    def unit_walled_garden(self, url):
        self.w.driver.get(url)
        self.w.wait_until_element_displayed(access_Internet_ip_page)
        self.w.info('open Internent in walled-garden', True)
        
    def unit_success_redirect_orginal(self):
        self.w.wait_until_element_displayed(access_Internet_ip_page, 10)
        self.w.info('''The original url is "%s"''' % self.w.current_url(), True)
        
    def unit_login_result(self, is_success=True, is_redirect="none"):
        if is_success == "True" or is_success == "true":#login successful page and stay at the successful page.
            self.w.wait_until_element_displayed(login_success_info)
            self.w.info('login successfully page', True)
            self.w.info('''After Authentication, redirect-url is "%s"''' % self.w.current_url())
            is_success = "True"
        if is_success == "false" and is_redirect == "none":#if login fail,stay at failure page.
            self.w.wait_until_element_displayed(login_failed_info)
            self.w.info('Login failed page', True)
            self.w.info('''After Authentication, redirect-url is "%s"''' % self.w.current_url())
            self.w.info('CWP auth failed reason is "%s"' % self.w.get_text(login_failed_reason))
        elif is_redirect == "failure_redirect":#failure redirect to external page
            self.w.wait_until_element_displayed(access_Internet_ip_page)
            self.w.info('The failuer redirect external page', True)
        elif is_redirect == "failure_redirect3":#failure redirect to login page
            self.w.wait_until_element_displayed(login_auth_username_txt)
            self.w.info('The failuer redirect login page', True)
            self.w.info('''After Authentication, redirect-url is "%s"''' % self.w.current_url())
    def unit_ppsk_login_result(self,is_ppsk_success=True):
        if  is_ppsk_success == "True" or is_ppsk_success=="true":
            self.w.wait_until_element_displayed(ppsk_login_success_info)
            self.w.info('Login successfully,show the ppsk ssid and psk', True)
            self.w.info('''Login ppsk_ssid_is:"%s"'''%self.w.get_text(ppsk_login_success_ssid))
            self.w.info('''Login password_is:"%s"'''%self.w.get_text(ppsk_login_success_key))
        else:
            self.w.wait_until_element_displayed(ppsk_login_fail_reason)
            self.w.info('Login failed,show the failed reason', True)
            self.w.info('''failed reason is:"%s"'''%self.w.get_text(ppsk_login_fail_reason))
 #   def unit_login_result(self, is_success=True):
 #       if is_success == "True" or is_success == "true":
 #           self.w.wait_until_element_displayed(login_success_info)
 #           self.w.info('login successfully page', True)
 #       else:
 #           self.w.wait_until_element_displayed(login_failed_info)
 #           self.w.info('Login failed page', True)
 #           self.w.info('CWP auth failed reason is "%s"' % self.w.get_text(login_failed_reason))
 #       self.w.info('''After Authentication, redirect-url is "%s"''' % self.w.current_url())
    def unit_access_internet(self, permit_url):
            self.w.get(permit_url)
            self.w.info("access Internet permit url", True)
            time.sleep(1)
            self.w.get(permit_url)
            self.w.info("access Internet permit url twice", True)
            time.sleep(1)
            self.w.get(permit_url)
            self.w.info("access Internet permit url third times", True)
            self.w.wait_until_element_displayed(access_Internet_ip_page)
            
    def unit_logout(self, logout_title, timeout=60):
        _timeout(len(self.w.driver.window_handles) > 1, timeout)
        is_logout = False
        for window in self.w.driver.window_handles:
            self.w.driver.switch_to_window(window)
            if logout_popup_title_part in self.w.driver.title:
                is_logout = True
                break
        self.w.info('Get to login page successfully', True)
        if not is_logout:
            self.w.info('Cannot find pop up page, capture picture', True)
            raise AssertionError, '''Cannot find pop up page,raise error'''
        self.w.wait_until_element_displayed(logout_popup_btn)
        self.w.info('Wait logout pop up successfully', True)
        self.w.click(logout_popup_btn)
        self.w.info('Wait alert successfully')
        # get alert()
        a = self.w.driver.switch_to_alert()
        a.accept()
        if self.w.driver.title in logout_success_title:
            pass
            #self.w.info('Click log out successfully', True)
        self.w.info('Logout successfully', True)
        #self.w.info('close the pop up', True)
