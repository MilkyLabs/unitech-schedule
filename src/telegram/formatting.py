import logging
from aiogram import html
import dateutil
from datetime import date

import dateutil.parser

DAYS = {
    0: "Пн",
    1: "Вт",
    2: "Ср",
    3: "Чт",
    4: "Пт",
    5: "Сб",
    6: "Вс",
}

def format_day_time_table(time_table) -> str:
    logging.info(time_table['date'])
    weekday = DAYS[dateutil.parser.parse(time_table['date']).weekday()]
    message = f"Расписание на {html.bold(time_table['date'])} ({weekday})\n\n"

    for lesson in time_table['lessons']:
        message += f"* {lesson['number']}-я пара {lesson['subject']} {html.italic(lesson['room'] + ' каб.')}\n"

    return message
