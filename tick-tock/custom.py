#!/usr/bin/env python3

import time
import datetime


bday = datetime.datetime(1990,1,5,23,59,59) # my bday import intp pythonese
ctsecs = int(time.time()) #epoch time in secs
#print(ctsecs)
bdtsecs = time.mktime(bday.timetuple()) # import the user date into seconds
#print(bdtsecs)
#tdelta = #epoch time in secs minus mybday in secs
tdelta = ctsecs - bdtsecs #turn human time into second
#print(tdelta)

#convert tdelta from secs to days

tdeltasec = int(tdelta) / int((60*60*24))
print(str(round(tdeltasec)) + ' days since my birthday')
