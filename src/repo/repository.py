from datetime import date as Date
from json import loads as parse_json
import parser.cache

class Repository:
    def __init__(self):
        parser.cache.ensure_cached()

    def get_groups(self):
        return parse_json(parser.cache.get_groups_file().read_text())
    
    def get_timetable(self, group: str):
        return parse_json(parser.cache.get_timetable_file().read_text)[group]
    
    def get_day_timetable(self, group: str, day: Date):
        ...
        # TODO
    def get_week_timetable(self, group: str, week_day: Date):
        ...
        # TODO
