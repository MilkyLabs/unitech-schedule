import json
import logging
import os
import parser.groups
import parser.timetable
from datetime import datetime
from pathlib import Path


__TIMETABLE_CACHE_FILE    = ".cache/timetable.json"
__GROUPS_CACHE_FILE       = ".cache/groups.json"
__URL                     = "https://ies.unitech-mo.ru/schedule_list_groups?g=1801"

def get_groups_file() -> Path:
    return Path(__GROUPS_CACHE_FILE)


def get_timetable_file() -> Path:
    return Path(__TIMETABLE_CACHE_FILE)


def __is_cached() -> bool:
    return Path(__TIMETABLE_CACHE_FILE).exists() \
        and datetime.fromtimestamp(os.path.getmtime(__TIMETABLE_CACHE_FILE)).hour == datetime.today().hour \
        and Path(__GROUPS_CACHE_FILE).exists() 


def __make_groups_cache(groups):
    Path(__GROUPS_CACHE_FILE).write_text(json.dumps(groups))

def __make_timetables_cache(timetables):
    Path(__TIMETABLE_CACHE_FILE).write_text(json.dumps(timetables))

def __make_cache():
    log = logging.getLogger()
    
    log.info("Start making cache")
    cache_parent = Path(__TIMETABLE_CACHE_FILE).parent 
    if (not cache_parent.exists()):
        log.info("Creating cache folder")
        os.mkdir(cache_parent.name)
    
    groups = parser.groups.parse()

    log.info(f"End parsing groups, total: {len(groups)}")
    
    
    timetables = {}
    for group in groups:
        timetables[group.name] = parser.timetable.parse(group.link)

    __make_groups_cache(groups)
    __make_timetables_cache(timetables)


def ensure_cached():
    if (not __is_cached()):
        __make_cache()
