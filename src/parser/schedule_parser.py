from core.models import DaySchedule, LessonInfo
from bs4 import BeautifulSoup
from sys import stderr
import datetime
from requests import Session

URL = "https://ies.unitech-mo.ru/schedule_list_groups?g=1801"

def get_week_start() -> datetime.date:
    today = datetime.date.today()
    return datetime.date(today.year, 
                         today.month, 
                         today.day - today.weekday())

def parse_schedule():

    # Отправляем POST-запрос для авторизации
    with Session() as session:
        response = session.get(URL)

        # Проверяем успешность авторизации
        if response.status_code != 200:
            print("Status code:", response.status_code, file=stderr)
            yield 

        soup = BeautifulSoup(response.text, 'html.parser')
        
        current_date = get_week_start()

        tables = soup.find_all('table')
        for t in tables:
            day_schedule = DaySchedule(current_date)
            current_date = datetime.date(current_date.year, current_date.month, current_date.day + 1)

            table_body = t.find('tbody')
            rows = table_body.find_all('tr')
            
            for r in rows:
                columns = r.find_all('td')
                if (columns[2].text != ""):
                    day_schedule.lessons.append(LessonInfo.create(columns))
            
            yield day_schedule
