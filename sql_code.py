from database_credentials import *
import re
from datetime import datetime
from sql_var import *

# # # # Check If ID Is In Database And Update If Not # # # #


def LogTweet(tweet_id, handle, full_name, URL, sql1, sql2, sql3, sql4):

    # # # # For tweets table # # # #

    cursor.execute(sql1, (tweet_id,)) # Checks if tweet is already logged in tweets table
    result = cursor.fetchall()

    if not result: # If tweet is not already logged, insert it
        cursor.execute(sql2, (tweet_id, handle, full_name, URL,))
        mydb.commit()


    # # # # For assigned_mentors table # # # #

    cursor.execute(sql3, (tweet_id,))  # Checks if tweet is already logged in assigned_mentors table
    result = cursor.fetchall()
    if not result:  # If tweet is not already logged, insert it
        cursor.execute(sql4, (tweet_id,))
        mydb.commit()

    return tweet_id


# # # # Checks that the tweetID that was assigned on discord # # # #


def CheckID(message, sql5):

    discord_tweet_id = re.search(r"\(([A-Za-z0-9_]+)\)", message.content).group(1)  # finds substring within parentheses ()
    cursor.execute(sql5, (discord_tweet_id,))  # Checks if substring already in your tweets table
    result = cursor.fetchone()  # If tweet ID not in your tweets table returns None

    return result, discord_tweet_id


# # # # Checks the major that was assigned on Discord and returns the handles of someone attached to that major # # # #


def AppendMentors(message, sql6):

    assignment = re.search(r"\[([A-Za-z0-9_]+)\]", message.content).group(1)  # Finds substring within square brackets []
    cursor.execute(sql6, (assignment,))
    result = cursor.fetchall()
    handles = [assignment]  # Ensures major is always on index 0
    for handle in result:
        handles.append(handle)  # Appends in tuple form

    return handles, assignment

# # # # Check if mentors are already assigned, if not return False # # # #

def AreMentorsAssigned(sql7):
    cursor.execute(sql7)
    is_assigned = cursor.fetchone()

    if is_assigned is None:  # No tweet_id results in None type
        error = 'Tweet ID does not exist on YOUR TABLE NAME table'

    elif is_assigned[0] is not None:  # Mentors already assigned
        error = 'Mentors have already been assigned to this tweet ID'
    else:
        error = False

    return error


# # # # Logs mentors assigned via Discord into mentors_assigned table # # # #


def LogMentorAssignment(handles, sql8, sql9):

    if len(handles) == 4: # Tweet_id, major and 2 experts
        cursor.execute(sql8, (handles[0], handles[1], handles[2], handles[3],))
        mydb.commit()
        success = True

    elif len(handles) == 3: # Tweet_id, major and 1 expert
        cursor.execute(sql9, (handles[0], handles[1], handles[2],))
        mydb.commit()
        success = True

    else:
        success = False

    return success