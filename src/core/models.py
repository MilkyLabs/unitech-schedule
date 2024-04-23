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
    
"""     @staticmethod
    def from_json(obj):
        result = LessonInfo()
        result.__dict__ = obj
        return result """

    
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

"""     @staticmethod
    def from_json(obj):
        result = DayTimeTable(obj['date'])
        result.__dict__ = obj
        result.lessons = []

        for lesson in obj['lessons']:
            result.lessons.append(LessonInfo.from_json(lesson))

        return result """

@dataclass
class WeekTimeTable(object):
    days: list[DayTimeTable]
    def __init__(self):
         self.days = []

    
    def to_json(self):
         return json.dumps(self,
            default=lambda o: o.__dict__,
            sort_keys=True)


"""   @staticmethod
    def from_json(obj):
        result = WeekTimeTable()

        for day in obj['days']:
            result.days.append(DayTimeTable.from_json(day))
        return result
 """
