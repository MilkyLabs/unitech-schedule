from datetime import date as Date, timedelta as TimeDelta

def get_week_start(day: Date) -> Date:
    return day - TimeDelta(days=day.weekday())
