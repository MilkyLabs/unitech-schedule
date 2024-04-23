#!/usr/bin/env python

import schedule_parser
from args import Args
import datetime

def print_day_schedule(schedule):
    print("Расписание на", schedule.date)
    for lesson in schedule.lessons:
        print()
        print(f"{lesson.number}-я пара ({lesson.time})")
        print(lesson.subject)
        print("Кабинет", lesson.room)
        print(lesson.teachers)
        if (lesson.notices != ""):
            print("", lesson.notices)


def main():
    schedule = schedule_parser.parse_schedule()
    args = Args()

    if (args.flag("--today")):
        day_schedule = list(schedule)[datetime.date.today().weekday()]
        if (args.flag("--pretty")):
            print(day_schedule)
        else:
            print(day_schedule)
        return
    

    if (args.flag("--pretty")):
        for i in schedule:
            print_day_schedule(i)
            print()
    else:
        print(list(schedule))

if __name__ == "__main__":
    main()
