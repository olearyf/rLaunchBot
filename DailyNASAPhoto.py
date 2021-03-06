"""
    Frances O'Leary, 8/14/2020

    This is a Python script I keep running in the background on
    a raspberry pi to power by TwitterBot @rLaunchBot. This script
    takes care of tweeting the APOD from NASA. Everyday at 1 PM
    EST this script will get the Astronomy Picture of the Day
    and tweet it along with a thread containing the explanation
    provided by NASA.
    
    Update 8/16/2020 - some incoming images exceed the max file size Tweepy can tweet!
    (3072 kb) As a result, Pillow is now imported to adjust the size
    of an image if it is too big to be tweeted.
"""
import schedule
import time
import tweepy
import requests
import json
import os
from PIL import Image

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
    explanationLength = len(explanation)
    if explanationLength < 262:
        return explanation
    chunks = []
    while 1:
        testChunk = explanation[:262]
        if (len(testChunk) == 262):
            lastWordIndex = testChunk.rfind(' ')
            chunks.append(explanation[:lastWordIndex])
            explanation = explanation[lastWordIndex:]
        else:
            chunks.append(testChunk)
            break

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
            # If image is larger than acceptable size, resize
            if ((os.path.getsize(filename) / 1000) >= 3072):
                newImage = Image.open(filename)
                size = newImage.size
                width = size[0]
                height = size[1]
                # Right now just approximate. Will use fancier math later.
                newImage = newImage.resize((width - 200, height - 200))
                newImage.save(filename)
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

