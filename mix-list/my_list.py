#!/usr/bin/env python3
# This script is to learn how to manipulate lists
my_list = ['192.168.0.5', 5060, 'UP']
print( "THe first item in teh list (IP): " + my_list[0] )
print( "The second item in teh list (state): " + my_list[2] )
new_list = [ 5060, '80', 55, '10.0.0.1', '10.20.30.1', 'ssh' ]

#my code to use a single print() to print all data from new_list

print( 'Ip addresses ' + new_list[3] + " " + new_list[4] + ' availalbe for ' + new_list[5] + ' at ports ' + new_list[0-2] )