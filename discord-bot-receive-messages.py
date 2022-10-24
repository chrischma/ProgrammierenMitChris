import discord
import pandas as pd


# bot setup
token = 'YOUR_TOKEN' # you can get a custom bot token here: https://discord.com/developers/applications
client = discord.Client(intents=discord.Intents.default())


# teaching our bot to receive messages
@client.event 
async def on_message(msg):
    print(msg.content)

# running the bot
client.run(token)
