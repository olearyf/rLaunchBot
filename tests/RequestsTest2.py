"""
    Frances O'Leary, 8/14/2020

    This is a test to get data back from the LaunchLibrary API.
    But it now takes the parsed responses and determines if it
    is in the future or happening today.
"""
import requests
import json
import datetime

class Launch:
    def __init__(self, name, date, infoURLs, pad):
        self.name = name
        self.date = date
        self.infoURLs = infoURLs
        self.pad = pad

def isToday(date):
    launchDateList = date.split(' ')
    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
        ]
    count = 1
    for month in months:
        if (month == launchDateList[0]):
            break
        count += 1
    launchTime = datetime.datetime(int(launchDateList[2]), count, int(launchDateList[1][:-1]))
    now = datetime.datetime.now()
    if (now.year == launchTime.year):
        if (now.month == launchTime.month):
            if (now.day == launchTime.day):
                return True
    return False

r = requests.get('https://launchlibrary.net/1.3/launch/next/5')
if (r.status_code == requests.codes.ok):
    json = json.loads(r.text)
    launches = []
    for i in range(5):
        name = json["launches"][i]["name"]
        date = json["launches"][i]["windowstart"]
        infoURLs = json["launches"][i]["infoURLs"]
        pad = json["launches"][i]["location"]["pads"][0]["name"]
        launches.append(Launch(name, date, infoURLs, pad))
    launchesToday = []
    launchesFuture = []
    for launch in launches:
        if isToday(launch.date):
            print 'today'
            launchesToday.append(launch)
        else:
            print 'not today'
            launchesFuture.append(launch)
else:
    print 'GET request failed!'
