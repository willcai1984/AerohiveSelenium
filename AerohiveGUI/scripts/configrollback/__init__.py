# -*- coding: UTF-8 -*-

from AerohiveGUI import WebGUI, _timeout
from AerohiveGUI.page.configrollback import *
import time, re
from selenium.common.exceptions import *

class ConfigRollBack(object):
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
    
    
    def unit_monitor_modify(self, mac, mode='ap'):
        self.w.wait_until_element_displayed(top_monitor_link)
        self.w.click(top_monitor_link)
        self.w.wait_until_element_displayed(monitor_modify_button)
        #The expect mac format is E01C41003D80
        monitor_device_entry_checkbox = (By.XPATH, '//td[starts-with(text(),"%s")]/../td[1]/input' % re.sub(' |:|,', '', mac).upper())
        self.w.click(monitor_device_entry_checkbox)
        self.w.info('Select device successfully', True)
        self.w.click(monitor_modify_button)
        #modify page
        #self.w.click(modify_networkpolicy_droplist)
        #click cannot select the option, we need click option directly without click droplist
        if mode == 'ap':
            self.w.click(modify_networkpolicy_ap_option)
            #self.w.send_keys(modify_networkpolicy_ap_option,Keys.ENTER)
        elif mode == 'router':
            self.w.click(modify_networkpolicy_router_option)
            #self.w.send_keys(modify_networkpolicy_router_option,Keys.ENTER)
        self.w.info('Select default policy successfully', True)
        self.w.click(modify_credentials_button)
        #self.w.click(modify_credentials_primary_droplist)
        self.w.click(modify_credentials_primary_invalidserver_option)
        #self.w.click(modify_credentials_backup_droplist)
        self.w.click(modify_credentials_backup_invalidserver_option)
        self.w.info('Modify capwap server successfully', True)
        self.w.click(modify_save_button)
        
    def unit_monitor_update(self, mac, mode='complete'):
        self.w.wait_until_element_displayed(top_monitor_link)
        self.w.click(top_monitor_link)
        #u'E01C41003D80 &nbsp;' cannot locator via xpath with spaca/&nbsp;/${nbsp}, so use start with instead        
        monitor_device_entry_checkbox = (By.XPATH, '//td[starts-with(text(),"%s")]/../td[1]/input' % re.sub(' |:|,', '', mac).upper())
        try:
            self.w.wait_until_element_displayed(monitor_device_entry_checkbox, 5)
        except TimeoutException, e:
            self.w.wait_until_element_displayed(top_monitor_link)
            self.w.click(top_monitor_link)
        self.w.wait_until_element_displayed(monitor_device_entry_checkbox, 20)
        self.w.click(monitor_device_entry_checkbox)
        self.w.info('Select device successfully', True)
        self.w.click(monitor_update_button) 
        self.w.click(monitor_update_device_option)
        self.w.info('Click update button successfully', True)
        self.w.wait_until_element_displayed(update_complete_checkbox)
        if mode == 'complete':
            self.w.click(update_complete_checkbox)
            self.w.info('Select complete mode', True)
        else:
            self.w.info('Select delta mode', True)
        self.w.click(update_update_button)
        time.sleep(3)
        #after click update may pop up reboot page, reboot auto
        try:
            self.w.click(reboot_auto_checkbox)
        except TimeoutException, e:
            self.w.info('No reboot option, return successful', True)
            return
        self.w.info('Enter to reboot option, click reboot btn', True)
        self.w.click(reboot_ok_button)
        
    
        
