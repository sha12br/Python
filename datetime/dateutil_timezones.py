
from dateutil import tz 
# if dateutil is not installed ; install it as shown below
# python -m pip install python-dateutil
from datetime import datetime

#-----------------------------------------------------------------------------------------#
##### To view local timezone based on System time zone settings

now = datetime.now(tz=tz.tzlocal())
print(now)
# >> datetime.datetime(2020, 5, 5, 13, 57, 8, 289602, tzinfo=tzlocal())

print("Local Time Zone is : " str(now.tzname()))
# >> Local Time Zone is : India Standard Time  --> this could differ based on your time zones settings
#	NOTE: The timezone would be differ from windows to Linux , where EST would be printed in Linux  instead of Easter Standard time

#-----------------------------------------------------------------------------------------#

### Getting Time Zones for Various Cities around the world

american_vancouver_tz = tz.gettz("America/Vancouver")
# You could get different time zones names from IANA using the below link
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

now = datetime.now(tz=american_vancouver_tz)
print(now)

print("American Vancouver Time Zone is : " str(now.tzname()))
# >> this would psosibly return PDT i belive, but you are free to try it out yourself

# You could also use general UTC zone
#i.e. datetime.now(tz=tz.UTC)

#-----------------------------------------------------------------------------------------#