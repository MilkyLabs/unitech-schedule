from dataclasses import dataclass
import datetime

@dataclass
class LessonInfo:
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

    @staticmethod
    def create(table_rows):
            return LessonInfo(number=table_rows[0].text,
                        time=table_rows[1].text,
                        subject=table_rows[2].text, 
                        room=table_rows[3].text, 
                        teachers=list(filter(lambda el: str(el) != "<hr/>", table_rows[4].children)),
                        notices=table_rows[5].text)
    
@dataclass
class DaySchedule:
    date: datetime.date
    lessons: list[LessonInfo]

    def __init__(self, date: datetime.date):
        self.date = date
        self.lessons = []
