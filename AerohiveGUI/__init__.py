#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author: Will

import argparse, os, sys, json, time, re, logging
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException
from utils import get_default_profile, get_default_log_file, get_default_test_data, josn_process, HtmlHandler, _timeout
'''
Todo: 
1.rewrite selenium.common.exceptions, when generate error, the AerohiveGUI can capture the page itself
'''

class WebGUIArgs(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='setup web testing')
        self.parser.add_argument('-r', '--remote-selenium', required=True, dest='remote_selenium',
                                 help='remote selenium url')
        self.parser.add_argument('-t', '--browser-type', required=False, default='ff', dest='browser_type',
                                 help='firefox,chrome , default is firefox')
        self.parser.add_argument('-p', '--browser-profile', required=False, default=get_default_profile(), dest='browser_profile',
                                 help='browser profile, firefox only, default is "webui/profile/ff"')
        self.parser.add_argument('-l', '--log-level', required=False, default='debug', dest='log_level',
                                 help='debug, info, warn, error, default is debug')
        self.parser.add_argument('-f', '--log-file', required=False, default=get_default_log_file(), dest='log_file',
                                 help='log file, default is "[dir of test file]/WebUI.html"')
        self.parser.add_argument('-d', '--data-file', required=False, default=get_default_test_data(), dest='data_file',
                                 help='data file (should be encoded in utf-8), default is "[dir of test file]/[name of test file].json"')
        self.parser.add_argument('--parameters', required=False, default=None, nargs='+', dest='parameters',
                                 help='parameters from command line have higher priority than which specified in data file')
        self.parser.add_argument('--preserve-session', required=False, default=False, dest='preserve_session', action='store_true',
                                 help='preserver session')
        self.parser.add_argument('--session-id', required=False, default=None, dest='session_id',
                                 help='use existing session')
        self._parse_args()
        # get data file 1st
        self._datafile_process()
        # update the value to the para you input
        self._parameters_process()
        self._logfile_process()
        self._init_logger()
        
    def _parse_args(self):
        self.args = self.parser.parse_args()
        self.remote_selenium = self.args.remote_selenium
        self.browser_type = self.args.browser_type.lower()
        self.browser_profile = self.args.browser_profile
        self.log_level = self.args.log_level.lower()
        self.log_file = self.args.log_file
        self.data_file = self.args.data_file
        self.parameters = self.args.parameters
        self.preserve_session = self.args.preserve_session
        self.session_id = self.args.session_id
    
    def _datafile_process(self):
        self.para_dict = josn_process(self.data_file)
    
    def _parameters_process(self):
        #print '--parameters is as below\n%s' % str(self.parameters)
        # primary is ['visit.url=http://www.google.com.hk', 'login.username=autotest', 'login.password=aerohive']
        # split with the first '=', if the para is not null
        self.para_t_list = [para.split('=', 1) for para in self.parameters if para]
        #print '--para_t_list is as below\n%s' % str(self.para_t_list)
        for para in self.para_t_list:
            self.para_dict[para[0]] = para[1]
        #print '--para_dict is as below\n%s' % str(self.para_dict)
    def _logfile_process(self):
        if not os.path.isabs(self.log_file):
            self.log_file = os.path.abspath(os.path.join('.', self.log_file))
        if not self.log_file.endswith('.html'):
            self.log_file = '%s.html' % self.log_file
        if os.path.exists(self.log_file):
            os.remove(self.log_file)
        self.log_pic_dir = '%s_pic' % self.log_file.replace('.html', '')
        try:
            os.mkdir(self.log_pic_dir)
        except OSError:
            f_l = os.listdir(self.log_pic_dir)
            if f_l:
                for f in f_l:
                    os.remove(self.log_pic_dir + '/' + f)

    def _init_logger(self):
        level = getattr(logging, self.log_level.upper())
        logger = logging.getLogger('AerohiveGUITest')
        logger.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')
        
        sh = logging.StreamHandler(sys.stdout)
        sh.setFormatter(formatter)
        logger.addHandler(sh)
        # Todo 
        # Research HtmlHandler 
        hh = HtmlHandler(self.log_file)
        hh.setFormatter(formatter)
        logger.addHandler(hh)
#        fh = logging.FileHandler(self.log_file)
#        fh.setFormatter(formatter)
#        logger.addHandler(fh)
        
        self.logger = logger

class WebGUIDriver(WebDriver):
    def __init__(self, command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=None, browser_profile=None, session_id=None):
        self.preserved_session_id = session_id
        self.browser_profile = browser_profile
        WebDriver.__init__(self, command_executor, desired_capabilities, browser_profile)

        # Todo 
        # Research Session 
    def start_session(self, desired_capabilities, browser_profile=None):
        if self.preserved_session_id:
            self.command_executor._commands['getSession'] = ('GET', '/session/$sessionId')
            self.session_id = self.preserved_session_id
            response = self.execute('getSession', {'sessionId ': self.session_id})
            self.session_id = response['sessionId']
            self.capabilities = response['value']
        else:
            WebDriver.start_session(self, desired_capabilities, browser_profile)


