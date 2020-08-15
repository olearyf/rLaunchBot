"""
    Frances O'Leary, 8/14/2020

    This is a test to get data back from the LaunchLibrary API.
    It parses the response and puts relevant information into a
    Python dictionary called Launch. The API call used returns the upcoming 5 launches.
    This script prints out the first one.
"""
import requests
import json

class Launch:
    def __init__(self, name, date, infoURLs, pad):
        self.name = name
        self.date = date
        self.infoURLs = infoURLs
        self.pad = pad

r = requests.get('https://launchlibrary.net/1.3/launch/next/5')
if (r.status_code == requests.codes.ok):
    json = json.loads(r.text)
    name = json["launches"][0]["name"]
    date = json["launches"][0]["windowstart"]
    infoURLs = json["launches"][0]["infoURLs"]
    pad = json["launches"][0]["location"]["pads"][0]["name"]
    testLaunch = Launch(name, date, infoURLs, pad)
    print testLaunch.name
    print testLaunch.date
    print testLaunch.infoURLs
    print testLaunch.pad
else:
    print 'GET request failed!'