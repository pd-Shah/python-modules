import datetime
import time
import calendar

#today:
datetime.datetime.today()

#now:
now=datetime.datetime.fromtimestamp(time.time())
#year, month, day, hour:
now.year, now.month, now.day, now.hour, now.minute, now.second

#my_calendar
my_calendar=calendar.TextCalendar(calendar.SATURDAY)
print(my_calendar.formatmonth(now.year, now.month))
print(now.year, now.month, now.day)

#HTML_calendar
my_calendar = calendar.HTMLCalendar(calendar.SATURDAY)
print(my_calendar.formatmonth(now.year, now.month))

#time delta
today=datetime.date(now.year,now.month,now.day)
yesterday=datetime.date(now.year,now.month,now.day-1)

time_delta=today-yesterday
print(time_delta, time_delta.days, time_delta.total_seconds())
