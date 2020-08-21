"""
    Frances O'Leary, 8/14/2020

    This is a test to tweet a photo from the NASA APOD
    API along with a thread containing the explanation associated
    with it.
"""
import schedule
import time
import tweepy
import requests
import json
import os

# Define auth keys
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate Twitter access
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

class NASAImage:
    def __init__(self, date, explanation, hdurl, title):
        self.date = date
        self.explanation = explanation
        self.hdurl = hdurl
        self.title = title
        
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

def job():
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

            api.update_with_media(filename, testImage.title)
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
job()
