# -*- coding: UTF-8 -*-

from AerohiveGUI import *
from AerohiveGUI.page.example import *
import time, re


class example(object):
    def __init__(self):
        self.w = WebGUI()
        
    def search(self, url, keyword):
        self.w.driver.get(url)
        self.w.wait_until_element_displayed(baidu_keyword_input)
        self.w.info('Get url successfully', True)
        self.w.input(baidu_keyword_input,keyword)
        self.w.click(baidu_search_btn)
        self.w.info('Search keyword successfully', True)