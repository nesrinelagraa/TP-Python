from email import message
import discord
import json
import logging

client=discord.Client()
with open("config.json","r") as f:
    data = json.load(f)

#Screamhandler, Filehandler
#for logger we need to create another class and 

logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is when this event was logged.')
'''class MyBot(discord.Customer):
    def __init__(self):
        super().__init__()
    
    @client.event
    async def on_ready(self):
        self.log.infolog(f"{self.user} has connected to Discord!")

    @client.event
    async def on_message(message):
        if('hello' in message.content.lower()):
            await message.channel.send('Hi!')

class Message(message):
    def __init__(self):
        pass'''
    


@client.event
async def on_ready():
    print("The bot is ready!")

@client.event
async def on_message(message):
    logging.basicConfig(format='%(asctime)s %(message)s')
    logging.info(message.content)
    if('hello' in message.content.lower()):
        await message.channel.send('Hi!')
    ''' print(message.content)
    await message.channel.send(message.content)
    logging.basicConfig(format='%(asctime)s %(message)s')
    logging.info(message.content)'''


client.run(data['TOKEN'])
f.close()