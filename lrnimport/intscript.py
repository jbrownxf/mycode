#!/usr/bin/env python3
from subprocess import call

call(['ip', 'link', 'show', 'up'])
print ('THis program will check you interfaces')
interface = input('enter an interface, like ens3: ')
call(['ip', 'addr', 'show', 'dev', interface])
call(['ip', 'route', 'show', 'dev', interface])