from discord.ext import commands

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online')

# # # # Write all of your commands in here # # # #

    #Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong')

def setup(client):
    client.add_cog(Commands(client))