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
    "[.]*[Мм]атем[.]*": "🤮",
    "[.]*[Фф]изич[.]*": "👩‍🦽",
    "Архитектура вычислительных систем": "🧮",
    "[.]*[Пп]рогр[.]*": "👨‍💻", # TODO: fix, currently not working regex
    ".": "🔺",
}

SUBJECT_ABBREVIATION = {
    "Математический анализ": "Мат. анализ",
    "Основы алгоритмизации и программирования": "ОАиП",
    "Архитектура вычислительных систем": "Архитектура ВС",
    "Физическая культура": "Физ-ра",
}
SUBJECT_FORM_ABBREVIATION = {
    "Практическое занятие": "практика",
    "Практическое занятие(Д)": "практика дистант",
    "Лекция": "лекция",
    "Лекция(Д)": "лекция дистант",
}

def format_subject(subject: str) -> str:
    emoji = ""
    # logging.info(subject)
    for key in SUBJECT_EMOJI.keys():
        # logging.info(f"Key and emoji {key}")
        r = regex.compile(key)
        if (r.match(subject)):
            emoji = SUBJECT_EMOJI[key]
            # logging.info(f"Key and emoji {key}, {emoji}")
            break
    
    split_subject = subject.split(" - ")
    subject = split_subject[0]
    form = split_subject[1]

    subject = SUBJECT_ABBREVIATION[subject] if SUBJECT_ABBREVIATION.get(subject) else subject
    form = SUBJECT_FORM_ABBREVIATION[form] if SUBJECT_FORM_ABBREVIATION.get(form) else form

    return f"{html.bold(subject)} {emoji} - {html.underline(form)}" 

def format_room(room: str) -> str:

    if ("Дистанционная" in room):
        return ""

    return f"{html.italic(' - ' + room + ' каб.')}"

def format_lesson(lesson) -> str:
    formatted = f"◦ {lesson['number']}-я пара {format_subject(lesson['subject'])} {format_room(lesson['room'])}\n"
    # logging.info(formatted)
    return formatted


def format_day_time_table(time_table) -> str:
    weekday = DAYS[dateutil.parser.parse(time_table['date']).weekday()]
    message = f"🗓 Расписание на {html.bold(time_table['date'])} ({weekday})\n\n"

    for lesson in time_table['lessons']:
        message += format_lesson(lesson)

    return message

