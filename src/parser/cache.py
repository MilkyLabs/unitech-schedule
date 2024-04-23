import json
import os
from datetime import datetime
from pathlib import Path
from parser.parser import parse_time_table_html


CACHE_FILE  = ".cache/schedule.json"
URL         = "https://ies.unitech-mo.ru/schedule_list_groups?g=1801"


def is_cached() -> bool:
    return Path(CACHE_FILE).exists() and datetime.fromtimestamp(os.path.getmtime(CACHE_FILE)).hour == datetime.today().hour


def make_cache():
    time_table = parse_time_table_html(URL)
    cache_parent = Path(CACHE_FILE).parent 
    if (not cache_parent.exists()):
        os.mkdir(cache_parent.name)
    
    Path(CACHE_FILE).write_text(time_table.to_json())

    
