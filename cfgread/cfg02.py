#!/usr/bin/env python3
## create file object in "r"ead mode
configfile = open('vlanconfig.cfg', 'r')


## display file to the screen - .read()
configblog = configfile.read()

print("Here is a blob \n" + configblog)

## break configblog across line boundaries (strips out \n)
configlist = configblog.splitlines()

## display list with no '\n'
print(configlist)



#readlines to determine number of lines in file
print(len(configlist))


## Always close your file
configfile.close()