#!/usr/bin/env python3

#by Josh brown
#Wednesday Afternoon lab

#Given Dictionary
cisco_ios = {'device_type': 'cisco_ios_ssh', 'ip': '10.10.10.27', 'username': 'admin', 'password': 'passwd', 'port': 22}

#for loop printing "cisco login info -" for each dictionary VALUE

for x in cisco_ios.values():
   print('CISCO LOGIN INFO - ' + str(x)) 
   #Dont forget to wrap varialbes in "str()" to catch rogue dictionary inputs

#nice work mang :)