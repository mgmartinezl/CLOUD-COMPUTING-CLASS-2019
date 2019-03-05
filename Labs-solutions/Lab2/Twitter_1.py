import os
import json
import tweepy
from tweepy import OAuthHandler

consumer_key = os.environ['CONSUMER-KEY']
consumer_secret = os.environ['CONSUMER-SECRET']
access_token = os.environ['ACCESS-TOKEN']
access_secret = os.environ['ACCESS-SECRET']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

user = api.me()

print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.followers_count))
print('Created: ' + str(user.created_at))
print('Description: ' + str(user.description))

