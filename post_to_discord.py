import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

DISCORD_URL = os.getenv('DISCORD_URL')

def PostMessageToDiscord(message, DISCORD_URL): # Will post your tweet to a Discord channel

    url = DISCORD_URL
    headers = {}
    headers['content-type'] = 'application/json'
    data = {'content': message}
    response = requests.post(url=url, headers=headers, data=json.dumps(data)).status_code

    if response == 204:
        print("success")
    else:
        print(response)  # Handle Exceptions

    return response


def PostIDToDiscord(tweet_id, DISCORD_URL): # Will post the tweetID to a Discord channel. Makes assignment easier on mobile

    url = DISCORD_URL
    headers = {}
    headers['content-type'] = 'application/json'
    data = {'content': tweet_id}
    response = requests.post(url=url, headers=headers, data=json.dumps(data)).status_code

    if response == 204:
        print("success")
    else:
        print(response)  # Handle exceptions

    return response
