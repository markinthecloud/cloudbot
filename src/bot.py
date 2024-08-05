import os
from twitchio.ext import commands
from dotenv import load_dotenv
from roadmap import create_db_tables, add_new_user, retrieve_progress_data, calculate_progress_pc, complete_topic
from utils import extract_topic

load_dotenv()

ACCESS_TOKEN=os.environ['ACCESS_TOKEN']
MODULES = """
            Linux, Bash Scripting, Docker, Python, Git & GitHub, Basic Networking,
            AWS or Azure, Terraform, CI/CD - Github Actions, Ansible, Build Projects
            """

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

    @commands.command()
    async def join(self, ctx: commands.Context):
        # Allows a player to join DevOps and record their progress against the roadmap
        response = add_new_user(ctx.author.name)
        await ctx.send(response)

    @commands.command()
    async def roadmap(self, ctx: commands.Context):
        # Returns the current DevOps roadmap
        await ctx.send(f"DevOps Roadmap: {MODULES}")      

    @commands.command()
    async def progress(self, ctx: commands.Context):
        # Allows a player to join DevOps and record their progress against the roadmap
        modules, completed = retrieve_progress_data(ctx.author.name)
        progress = calculate_progress_pc(modules, completed)
        topic = modules[0]
        await ctx.send(f'{ctx.author.name} has made {progress}% progress so far as is working on {topic}')  

    @commands.command()
    async def complete(self, ctx: commands.Context):
        # Allows a player to complete a topic and progress through the roadmap
        # complete_topic(ctx.author.name, ctx.message)
        topic = extract_topic(ctx.message.content)
        if topic != None:
            response = complete_topic(ctx.author.name, topic)
        else:
            response = "Invalid use of !complete command. Here's an example: !complete Linux"
        await ctx.send(f'{response}') 

create_db_tables()
bot = Bot()
bot.run()
# bot.run() is blocking and will stop execution of any below code here until stopped or closed.