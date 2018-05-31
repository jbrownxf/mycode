#!/usr/bin/env python3

import time
import datetime


bday = datetime.datetime(1990,1,5,23,59,59) # my bday import intp pythonese
ctsecs = int(time.time()) #epoch time in secs
#print(ctsecs)
bdtsecs = time.mktime(bday.timetuple()) # import the user date into seconds
#print(bdtsecs)
#tdelta = #epoch time in secs minus mybday in secs
tdelta = ctsecs - bdtsecs
print(tdelta)

#convert tdelta from secs to days
tdeltadays = int(tdelta) / int((60*60*24))
print(str(round(tdeltadays)) + ' days since my birthday')

#Shows the curretn time plus 500 seconds
f5sec = datetime.datetime.now() + datetime.timedelta(seconds=500)
print(f5sec)
print(time.mktime(f5sec.timetuple()))
#Shows the curretn time plus 500 days
f5day = datetime.datetime.now() + datetime.timedelta(days=500)
print(f5day)
print(time.mktime(f5day.timetuple()))
