import logging
from bs4 import BeautifulSoup
from requests import Session
from datetime import date
from core.models import WeekTimeTable
from dataclasses import dataclass
import datetime
import json

@dataclass
class LessonInfo(object):
    number: int
    time: str
    subject: str
    room: str
    teachers: list[str]
    notices: str


    def __init__(self, number: str, time: str, subject: str, room: str, teachers: list[str], notices: str):
        self.number = int(number)
        self.time = time
        self.subject = subject
        self.room = room
        self.teachers = teachers
        self.notices = notices


    def to_json(self):
        return json.dumps(self,
            default=lambda o: o.__dict__,
            sort_keys=True)
        

    @staticmethod
    def create(table_rows):
            return LessonInfo(number=table_rows[0].text,
                        time=table_rows[1].text,
                        subject=table_rows[2].text, 
                        room=table_rows[3].text, 
                        teachers=list(filter(lambda el: str(el) != "<hr/>", table_rows[4].children)),
                        notices=table_rows[5].text)
    
@dataclass
class DayTimeTable(object):
    date: str
    lessons: list[LessonInfo]


    def to_json(self):
        return json.dumps(self,
            default=lambda o: o.__dict__,
            sort_keys=True)
    

    def __init__(self, date: datetime.date):
        self.date = str(date)
        self.lessons = []

@dataclass
class WeekTimeTable(object):
    days: list[DayTimeTable]
    def __init__(self):
         self.days = []

    
    def to_json(self):
         return json.dumps(self,
            default=lambda o: o.__dict__,
            sort_keys=True)


def get_week_start() -> date:
    today = date.today()
    return date(today.year, 
                         today.month, 
                         today.day - today.weekday())

def parse(url: str):
    with Session() as session:
        response = session.get(url)

        if response.status_code != 200:
            logging.error(f"Status code {response.status_code} from url {url}")
            return {}

        result = WeekTimeTable()

        soup = BeautifulSoup(response.text, 'html.parser')
        
        current_date = get_week_start()

        tables = soup.find_all('table')
        for t in tables:
            day_time_table = DayTimeTable(current_date)
            current_date = date(current_date.year, current_date.month, current_date.day + 1)

            table_body = t.find('tbody')
            rows = table_body.find_all('tr')
            
            for r in rows:
                columns = r.find_all('td')
                if (columns[2].text != ""):
                    day_time_table.lessons.append(LessonInfo.create(columns))
            result.days.append(day_time_table)
        
        return result
