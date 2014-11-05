# -*- coding: UTF-8 -*-

from AerohiveGUI import WebGUI, _timeout
from AerohiveGUI.page.miniui import *
import time, re
from selenium.common.exceptions import *

class miniui(object):
    def __init__(self):
        self.w = WebGUI()
        
    def unit_login(self, url, user, passwd):
        self.w.driver.get(url)
        self.w.wait_until_element_displayed(login_username_txt)
        self.w.clear(login_username_txt)
        self.w.input(login_username_txt, user)
        self.w.clear(login_passwd_txt)
        self.w.input(login_passwd_txt, passwd)
        self.w.info('Login successfully', True)
        self.w.click(login_login_btn)
    
    def unit_invalid(self, url):
        self.w.driver.get(url)
        self.w.wait_until_element_displayed(invalid_url_txt)
        self.w.info('404 Not Found', True)
    
    def unit_local_modify(self, mode, dns, ip, netmask, gateway):
        self.w.wait_until_element_displayed(left_local_link)
        self.w.click(left_local_link)
        self.w.wait_until_element_displayed(local_static_dns_txt)
        self.w.info('Enter to Local network setting successfully', True)
        #sleep 10s for web reload the data from our device
        self.w.info("Sleep 10s for web read our devices' data")
        time.sleep(10)
        if mode == "dhcp":
            self.w.info('Enter to DHCP mode')
            self.w.click(local_dhcp_checkbox)
            self.w.clear(local_static_dns_txt)
            self.w.input(local_static_dns_txt, dns)          
            self.w.info('Modify Local network setting successfully', True)
            self.w.click(local_apply_btn)
 #           self.w.wait_until_element_displayed(info_ok_btn)
            self.w.info('Apply modify successfully', True)
#            self.w.click(info_ok_btn)
        elif mode == "static":
            self.w.info('Enter to STATIC mode')
            self.w.click(local_static_checkbox)
            self.w.wait_until_element_displayed(local_static_ip_txt)
            self.w.clear(local_static_ip_txt)
            self.w.input(local_static_ip_txt, ip)
            self.w.clear(local_static_netmask_txt)
            self.w.input(local_static_netmask_txt, netmask)            
            self.w.clear(local_static_gateway_txt)
            self.w.input(local_static_gateway_txt, gateway)            
            self.w.clear(local_static_dns_txt)
            self.w.input(local_static_dns_txt, dns)
            self.w.info('Modify Local network setting successfully', True)
            self.w.click(local_apply_btn)
            self.w.wait_until_element_displayed(info_continue_btn)
            self.w.info('Apply modify successfully', True)
            self.w.click(info_continue_btn)
            self.w.info('Apply modify successfully', True)
            
    def unit_hm(self, is_para, is_http, is_proxy, para_ip, para_port, proxy_ip, proxy_port, is_auth, user, passwd):
        self.w.wait_until_element_displayed(left_hivemanager_link)
        self.w.click(left_hivemanager_link)        
        self.w.wait_until_element_displayed(hm_para_checkbox)
        self.w.info('Enter to HiveManager Configuration successfully', True)
        #sleep 10s for web reload the data from our device
        self.w.info("Sleep 5s for web read our devices' data")
        time.sleep(5)
        if is_para == "true":
            # Add by will
            if not self.w.is_checked(hm_para_checkboxdiv):
                self.w.click(hm_para_checkbox)
            self.w.wait_until_element_displayed(hm_para_ip_txt)
            self.w.clear(hm_para_ip_txt)
            self.w.input(hm_para_ip_txt, para_ip)
            self.w.clear(hm_para_port_txt)
            self.w.input(hm_para_port_txt, para_port) 
            self.w.info('Config hm parameters successfully', True)             
        if is_http == "true":
            # Add by will
            if not self.w.is_checked(hm_http_checkboxdiv):
                self.w.click(hm_http_checkbox)
            self.w.info('Config http transport method successfully', True)
        else:
            if self.w.is_checked(hm_http_checkboxdiv):
                self.w.click(hm_http_checkbox)
            self.w.info('Cancel http transport method successfully', True)
        if is_proxy == "true":
            # Add by will
            if not self.w.is_checked(hm_proxy_checkboxdiv):
                self.w.click(hm_proxy_checkbox)
            self.w.wait_until_element_displayed(hm_proxy_ip_txt)
            self.w.clear(hm_proxy_ip_txt)
            self.w.input(hm_proxy_ip_txt, proxy_ip)
            self.w.clear(hm_proxy_port_txt)
            self.w.input(hm_proxy_port_txt, proxy_port)   
            self.w.info('Config http proxy server successfully', True) 
            if is_auth == "true":
            	if not self.w.is_checked(hm_proxy_auth_checkboxdiv):
            		self.w.click(hm_proxy_auth_checkbox)
                self.w.wait_until_element_displayed(hm_proxy_auth_user_txt)
                self.w.clear(hm_proxy_auth_user_txt)
                self.w.input(hm_proxy_auth_user_txt, user)
                self.w.clear(hm_proxy_auth_pwd_txt)
                self.w.input(hm_proxy_auth_pwd_txt, passwd)
                self.w.info('Config auth for http proxy successfully', True)
            else:
            	if self.w.is_checked(hm_proxy_auth_checkboxdiv):
            		self.w.click(hm_proxy_auth_checkbox)
            	self.w.info('Cancel auth for http proxy successfully', True)
        else:
           	if self.w.is_checked(hm_proxy_checkboxdiv):
                   self.w.click(hm_proxy_checkbox)
                self.w.info('Cancel http proxy server successfully', True)         
		self.w.click(hm_apply_btn)
        self.w.click(hm_apply_btn)
        self.w.info('Apply modify successfully', True)
 
    
        
    
        
