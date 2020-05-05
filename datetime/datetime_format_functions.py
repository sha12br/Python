

from datetime import date, time, datetime


# fromtimestamp()

timestamp = 1528797322 # hours and seconds representation
date_time = datetime.fromtimestamp(timestamp) # converts timestamp into datetime object

print(date_time)

# fromisoformat()
date_iso = date.fromisoformat("2020-01-31")

# >> datetime.date(2020, 1, 31)
# date.fromisoformat() to create a date instance for January 31, 2020 ;  based on ISO 8601 standard

# Other functions

today = date.today()
print(today)
# today = date.today()

now = datetime.now()
# datetime.datetime(2020, 1, 24, 14, 4, 57, 10015)

current_time = time(now.hour, now.minute, now.second)
cur_date_time = datetime.combine(today, current_time) #combines time and date together
# datetime.datetime(2020, 1, 24, 14, 4, 57)