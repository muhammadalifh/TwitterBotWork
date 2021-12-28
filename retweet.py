# import dependencies
import tweepy
import os
from dotenv import load_dotenv
from tweepy.streaming import StreamListener
from streamlistener import StreamListener

load_dotenv()

# import and assign our environment variables
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')

# initiate oauth handler and set access token
twitter_auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
twitter_auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# initiate tweepy api object using the authentication handler object
twitter_api = tweepy.API(twitter_auth)

try:
    if twitter_api.verify_credentials():
        print("Successfully logged in")
    else:
        print("login failed")

except tweepy.TweepError as e:
    print(e)

except Exception as e:
    print(e)

# initiate a StreamListener object
tweets_listener = StreamListener(twitter_api)

# initiate a tweepy.Stream object
tweet_stream = tweepy.Stream(twitter_api.auth, tweets_listener)

# use the filter method
tweet_stream.filter(track=["#100DaysofCode", "#ProgrammingLife", "#javascript", "#nodejs", "#pythondeveloper", "#javaprogramming"],
languages=["en"])