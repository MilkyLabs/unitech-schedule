from datetime import date
from bs4 import BeautifulSoup
from requests import Session

from core.models import DayTimeTable, LessonInfo, WeekTimeTable


def get_week_start() -> date:
    today = date.today()
    return date(today.year, 
                         today.month, 
                         today.day - today.weekday())


def parse_time_table_html(url: str) -> WeekTimeTable:

    with Session() as session:
        response = session.get(url)

        if response.status_code != 200:
            print("Status code:", response.status_code, file=stderr)
            return

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
