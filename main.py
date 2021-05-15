import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

help_command = commands.DefaultHelpCommand(no_category='Commands')
bot = commands.Bot(command_prefix=commands.when_mentioned_or('>'), help_command=help_command)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.command(brief="Pong!", description="Pings the bot and displays the latency")
async def ping(ctx):
    await ctx.send(f':ping_pong: | Latency: {int(bot.latency * 1000)}ms')


bot.run(os.getenv('TOKEN'))
