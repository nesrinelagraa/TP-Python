import discord
from message import Message
import Logger
import json
from argparse import ArgumentParser, Namespace


class Bot(discord.Client):

    def __init__(self):
        super().__init__(command_prefix="!")
        self.log=Logger.Logger('example.log')
        self.log.infolog(f"{self.user} has connected to Discord!") #gives username none?! 

    async def on_ready(self):
        print("Le bot est prêt.")

    async def on_message(self,msg):
        self.log.infolog(f"{msg.author.name} said {msg.content}")
        m= Message(msg.content)
        ans=m.replyMessage()
        await msg.channel.send(ans)
    
    async def on_member_join(self,member):
        self.log.infolog(f"L'utilisateur {member.display_name} a rejoint le serveur !")

    def parse_args()-> Namespace:
        parser = ArgumentParser()
        parser.add_argument(
            "-c", "--config", help="Config file", required=True, dest="config"
        )
        return parser.parse_args()



bot = Bot()

with open("config.json","r") as f:
    data = json.load(f)
bot.run(data['TOKEN'])

args=bot.parse_args()

with open(args.config,"r") as f:
    config = json.load(f)
print(config)