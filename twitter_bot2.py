from database_credentials import *
from twitter_auth import *
import json


"""
If you'd like, you can combine these two functions into one function. I decided to keep them as two
"""
api = MBTwitterAuth(MB_ACCESS_TOKEN, MB_ACCESS_TOKEN_SECRET, MB_API_KEY, MB_API_SECRET)

# # # #  Messages one mentor # # # #

def MessageOneMentor(handles):

    try:
        mentor_id_1 = api.get_user(screen_name=handles[1]).id
        api.send_direct_message(recipient_id=mentor_id_1, text='Hi There')

    except Exception as e:
        print(e) # Handle exceptions



# # # # Messages two mentors # # # #

def MessageTwoMentors(handles):

    try:
        mentor_id_1 = api.get_user(screen_name=handles[1]).id
        mentor_id_2 = api.get_user(screen_name=handles[2]).id
        api.send_direct_message(recipient_id=mentor_id_1, text='Hi There')
        api.send_direct_message(recipient_id=mentor_id_2, text='Hi There')
    except Exception as e:
        print(e) # Handle exceptions