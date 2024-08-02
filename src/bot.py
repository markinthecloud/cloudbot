import os
from twitchio.ext import commands
from dotenv import load_dotenv


load_dotenv()

ACCESS_TOKEN=os.environ['ACCESS_TOKEN']

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=ACCESS_TOKEN, prefix='!', initial_channels=['markinthecloud'])

    async def event_ready(self):
        # Notify us when everything is ready!
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        if message.echo:
            return

        # Print the contents of our message to console...
        print(message.content)

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    @commands.command()
    async def help(self, ctx: commands.Context):
        # Send a link to the available commands!
        await ctx.send(f'Commands: https://markinthecloud.com/commands')

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Sends a hello back!
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command()
    async def web(self, ctx: commands.Context):
        # Sends back my website links
        await ctx.send(f'https://markinthecloud.com | https://thedevopsacademy.com')

    @commands.command()
    async def discord(self, ctx: commands.Context):
        # Returns Discord invite link
        await ctx.send(f'Join our Discord: https://discord.gg/6nVd32U8GY')

    @commands.command()
    async def tiktok(self, ctx: commands.Context):
        # Returns Tiktok link
        await ctx.send(f'Follow Mark on TikTok: https://tiktok.com/@markinthecloud')

    @commands.command()
    async def youtube(self, ctx: commands.Context):
        # Returns Tiktok link
        await ctx.send(f'Follow Mark on YouTube: https://youtube.com/@markinthecloud')

bot = Bot()
bot.run()
# bot.run() is blocking and will stop execution of any below code here until stopped or closed.