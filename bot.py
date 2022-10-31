import discord
import os
import time
import json
import random

from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv("TOKEN")

#UNTIL I CAN GET JSON TO WORK:
quizQuestions = ["T or F: Is Brandon colorblind?", "Which is a Barry B. Benson quote? a. 'You like jazz?' b. 'My sweater is Lacoste, and I have no pants.'"]
quizAnswers = ["T", "a"]


#with open('config.json') as f:
   # data = json.load(f)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix="$")
client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def ping(ctx):
	await ctx.channel.send("pong")

@bot.command()
async def joke(ctx):
    await ctx.channel.send("What\'s a duck\'s favorite ballet?")
    time.sleep(2)
    await ctx.channel.send("The Nut-quacker")

@bot.command()
async def print(ctx, *args):
    response = ""

    for arg in args:
        response = response + " " + arg

    await ctx.channel.send(response)

ranNums = 0

@bot.command()
async def quiz(ctx):
    ranNums = random.sample(range(0, len(quizQuestions)), 1) #https://docs.python.org/3.3/library/random.html#random.sample
    print(ranNums)
    await ctx.channel.send("1) T or F: Is Brandon colorblind?\n 2) Which is a Barry B. Benson quote? a. 'You like jazz?' b. 'My sweater is Lacoste, and I have no pants.'\nTo respond, type $checkQuiz and then your answers.")

@bot.command()
async def checkQuiz(ctx, arg1, arg2):
    quizScore = 0
   # response = ""
    if arg1 == "T" or "t":
        quizScore += 1
    if arg2 == "a" or "A":
        quizScore += 1
    if quizScore > 0:
        await ctx.channel.send(f"Well done! Your score is {quizScore}")


bot.run(TOKEN)
