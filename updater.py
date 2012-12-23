import time
import json

import lxml.html 
import urllib.request

from supergraph import get_cur_dict

def update():
    now_time = time.time()

    supersite = urllib.request.urlopen('http://supersupersupersuper.com')
    html = lxml.html.document_fromstring(supersite.read())

    supernum_elem = html.find_class('supernumber')[0] 
    supernum = int(supernum_elem.text_content())

    json_dict = get_cur_dict()

    json_dict[now_time] = supernum

    with open('super.json', 'w') as f:
        json.dump(json_dict, f)
