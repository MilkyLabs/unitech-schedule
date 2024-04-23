#!/usr/bin/env python

from core.models import DayTimeTable
import parser.time_table as time_table
from cli.args import Args
import datetime

def print_day_schedule(time_table: DayTimeTable):
    print(time_table)
    print("Расписание на", time_table['date'])
    for lesson in time_table['lessons']:
        print()
        print(f"{lesson['number']}-я пара ({lesson['time']})")
        print(lesson['subject'])
        print("Кабинет", lesson['room'])
        print(lesson['teachers'])
        if (lesson['notices'] != ""):
            print("", lesson['notices'])


def main():
    table = time_table.get_time_table()
    args = Args()

    if (args.flag("--today")):
        day_time_table = table['days'][datetime.date.today().weekday()]
        if (args.flag("--pretty")):
            print_day_schedule(day_time_table)
        else:
            print(day_time_table)
        return
    

    if (args.flag("--pretty")):
        for i in table['days']:
            print_day_schedule(i)
            print()
    else:
        print(table)

if __name__ == "__main__":
    main()
