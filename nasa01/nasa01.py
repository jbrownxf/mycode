#!/usr/bin/env python3
import urllib.request
import json
import webbrowser

## Define APOD
apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=JTYmRrqwk6OQF7pEpXOHr1IVyQtvWCWVARoZ0bgw'    ## your key goes in place of DEMO_KEY
dtinpt = input('What date (YYYY-MM-DD) would you like to see? ')

#New call the websirvice
apodurlobj = urllib.request.urlopen(apodurl + 'date=' + dtinpt + '&' + mykey)

## Call the webservice
#apodurlobj = urllib.request.urlopen(apodurl + mykey)

## read the file-like object
apodread = apodurlobj.read()

## decode json to python data structure
decodeapod = json.loads(apodread.decode('utf-8'))

## display our pythonic data
print("\n\nConverted python data")
print(decodeapod['explanation']['date']['title'])

## use firefox to open the HTTPS URL
input('\nPress Enter to open NASA Picture of the Day in Firefox')
webbrowser.open(decodeapod['url'])
