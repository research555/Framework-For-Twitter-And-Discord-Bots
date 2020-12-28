from twitter_auth import *
from database_credentials import *
import json
import random
from tweepy import Stream
from tweepy.streaming import StreamListener
from post_to_discord import *
from sql_code import *
import traceback

api = TSTwitterAuth(TS_ACCESS_TOKEN, TS_ACCESS_TOKEN_SECRET, TS_API_KEY, TS_API_SECRET)

class StdOutListener(StreamListener):


    def on_error(self, status):
        print(status) # Do stuff when an error is encountered
        return status

    def on_data(self, data): # This function defines what happens when you get a tweet
        tweet_data = json.loads(data)
        tweet = tweet_data['text']
        print(tweet_data)
        if "#Some Hashtag" in tweet:  # you can also sort by hashtag using entities (check out Twitters API), or anything else
            tweet_id = tweet_data['id']
            handle = tweet_data['user']['screen_name']
            full_name = tweet_data['user']['name']
            URL = f"https://twitter.com/{handle}/status/{tweet_id}"
            message = "Some message for your discord to post on your discord server"

            LogTweet(tweet_id, handle, full_name, URL)
            PostMessageToDiscord(message)
            PostIDToDiscord(tweet_id)  # This function makes it easier to copy the tweet ID on mobile
            recipient_id = 1234567890  # Enter the username id here to whoever you'd like to DM
            text = "Some text to send to the recipient of your twitter DM"
            api.send_direct_message(recipient_id=recipient_id, text=text)
        else:
            pass


listener = StdOutListener()
stream = Stream(auth, listener)
tweets = stream.filter(track=['Your Account username Here'])  # Edit this to include your account username
