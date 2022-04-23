import discord
import Logger
import json
from argparse import ArgumentParser
class Bot(discord.Client):
    def __init__(self):
        super().__init__(command_prefix="!")
        self.log=Logger.Logger('example.log')
        self.log.infolog(f"{self.user} has connected to Discord!") #gives username none?! 

    async def on_ready(self):
        print("Le bot est prêt.")

    async def on_message(self,message):
        self.log.infolog(message.content)
        if('hello' in message.content.lower()):
            await message.channel.send('Hi!')

    def parse_args():
        parser = ArgumentParser()
        parser.add_argument(
            "-c", "--config", help="Config file", required=True, dest="config"
        )
        return parser.parse_args()



bot = Bot()
with open("config.json","r") as f:
    data = json.load(f)
bot.run(data['TOKEN'])