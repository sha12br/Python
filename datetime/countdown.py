
from datetime import datetime # import datetime function from datetime package

""" The below example is static and
could be made dynamic by importing sys package
and receiving arguments from runtime using sys.argv[]
"""

event_date = datetime(year=2020,month=8,day=11,hour=0)
countdown = event_date - datetime.now()

print("Countdown days for the Event: " +str(countdown)) #format would be of : day days, HH:MM:SS --> i.e: 97 days, 10:30:24


#-----------------------------------------------------------------------------------------#

# Improving countdown script using dateutil module

from dateutil import parser, tz

event_date = parser.parse("August 8, 2020 12:00 AM") 
# parser.parse literally creates a datetime object from string literals as shown above
# you could get much of an interface while creating a datetime 

event_date = event_date.replace(tzinfo=tz.gettz("America/New_York")) # you could have any TZ specified based on your TZ
now = datetime.now(tz=tz.tzlocal()) # Replacing the current TZ based on  local TZ

countdown = event_date - now
print("Countdown days for the Event: " +str(countdown))

#-----------------------------------------------------------------------------------------#