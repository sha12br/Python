

from datetime import datetime, timedelta


now = datetime.now()
# datetime.datetime(2020, 1, 26, 9, 37, 46, 380905)

tomorrow = timedelta(days=+1) # timedelta is used to perform some operations on datetime object's
next_day = now + tomorrow  # datetime.datetime(2020, 1, 27, 9, 37, 46, 380905)
print(next_day)

yesterday = timedelta(days=-1)
prev_day = now + tomorrow  # datetime.datetime(2020, 1, 25, 9, 37, 46, 380905)
print(prev_day)

delta = timedelta(days=+3, hours=-4)
change_delta_time = now + delta
# datetime.datetime(2020, 1, 29, 5, 37, 46, 380905)


from dateutil.relativedelta import relativedelta
# relativedelta is very similar to timedelta ; produce changes of any number of years, months, days, hours, seconds, or microseconds

tomorrow = relativedelta(days=+1)
nextday = now + tomorrow # datetime.datetime(2020, 1, 27, 9, 37, 46, 380905)

# you use relativedelta instead of timedelta to find the datetime corresponding to tomorrow. 
# Now you can try adding five years, one month, and three days to now while subtracting four hours and thirty minutes

delta = relativedelta(years=+5, months=+1, days=+3, hours=-4, minutes=-30)
delta_change = now + delta
# datetime.datetime(2025, 3, 1, 5, 7, 46, 380905)