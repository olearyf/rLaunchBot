import schedule
import time
import tweepy
import requests
import json
import os
import datetime

# Define authentication keys
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Stores launch data per returned launch
class Launch:
    def __init__(self, name, date, infoURLs, pad):
        self.name = name
        self.date = date
        self.infoURLs = infoURLs
        self.pad = pad
        
# Determines if a launch is today or not
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
    
# Makes the string for an upcoming launch
def makeUpcomingLaunchString(launch):
    dateList = launch.date.split(' ')
    launchStr = launch.name + " on " + dateList[0] + " " + dateList[1] + " " + dateList[2]
    return launchStr

# Parses the API response and tweets launch information
def job():
    
    # Authenticate Twitter access
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create API object
    api = tweepy.API(auth)

    # Initiate and parse API call
    r = requests.get('https://launchlibrary.net/1.3/launch/next/5')
    if (r.status_code == requests.codes.ok):
        jsonParsed = json.loads(r.text)
        launches = []
        # Parse upcoming 5 launches
        for i in range(5):
            name = jsonParsed["launches"][i]["name"]
            date = jsonParsed["launches"][i]["windowstart"]
            infoURLs = jsonParsed["launches"][i]["infoURLs"]
            pad = jsonParsed["launches"][i]["location"]["pads"][0]["name"]
            launches.append(Launch(name, date, infoURLs, pad))
        launchesToday = []
        launchesFuture = []
        # Figure out which launches are today; which are in the future
        for launch in launches:
            if isToday(launch.date):
                launchesToday.append(launch)
            else:
                launchesFuture.append(launch)
        # If no launches, tweet thread of upcoming ones
        if (len(launchesToday) == 0):
            api.update_status("There are no launches scheduled for today! However, the following are coming up soon:")
            for launch in launchesFuture:
                tweets = api.user_timeline(screen_name="rLaunchBot", count=1)
                for tweet in tweets:
                    api.update_status("@rLaunchBot " + makeUpcomingLaunchString(launch), in_reply_to_status_id=tweet.id)
        # If launches today, tweet those and a thread of upcoming ones
        else:
            for launch in launchesToday:
                dateList = launch.date.split(' ')
                if (launch.infoURLs != None):
                    urls = ""
                    for URL in launch.infoURLs:
                        urls += " " + URL
                    api.update_status(launch.name + " is launching today at " + dateList[3] + " UTC! At " + launch.pad + ". For more information, visit " + urls)
                else:
                    api.update_status(launch.name + " is launching today at " + dateList[3] + " UTC! At " + launch.pad + ".")
            api.update_status("The following are coming up soon:")
            for launch in launchesFuture:
                tweets = api.user_timeline(screen_name="rLaunchBot", count=1)
                for tweet in tweets:
                    api.update_status("@rLaunchBot " + makeUpcomingLaunchString(launch), in_reply_to_status_id=tweet.id)
    else:
        print 'GET request failed!'
        
# Do this everyday at 3 AM EST
schedule.every().day.at("03:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)


