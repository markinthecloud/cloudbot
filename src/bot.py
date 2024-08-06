"""
Twitch bot for interaction with users whilst streaming. Handles all chat msgs & commands
"""
import os
from twitchio.ext import commands
from dotenv import load_dotenv
# from rich import print as rprint
from roadmap import create_db_tables, add_new_user, retrieve_progress_data, complete_topic, \
    update_role
from utils import extract_topic, extract_role, calculate_progress_pc

load_dotenv()

ACCESS_TOKEN=os.environ['ACCESS_TOKEN']
MODULES = """
            Linux, Bash Scripting, Docker, Python, Git & GitHub, Basic Networking,
            AWS or Azure, Terraform, CI/CD - Github Actions, Ansible, Build Projects
            """

class Bot(commands.Bot):
    """
    Main Bot class to listen for and process incoming messages & commands
    """
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
        print(f"[red]{message.content}")

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    @commands.command()
    async def help(self, ctx: commands.Context):
        """
        Sends a link to the available commands when !help is used
        """
        await ctx.send('Commands: https://markinthecloud.com/commands')

    @commands.command()
    async def hello(self, ctx: commands.Context):
        """
        Sends a "hello" back to the user when !hello is used
        """
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command()
    async def web(self, ctx: commands.Context):
        """
        Sends links to my websites when !web is used
        """
        await ctx.send('https://markinthecloud.com | https://thedevopsacademy.com')

    @commands.command()
    async def discord(self, ctx: commands.Context):
        """
        Sends a link join Discord when !discord is used
        """
        await ctx.send('Join our Discord: https://discord.gg/6nVd32U8GY')

    @commands.command()
    async def tiktok(self, ctx: commands.Context):
        """
        Sends a link to TikTok when !tiktok is used
        """
        await ctx.send('Follow Mark on TikTok: https://tiktok.com/@markinthecloud')

    @commands.command()
    async def youtube(self, ctx: commands.Context):
        """
        Sends a link to YouTube when !youtube is used
        """
        await ctx.send('Follow Mark on YouTube: https://youtube.com/@markinthecloud')

    @commands.command()
    async def github(self, ctx: commands.Context):
        """
        Sends a link the GitHub repo for this project when !github is used
        """
        await ctx.send('This project is on GitHub here: \
                       https://github.com/markinthecloud/cloudbot')

    @commands.command()
    async def join(self, ctx: commands.Context):
        """
        Adds the user to the db when !join is used
        """
        response = add_new_user(ctx.author.name)
        await ctx.send(response)

    @commands.command()
    async def roadmap(self, ctx: commands.Context):
        """
        Sends a list of the roadmap skills when !roadmap is used
        """
        await ctx.send(f"DevOps Roadmap: {MODULES}")

    @commands.command()
    async def progress(self, ctx: commands.Context):
        """
        Sends a summary of the user's progress when !progress is used
        """
        modules, completed = retrieve_progress_data(ctx.author.name)
        progress = calculate_progress_pc(modules, completed)
        topic = modules[0]
        await ctx.send(f'{ctx.author.name} has made {progress}% progress so far as is \
                       working on {topic}')

    @commands.command()
    async def complete(self, ctx: commands.Context):
        """
        Marks a topic as complete in the db when !complete {topic} is used
        """
        topic = extract_topic(ctx.message.content)
        if topic is not None:
            response = complete_topic(ctx.author.name, topic)
        else:
            response = "Invalid use of !complete command. Here's an example: !complete Linux"
        await ctx.send(f'{response}')

    @commands.command()
    async def role(self, ctx: commands.Context):
        """
        Updates the user's role in the db when !role {role title} is used
        """
        role = extract_role(ctx.message.content)
        if role is not None:
            response = update_role(ctx.author.name, role)
        else:
            response = "Make sure you've used !join and formatted your !role correctly. \
                E.g. !role DevOps Engineer"
        await ctx.send(f'{response}')

create_db_tables()
bot = Bot()
bot.run()
# bot.run() is blocking and will stop execution of any below code here until stopped or closed.
