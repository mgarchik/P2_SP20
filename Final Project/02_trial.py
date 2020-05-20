import tweepy
import json

consumer_key = 'LGagr7jJ6io6RyWZvwt9Tc38R'
consumer_secret = 'rvVxEb1suQrm2m53CEaPUsGtKshwgn6a4OKJmiMzBfzHj569Y7'

with open('/Users/garch/Downloads/access_token.txt', 'r', encoding="utf-8") as f:
    access_token = f.read()
with open('/Users/garch/Downloads/access_secret.txt', 'r', encoding="utf-8") as f2:
    access_secret = f2.read()

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
public_tweets = api.home_timeline()

status = public_tweets[0]

#convert to string
json_str = json.dumps(status._json)

#deserialise string into python object
parsed = json.loads(json_str)

print(json.dumps(parsed, indent=4, sort_keys=True))

