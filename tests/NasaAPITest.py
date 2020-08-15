"""
    Frances O'Leary, 8/14/2020

    This is a test to get the APOD from the NASA
    APOD API. It prints out the response from the API,
    parsed into a Python dictionary.
"""
import requests
import json

class NASAImage:
    def __init__(self, date, explanation, hdurl, title):
        self.date = date
        self.explanation = explanation
        self.hdurl = hdurl
        self.title = title

r = requests.get('https://api.nasa.gov/planetary/apod?api_key=YOUR_KEY')
if (r.status_code == requests.codes.ok):
    json = json.loads(r.text)
    testImage = NASAImage(json["date"], json["explanation"], json["hdurl"], json["title"])
    print testImage.date
    print testImage.explanation
    print testImage.hdurl
    print testImage.title
else:
    print 'GET request failed!'
