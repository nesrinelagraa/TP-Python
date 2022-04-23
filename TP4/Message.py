import discord
class Message():

    def __init__(self, message):
        #super().__init__(command_prefix="!")
        self.message=message

    async def replyMessage(self):
        if('hello' in self.message.content.lower() or 'hi' in self.message.content.lower()) :
            return 'Hi!'