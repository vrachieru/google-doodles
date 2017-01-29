import datetime
import requests
import json
import tweepy

base_url = "http://www.google.com/doodles"

def twitter(config):
    auth = tweepy.OAuthHandler(config.get('consumerKey'), config.get('consumerSecret'))
    auth.set_access_token(config.get('accessToken'), config.get('accessTokenSecret'))
    return tweepy.API(auth)

def doodles():
    response = requests.get('%s/json/%s/%s' % (base_url, today.year, today.month))
    return json.loads(response.content)

today = datetime.date.today()
config = json.loads(open('config.json').read())
twitter = twitter(config)

for doodle in doodles():
    if doodle['run_date_array'] == [today.year, today.month, today.day]:
        tweet = '%s\n%s/%s' % (doodle['share_text'], base_url, doodle['name'])
        twitter.update_status(tweet.encode('utf-8'))