class WebGUI(object):
    def __init__(self):
        self.args = WebGUIArgs()
        self.remote_selenium = self.args.remote_selenium
        self.browser_type = self.args.browser_type
        self.browser_profile = self.args.browser_profile
        self.log_level = self.args.log_level
        self.log_file = self.args.log_file
        self.log_pic_dir = self.args.log_pic_dir
        self.para_dict = self.args.para_dict
        self.preserve_session = self.args.preserve_session
        self.session_id = self.args.session_id
        self.logger = self.args.logger
        self.log_pic_index = 0
        self.driver = None
        self._data = None
        self._assertion = None
        self._cleanup = []
        self.info('dump of webui\n' + str(self))
        # open browser
        self.openbrowser()
    
    def __str__(self):
        s = []
        s.append('remote-selenium = %s' % self.remote_selenium)
        s.append('browser-type = %s' % self.browser_type)
        if self.browser_type == 'ff':
            s.append('browser-profile = %s' % self.browser_profile)
        s.append('log-level = %s' % self.log_level)
        s.append('log-file = %s' % self.log_file)
        s.append('log-pic-dir = %s' % self.log_pic_dir)
        s.append('para_dict = %s' % str(self.para_dict))
        s.append('preserve-session = %s' % self.preserve_session)
        s.append('session-id = %s' % self.session_id)
        return '\n'.join(s)
    
    def openbrowser(self):
        browser_dict = {
                        'ff': "firefox",
                        'firefox': "firefox",
                        'ie': "ie",
                        'internetexplorer': "ie",
                        'googlechrome': "chrome",
                        'gc': "chrome",
                        'chrome': "chrome",
                        'opera' : "opera",
                        'phantomjs' : "phantomjs",
                        'htmlunit' : "htmlunit",
                        'htmlunitwithjs' : "htmlunitwithjs"}        
        browser_name = browser_dict[self.browser_type]
        capabilities = {
                        'firefox':DesiredCapabilities.FIREFOX,
                        'ie':DesiredCapabilities.INTERNETEXPLORER,
                        'chrome':DesiredCapabilities.CHROME,
                        'safari':DesiredCapabilities.SAFARI}

        if self.browser_type == 'firefox' and self.browser_profile:
            profile = FirefoxProfile(self.browser_profile)
        else:
            profile = FirefoxProfile(None) 

        if browser_name == 'firefox':
            self.driver = WebGUIDriver(self.remote_selenium, DesiredCapabilities.FIREFOX, profile, self.session_id)
        elif browser_name == 'chrome':
            self.driver = WebGUIDriver(self.remote_selenium, DesiredCapabilities.CHROME, profile, self.session_id)
        else:
            raise
        self.driver.maximize_window()
    
    def quit(self):
        if self.preserve_session:
            self.info('session preserved - %s' % self.driver.session_id)
            return
        return self.driver.quit()
    
    def get(self, url, timeout=10):
        self.driver.get(url)
    
    def refresh(self):
        self.driver.refresh()
    
    # locator's example is ('id','id_name'), *('id','id_name')='id','id_name'
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def wait_until_element_displayed(self, locator, timeout=60, msg=''):
        msg = msg if msg else 'displayed - %s' % str(locator)
        timeout = float(timeout)
        # method is a func
        method = lambda w: w.find_element(*locator) and w.find_element(*locator).is_displayed()
        return WebDriverWait(self.driver, timeout).until(method, msg)    
    
    def click_element(self, element):
        element.click()
        
    def click(self, locator):
        self.wait_until_element_displayed(locator)
        self.click_element(self.find_element(locator))
    
    def clear_element(self, element):
        element.clear()
        
    def clear(self, locator):
        self.clear_element(self.find_element(locator))

    def input_element(self, element, txt):
        self.click_element(element)
        if txt:
            element.send_keys(txt)
            
    def input(self, locator, txt):
        self.wait_until_element_displayed(locator)        
        self.input_element(self.find_element(locator), txt)
    
    def send_keys_element(self, element, key):
        element.send_keys(key)

    def send_keys(self, locator, key):
        self.send_keys_element(self.find_element(locator), key)

    def get_text_element(self, element):
        text = element.get_attribute("innerHTML")
        return text
    
    def get_text(self, locator):
        text = self.get_text_element(self.find_element(locator))
        return text
    
    def get_attribute_element(self, element, attr):
        return element.get_attribute(attr)
    
    def get_attribute(self, locator, attr):
        return self.get_attribute_element(self.find_element(locator), attr)

    #Judge if it has 'checked' in class name
    def is_checked_elemnet(self, element):
        e_class = self.get_attribute_element(element, "class")
        if re.search('checked', e_class):
            return True
        else:
            return False

    def is_checked(self, locator):
        return self.is_checked_elemnet(self.find_element(locator))
    
    def get_value(self, key):
        if self.para_dict.has_key(key):
            return self.para_dict[key]
    
    def current_url(self):
        return self.driver.current_url
    
    def screen_shot(self, path):
        #self.info('''Capture '%s' successfully''' % path)
        return self.driver.get_screenshot_as_file(path)
    
    def gen_log_msg(self, msg, is_pic=False):
        if is_pic == False or self.driver is None:
            return msg
        if is_pic == True:
            path = self.pic_path()
            #print 'Pic Path is %s' % path
            self.screen_shot(path)
        pic_link = './' + os.path.basename(os.path.dirname(path)) + '/' + os.path.basename(path)
        #print 'Pic link is %s' % pic_link
        return msg + HtmlHandler.PIC_TAG + pic_link
    
    def pic_path(self, name=''):
        pic_index = self.log_pic_index
        self.log_pic_index += 1
        return os.path.join(self.log_pic_dir, '%03d_%s.png' % (pic_index, name.replace(' ', '_').lower()))
    
    def debug(self, msg, is_pic=False):
        self.logger.debug(self.gen_log_msg(msg, is_pic))
    
    def info(self, msg, is_pic=False):
        self.logger.info(self.gen_log_msg(msg, is_pic))
    
    def warn(self, msg, is_pic=False):
        self.logger.warn(self.gen_log_msg(msg, is_pic))
    
    def error(self, msg, is_pic=False):
        self.logger.error(self.gen_log_msg(msg, is_pic))
    
