import json
import os
import parser.groups
from datetime import datetime
from pathlib import Path
from parser.parser import parse_time_table_html


TIMETABLE_CACHE_FILE    = ".cache/timetable.json"
GROUPS_CACHE_FILE       = ".cache/groups.json"
URL                     = "https://ies.unitech-mo.ru/schedule_list_groups?g=1801"


def is_cached() -> bool:
    return Path(TIMETABLE_CACHE_FILE).exists() \
        and datetime.fromtimestamp(os.path.getmtime(TIMETABLE_CACHE_FILE)).hour == datetime.today().hour \
        and Path(GROUPS_CACHE_FILE).exists() \
        and datetime.fromtimestamp(os.path.getmtime(GROUPS_CACHE_FILE)).day == datetime.today().day

def make_groups_cache(groups):
    Path(GROUPS_CACHE_FILE).write_text(json.dumps(groups))

def make_timetables_cache(timetables):
    Path(TIMETABLE_CACHE_FILE).write_text(json.dumps(timetables))

def make_cache():
    cache_parent = Path(TIMETABLE_CACHE_FILE).parent 
    if (not cache_parent.exists()):
        os.mkdir(cache_parent.name)
    
    groups = parser.groups.parse()
    
    timetables = []
    for group in groups:
        timetables.append(parse_time_table_html(group.link))

    make_groups_cache(groups)
    make_timetables_cache(timetables)
    

    
