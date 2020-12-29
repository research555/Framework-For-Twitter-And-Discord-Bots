## Framework For Twitter and Discord Bots

# Introduction

This is a code I have been working on for some time. It allows you to pull tweets from twitter, assign the tweet to someone who can respond to it on Discord,
and send a message to that person on Twitter.

# Purpose

The main purpose of these bots is to facilitate the discussion of Twitter events to Discord and back to Twitter. I have tried to comment as best I can to make the process understandable, and suggested ways it can be built upon, and used.

# Usage

The code is currently being used as a way to provide the direct access between STEM experts on Twitter, to mentees seeking specific help through tweets addressed to a specific account. Future commits will add an ML algorithm capable of determining the topic of questions, making manual assignment of question topic unnecessary.

There is currently a bug in Tweepy which does not allow sending Quick Replies through DMs. I have fixed this on the tweepy api.py file, let me know if you run into problems using the function.

# Disclaimer

Use this code however you'd like, but give credit where credit is due. Remember the human, edit it as much as you'd like, and enjoy the code :)
