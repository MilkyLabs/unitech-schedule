import json
from typing import Generator
from core.models import WeekTimeTable, DayTimeTable, LessonInfo
from bs4 import BeautifulSoup
from sys import stderr
import pathlib
import datetime
from requests import Session

from parser.cache import *


def get_time_table() -> WeekTimeTable:
    if (not is_cached()):
        make_cache()

    return json.loads(pathlib.Path(CACHE_FILE).read_text())

