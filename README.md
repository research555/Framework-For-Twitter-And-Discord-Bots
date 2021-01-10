## Framework For Twitter and Discord Bots

# Introduction

This is a code I have been working on for some time. It allows you to pull tweets from twitter, assign the tweet to someone who can respond to it on Discord,
and send a message to that person on Twitter.

# Purpose

The main purpose of these bots is to facilitate the discussion of Twitter events to Discord and back to Twitter. I have tried to comment as best I can to make the process understandable, and suggested ways it can be built upon, and used.

# Usage

The code is currently being used as a way to provide the direct access between STEM experts on Twitter, to mentees seeking specific help through tweets addressed to a specific account. Future commits will add an ML algorithm capable of determining the topic of questions, making manual assignment of question topic unnecessary.

There is currently a bug in Tweepy which does not allow sending Quick Replies through DMs. I have fixed this on the tweepy api.py file, let me know if you run into problems using the function.

# Edits

## CTA buttons & Quick reply support

I've modified the ```api.py send_direct_message```  function to now also include being able to send CTA (Call To Action) buttons as well as send quick replies. This is the function now:

``` python
    def send_direct_message(self, recipient_id, text, quick_reply_type=None, quick_reply_options=None, ctas=False,
                            ctas_options=None, attachment_type=None, attachment_media_id=None):
        """ Send a direct message to the specified user from the authenticating user """
        json_payload = {'event': {'type': 'message_create', 'message_create': {'target': {'recipient_id': recipient_id}}}}
        json_payload['event']['message_create']['message_data'] = {'text': text}
        if quick_reply_type is not None:
            json_payload['event']['message_create']['message_data']['quick_reply'] = {'type': quick_reply_type, 'options': quick_reply_options}
        if ctas is True:
            json_payload['event']['message_create']['message_data'] = {'text': text, 'ctas': ctas_options}
        if attachment_type is not None and attachment_media_id is not None:
            json_payload['event']['message_create']['message_data']['attachment'] = {'type': attachment_type}
            json_payload['event']['message_create']['message_data']['attachment']['media'] = {'id': attachment_media_id}

        return self._send_direct_message(json_payload=json_payload)
```
You can modify your own file by removing the function and copying in the one above.

You call it like this:

``` python

# # # # Do this for creating CTA buttons # # # #

text = 'some text'
ctas_options = [
                  {
                    "type": "web_url",
                    "label": "Some label 1",
                    "url": "https://www.google.com"
                  },
                  {
                    "type": "web_url",
                    "label": "Some label 2",
                    "url": "https://www.bing.com"
                  }
               ] 
api.send_direct_message(recipient_id=recipient_id, text=text, ctas=True, ctas_options=ctas_options)

# # # # Do this for sending quick replies # # # # 
recipient = 1234567890
text = 'Whos the best programmer in the game?'
reply_options = [
    {
        "label": "Imran Nooraddin",
        "description": "some description",
        "metadata": f"make some metadata to handle replies"  # Could be useful creating metadata that contains useful data if combining bots from two platforms
    },
    {
        "label": "Nooraddin Imran",
        "description": "some other description",
        "metadata": f"some other metadata"
    }
]


api.send_direct_message(recipient_id, text, quick_reply_type='options', quick_reply_options=reply_options).id

```
It works great for me, but I didn't want to create a PR since I haven't tested whether or not it introduces a bug elsewhere in the code. I also haven't changed the ``` _send_direct_message ``` function. You do however need to have access to Account Activity API to utilize the CTA buttons, but not for making quick replies. 

# Disclaimer

Use this code however you'd like, but give credit where credit is due. Remember the human, edit it as much as you'd like, and enjoy the code :)
