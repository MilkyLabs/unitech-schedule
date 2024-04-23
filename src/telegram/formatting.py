import logging
from aiogram import html
import dateutil
import re as regex
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

SUBJECT_EMOJI ={
    "[Мм]атем": "🤮"
}

def format_subject(subject: str) -> str:
    emoji = ""
    for key in SUBJECT_EMOJI.keys():
        r = regex.compile(key)
        if (r.match(subject)):
            emoji = SUBJECT_EMOJI[key]
            break
    return f"{subject} {emoji}" 


def format_day_time_table(time_table) -> str:
    logging.info(time_table['date'])
    weekday = DAYS[dateutil.parser.parse(time_table['date']).weekday()]
    message = f"🗓 Расписание на {html.bold(time_table['date'])} ({weekday})\n\n"

    for lesson in time_table['lessons']:
        message += f"🔘 {lesson['number']}-я пара {format_subject(lesson['subject'])} {html.italic(lesson['room'] + ' каб.')}\n"

    return message
