import tweepy
from textblob import textblob

consumer_key = ''
consumer_secret = ''

access_token = '' 
access_token_secret = ''

auth = tweepy.0AuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('League of Legends')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
