# -*- coding: UTF-8 -*-

from AerohiveGUI import WebGUI, _timeout
from AerohiveGUI.page.hm import *
import time, re
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys


class hm(object):
    def __init__(self):
        self.w = WebGUI()
        
    def unit_login(self, url, user, passwd):
        self.w.driver.get(url)
        self.w.wait_until_element_displayed(login_username_txt)
        self.w.clear(login_username_txt)
        self.w.input(login_username_txt, user)
        self.w.clear(login_passwd_txt)
        self.w.input(login_passwd_txt, passwd)
        self.w.info('handle login form', True)
        self.w.click(login_login_btn)
    
    def unit_config_update(self, policy, mac, mode="complete"):
        self.w.wait_until_element_displayed(top_config_link)
        self.w.click(top_config_link)
        self.w.wait_until_element_displayed(config_n_ok_btn)
        self.w.click((By.XPATH, '//span[@title="%s"]' % policy))
        self.w.info('Configure network done', True)
        self.w.click(config_n_ok_btn)
        time.sleep(2)
        self.w.info('Configure interface network done', True)
        self.w.click(config_i_ctn_btn)
        time.sleep(2)
        self.w.click(config_u_update_filter_none_option)
        time.sleep(5)
        
#        self.w.click(config_u_setting_btn)
#        if mode == 'complete':
#            self.w.click(config_u_setting_complete)
#        elif mode == 'delta':
#            self.w.click(config_u_setting_delta)
#        else:
#            raise ValueError, "The mode %s should be 'complete' or 'delta'" % mode
#        self.w.click(config_u_setting_save)
        device_mac = re.sub(r'[ :/]', '', mac.upper())
        if len(device_mac) != 12:
            raise ValueError, "The mac %s format is not as expect xx:xx:xx:xx:xx:xx" % mac
        device_mac = device_mac[:2] + ':' + device_mac[2:4] + ':' + device_mac[4:6] + ':' + device_mac[6:8] + ':' + device_mac[8:10] + ':' + device_mac[10:]
        device_checkbox = (By.XPATH, '//td[contains(text(),"%s")]/../td[1]/input' % device_mac)
        self.w.click(device_checkbox)
        self.w.info('Select device successfully', True)
#        ##page up 5 times
#        for i in range(5):
#            self.w.send_keys(config_u_update_btn, Keys.PAGE_UP)
#        
        self.w.click(config_u_update_btn)
        self.w.click(config_u_update_device_btn)
        self.w.info('Click update btn successfully', True)
        
        try:
            self.w.wait_until_element_displayed(config_u_update_confirm_yes_btn, 10)
            self.w.click(config_u_update_confirm_yes_btn)
        except TimeoutException, e:
            self.w.info('No policy change, so no confirm form jumped', False)
        
        self.w.wait_until_element_displayed(config_u_update_complete_checkbox)
        if mode == 'complete':
            self.w.click(config_u_update_complete_checkbox)
            self.w.info('Select complete mode', True)
        else:
            self.w.info('Select delta mode', True)  
        
        self.w.click(config_u_update_update_btn)
        time.sleep(3)
        #after click update may pop up reboot page, reboot auto
        try:
            self.w.click(config_u_update_reboot_auto_checkbox)
        except TimeoutException, e:
            self.w.info('No reboot option, return successful', True)
            return
        self.w.info('Enter to reboot option, click reboot btn', True)
        self.w.click(config_u_update_reboot_ok_btn)
