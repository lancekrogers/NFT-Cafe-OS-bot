#  import discord
from discord.ext import commands

#  import random
from dotenv import dotenv_values


config = dotenv_values(".env")
description = "Opensea bot for checking the floor price of popular projects"

bot = commands.Bot(command_prefix=config["prefix"], description=description)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("--------")


@bot.event
async def on_message(message):
    if message.channel.name == f"{config['channel']}":
        try:
            await bot.process_commands(message)
        except Exception as e:
            print(e)
    else:
        print(message.channel.name)


@bot.command(
    description="List the current floor price for a given project"
)
async def floor(ctx, projectID=None):
    if projectID:
        await ctx.send("pending...")
        return
    await ctx.send("""Project ID is required. Example:\n!floor projectID""")


@bot.command(description="List projects with available floors")
async def list(ctx):
    await ctx.send("Come back later")


bot.run(config["token"])
