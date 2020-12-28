from dotenv import load_dotenv
import os
import tweepy

load_dotenv()

# # # # Auth tokens for Twitter bot 1 # # # #

TS_ACCESS_TOKEN = os.getenv('TS_ACCESS_TOKEN')
TS_ACCESS_TOKEN_SECRET = os.getenv('TS_ACCESS_TOKEN_SECRET')
TS_API_KEY = os.getenv('TS_API_KEY')
TS_API_SECRET = os.getenv('TS_API_SECRET')

# # # # Auth Tokens for Twitter bot 2 # # # #

MB_ACCESS_TOKEN = os.getenv('MB_ACCESS_TOKEN')
MB_ACCESS_TOKEN_SECRET = os.getenv('MB_ACCESS_TOKEN_SECRET')
MB_API_KEY = os.getenv('MB_API_KEY')
MB_API_SECRET = os.getenv('MB_API_SECRET')

# # # # Auth for Twitter bot 1 # # # #

def TSTwitterAuth(TS_ACCESS_TOKEN, TS_ACCESS_TOKEN_SECRET, TS_API_KEY, TS_API_SECRET):
    auth = tweepy.OAuthHandler(TS_API_KEY, TS_API_SECRET)
    auth.set_access_token(TS_ACCESS_TOKEN, TS_ACCESS_TOKEN_SECRET)

    # Connect Tweepy to API

    api = tweepy.API(
        auth,
        wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)

    return api

# # # # Auth for Twitter bot 2 # # # #

def MBTwitterAuth(MB_ACCESS_TOKEN, MB_ACCESS_TOKEN_SECRET, MB_API_KEY, MB_API_SECRET):

    auth = tweepy.OAuthHandler(MB_API_KEY, MB_API_SECRET)
    auth.set_access_token(MB_ACCESS_TOKEN, MB_ACCESS_TOKEN_SECRET)

    # Connect Tweepy to API

    api = tweepy.API(
        auth,
        wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)

    return api
