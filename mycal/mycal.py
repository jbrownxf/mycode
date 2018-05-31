#!/usr/bin/python
import calendar
yr = input('What year is it? ')
lilcal = calendar.calendar(yr)

print("Here is a tiny calendar:")
print(lilcal)
if calendar.isleap(yr) == False:
   print('This is not a leap year')
else:
    print('This year is a leap year')
