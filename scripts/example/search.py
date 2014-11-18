# -*- coding: UTF-8 -*-
from AerohiveSelenium.scripts.example import example

def key_search():
    con = example()
    con.search(con.w.get_value("visit.url"), con.w.get_value("visit.keyword"))
if __name__ == '__main__':
    key_search()
