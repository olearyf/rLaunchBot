"""
    Frances O'Leary, 8/14/2020

    This is a test to tweet a photo with a local path.
"""
import tweepy

# Define authentication keys
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate Twitter access
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Create and publish tweet
api.update_with_media("path/to/photo.jpeg", "Test tweet with an image!")
