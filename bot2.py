import math
import discord
import os
import time
import json
import random

from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix="$")
client = discord.Client(intents=intents)

#when the bot has logged in, send a message in the node channel for confirmation
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(brief='pong')
async def ping(ctx):
	await ctx.channel.send("pong")

@bot.command(brief='Try this for a laugh!')
async def joke(ctx):
    ranNum = random.randint(0,2) #generate a random number from 0 to 2
    #for whichever number is generated, send a specific joke
    #reference: https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/ 
    match ranNum:
      case 0:
        await ctx.channel.send("What\'s a duck\'s favorite ballet?")
        time.sleep(2)
        await ctx.channel.send("The Nut-quacker")
      case 1:
        await ctx.channel.send("Why didn't the vampire go to the party?")
        time.sleep(2)
        await ctx.channel.send("He wasn't in-bited")
      case 2:
        await ctx.channel.send("Why do Java programmers have to use glasses?")
        time.sleep(2)
        await ctx.channel.send("Because they don't C#")

@bot.command(brief='Echoes your response')
async def echo(ctx, *args):
    response = ""
    #strings together everything the user sent
    for arg in args:
        response = response + " " + arg
    await ctx.channel.send(response) 

@bot.command(brief='Test your knowledge with a short quiz')
async def quiz(ctx):
    await ctx.channel.send("1) T or F: Is Brandon colorblind?\n 2) Which is a Barry B. Benson quote? a. 'You like jazz?' b. 'My sweater is Lacoste, and I have no pants.'\n3)What year did the first iPhone come out? a) 2005 b) 2006 c) 2007\nTo respond, type $checkQuiz and then your answers.")

@bot.command()
async def checkQuiz(ctx, arg1, arg2, arg3):
    quizScore = 0
    #change their responses to lowercase; if they typed the correct thing add 1 to their quiz Score
    if arg1.lower() == "t":
        quizScore += 1
    if arg2.lower() == "a":
        quizScore += 1
    if arg3.lower() == "c":
        quizScore += 1
    #if they got any correct, tell them their score. if not, tell them they suck.
    if quizScore > 0:
        await ctx.channel.send(f"Your score is {round(100*quizScore/3, 2)}%")
    elif quizScore == 0:
        await ctx.channel.send("How did you not get any correct?")


bot.run(TOKEN)
