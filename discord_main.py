from discord.ext import commands
from database_credentials import *
import random
import os
from dotenv import load_dotenv
import discord
import re
from sql_code import *
from discord_functions import *
from twitter_bot2 import *
from twitter_auth import *
import traceback


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix='.') # Tells us which prefix to use when calling bot

"""
An event is a piece of code that runs when the bot detects that a specific activity has happened
this can be things like messages, reactions etc
"""

api = MBTwitterAuth(MB_ACCESS_TOKEN, MB_ACCESS_TOKEN_SECRET, MB_API_KEY, MB_API_SECRET)

@client.event
async def on_message(message):
    await client.process_commands(message) # Makes sure your other commands on .cogs work
    try:
        if str(message.channel) == 'Your channel name here':  # if the message is in the correct channel
            if client.user.mentioned_in(message):  # Detects mention of your bot
                if message.author.bot is False:  # if user is not a bot, returns False
                    result, discord_tweet_id = CheckID(message)
                    if result is None: # If the tweet ID was input incorrectly or doesnt exist on your database
                        await message.channel.send("```There doesn't seem to be a Tweet ID matching the one you just sent me, are you sure you have entered the correct ID?```")

                    if result is not None:  # If the ID in the discord message is on your database
                        handles, assignment = AppendMentors(message)  # Appends mentor handles in tuple form to handles
                        handles.append(discord_tweet_id)  # Appends tweet_id as final item on handles
                        handles = RemoveTupleFromHandles(handles)  # Changes the tuple form of the handle into string item on handles
                        no_match_id_txt, no_match_major_txt, success_assignment_1_txt, \
                            appending_mentor_failure_txt = VariousLongText(assignment, handles)  # Text for messages to Discord

                        if len(handles) == 2:  # if major does not exist
                            await message.channel.send(no_match_major_txt)

                        success = LogMentorAssignment(handles)  # True if successful, False if not

                        if len(handles) == 3:  # If list only has one mentor
                            if success is True:
                                await message.channel.send(success_assignment_1_txt)

                            else:
                                await message.channel.send(appending_mentor_failure_txt)

                        if len(handles) == 4:  # If list have 2 mentors
                            if success is True:
                                await message.channel.send(f'```Woo! You have successfully assigned {handles[1]} and {handles[2]} to the question. They are experts in {assignment}.\n\n'
                                                           f'If you think this is a mistake, please react to this message within 1 minute```')
                                MessageTwoMentors(handles)
                            else:
                                await message.channel.send(appending_mentor_failure_txt)
    except Exception: # Handle exceptions
        channel_id = 1234567890 # Put the channel you'd like error messages to be sent to
        channel = client.get_channel(channel_id)
        await channel.send('There has been an error. See details below\n\n' + traceback.format_exc())


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(token)

