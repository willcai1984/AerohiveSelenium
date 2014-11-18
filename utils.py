# -*- coding: UTF-8 -*-
import os.path, sys, json, re, time
from logging import FileHandler
from cgi import escape

def get_default_profile():
    return os.path.join(os.path.dirname(__file__), 'profile', 'ff')

def get_default_log_file():
    test = sys.argv[0]
    test_dir, test_file = os.path.split(test)
    return os.path.join(test_dir, 'WebUI.html')

def get_default_test_data():
    test = sys.argv[0]
    test_dir, test_file = os.path.split(test)
    return os.path.join(test_dir, '%s.json' % os.path.splitext(test_file)[0])

def josn_process(path):
    with open(path) as f_open:
        f_read = f_open.read()
    f_j = json.loads(f_read)
    j_dict = {}
    if f_j:
        for key1 in f_j:
            if type(f_j[key1]) == type({}):
                for key2 in f_j[key1]:
                    if type(f_j[key1][key2]) == type({}):
                        raise AssertionError, '''Cannot support 3rd json "%s" now''' % f_j[key1][key2]
                    elif type(f_j[key1][key2]) == type('') or type(f_j[key1][key2]) == type(u''):
                        j_dict['%s.%s' % (key1, key2)] = f_j[key1][key2]
                    else:
                        raise AssertionError, '''Key "%s" and Value "%s" is not as expect''' % (key2, f_j[key1][key2])
            elif  type(f_j[key1]) == type('') or  type(f_j[key1]) == type(u''):
                j_dict[key1] = f_j[key1]
            else:
                raise AssertionError, '''Key "%s" and Value "%s" is not as expect''' % (key1, f_j[key1])
    return j_dict


def _timeout(expression, timeout):
    # wait the expression's result change to true, break the loop
    start_time = time.time()
    end_time = start_time + float(timeout)
    while True:
        if expression:
            break
        if time.time() > end_time:
            raise AssertionError, '''Time out when wait condition expression'''
        time.sleep(1)

class HtmlHandler(FileHandler, object):
    PIC_TAG = ' pic:'
    _PIC_TAG = 'ppic:'
    
    def __init__(self, filename):
        FileHandler.__init__(self, filename, mode='w', encoding=None, delay=0)
        self.stream.write('''<html>
    <head>
        <title>WebUI Log</title>
        <script language="javascript">
            function SetPicWidth(obj) {
                iMaxWidth = 800;
                iMinWidth = 100;
                iPicWidth = obj.width;
                if (iPicWidth == iMinWidth) {
                    obj.width = iMaxWidth;
                } else {
                    obj.width = iMinWidth;
                }
            }
        </script>
        <style type="text/css">
            div.debug {background-color:rgb(215,208,183); padding: 5px;}
            div.info {background-color:rgb(149,245,123); padding: 5px;}
            div.warning {background-color:rgb(252,252,142); padding: 5px;}
            div.error {background-color:rgb(253,143,135); padding: 5px;}
        </style>
    </head>
<body>
''')
    def format(self, record):
        msg = escape(record.msg).strip()
        msg = msg.replace(self.PIC_TAG, self._PIC_TAG).replace(' ', '&nbsp').replace('\n', '<br>')
        if self._PIC_TAG in msg:
            desc = msg.split(self._PIC_TAG)[0].strip()
            pic = msg.split(self._PIC_TAG)[1].strip()
            msg = '%s<br><img src="%s" OnClick="SetPicWidth(this);" width="100"/><br>' % (desc, pic)
        else:
            msg = '%s<br>' % msg
        record.msg = msg
        fmt = super(HtmlHandler, self).format(record)
        fmt = '<div class="%s">%s</div>' % (record.levelname.lower(), fmt)
        return fmt
    
    def close(self):
        self.stream.write('</body>\n</html>')
        FileHandler.close(self)
