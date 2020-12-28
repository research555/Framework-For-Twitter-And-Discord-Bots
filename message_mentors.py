from database_credentials import *
from discord_functions import RemoveTupleFromHandles

handles = RemoveTupleFromHandles(handles)

def CreateMessage(handles, sql10, sql11, sql12, sql13, sql14):

    if len(handles) == 3: # If only one mentor is available for assignment
        major = handles[0]
        mentor_1 = handles[1]
        tweet_id = handles[2]
        cursor.execute(sql10, (tweet_id,))  # Finds the handle of who asked the question
        cursor.execute(sql11, (mentor_1,))  # Find handle of mentor with matching major
        mentor_1 = cursor.fetchone()

        mentor_list = []
        for i in mentor_1: # Will allow you to put whatever rows you have of each mentor into a the mentor_list
            item = ''.join(i)
            mentor_list.append(item)

        message = "Some message for one mentor"

        return [message]

    if len(handles) == 4:  # If two mentors assigned

        major = handles[0]
        mentor_1 = handles[1]
        mentor_2 = handles[2]
        tweet_id = handles[3]

        cursor.execute(sql12, (tweet_id,))  # Finds the handle of who asked the question
        question_asker = cursor.fetchone()

        cursor.execute(sql13, (mentor_1,))  # Finds handle of mentor 1
        mentor_1 = cursor.fetchone()

        cursor.execute(sql14, (mentor_2,))  # Finds handle of mentor 2
        mentor_2 = cursor.fetchone()

        mentor_list = []  # Empty list to store mentors in
        for i in mentor_1:
            item = ''.join(i)  # Since they are fetched in tuples, I am here saving each item in the tuple as an item in the list
            mentor_list.append(item)

        for i in mentor_2:
            item = ''.join(i)
            mentor_list.append(item)

        message1 = "Some message for mentor 1"
        message2 = "Some message for mentor 2"

        return [message1, message2]


message_to_mentors = CreateMessage(handles)  # Saves the messages as a list called message_to_mentors






