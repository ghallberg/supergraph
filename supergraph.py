import time
import json

def get_cur_dict():
    try:
        with open('super.json', 'r') as f:
                return json.load(f)
    except:
        return {}

def build_json():
    json_dict = get_cur_dict()

    wanted_times = [time.gmtime(time.time() - x*3600) for x in range(0,24)]
    max_supers = [get_hour_max(json_dict, x) for x in wanted_times]
    max_supers.reverse()
    lines = ''
    for line_num in range(max(max_supers), 0, -1):
        line = ''
        for supers in max_supers:
            if supers >= line_num:
                line = line+' # '
            else:
                line = line+'   '
        lines = lines + '\n'+str(line_num).zfill(2) +  line

    line = ''
    for i in range(24,0, -1):
        line = line + str(i).zfill(2) + ' '
    lines = lines + '\n  ' + line
    lines = lines + '\n' +'hours ago'

    return lines

def _match_hour(t1, t2):
    return _match_yday(t1, t2) and t1.tm_hour == t2.tm_hour

def _match_yday(t1, t2):
    return _match_year(t1, t2) and t1.tm_yday == t2.tm_yday

def _match_year(t1, t2):
    return  t1.tm_year == t2.tm_year

def get_hour_max(dict, hour):
    hour_keys = filter(lambda data_time: _match_hour(time.gmtime(float(data_time)),
        hour), dict.keys())
    try:
       max_val =  max([dict[x] for x in hour_keys])
    except:
        max_val = -1
    return max_val


update()

#output = build_page()

#with open('index.html', 'w') as f:
#    f.write ('<html><body><div id="graph">'+output+'</div></body></div>')
