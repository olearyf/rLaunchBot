"""
    Frances O'Leary, 8/14/2020

    This is a Python script I keep running in the background on
    a raspberry pi to power by TwitterBot @rLaunchBot. This script
    takes care of tweeting the APOD from NASA. Everyday at 1 PM
    EST this script will get the Astronomy Picture of the Day
    and tweet it along with a thread containing the explanation
    provided by NASA.
"""
import schedule
import time
import tweepy
import requests
import json
import os

# Define authentication keys
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Stores NASA image data from API call
class NASAImage:
    def __init__(self, date, explanation, hdurl, title):
        self.date = date
        self.explanation = explanation
        self.hdurl = hdurl
        self.title = title

# Parses explanation text into size that Twitter can handle
def parseExplanation(explanation):
    n = 262
    chunks = [explanation[i:i+n] for i in range(0, len(explanation), n)]
    return chunks

# Tweets the image and explanation thread
def job():
    # Authenticate Twitter access
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create API object
    api = tweepy.API(auth)

    # Initiate and parse API call
    r = requests.get('https://api.nasa.gov/planetary/apod?api_key=YOUR_KEY')
    if (r.status_code == requests.codes.ok):
        jsonParsed = json.loads(r.text)
        testImage = NASAImage(jsonParsed["date"], jsonParsed["explanation"], jsonParsed["hdurl"], jsonParsed["title"])
        filename = 'temp.jpg'
        request = requests.get(testImage.hdurl, stream=True)
        if request.status_code == 200:
            with open(filename, 'wb') as image:
                for chunk in request:
                    image.write(chunk)
            api.update_with_media(filename, "APOD for " + testImage.date + ": " + testImage.title)
            os.remove(filename)
            chunks = parseExplanation(testImage.explanation)
            for chunk in chunks:
                tweets = api.user_timeline(screen_name="rLaunchBot", count=1)
                for tweet in tweets:
                    api.update_status("@rLaunchBot " + chunk, in_reply_to_status_id=tweet.id)
        else:
            print("Unable to download image")
    else:
        print 'GET request failed!'

# Do this everyday at 1 PM EST
schedule.every().day.at("13:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)

