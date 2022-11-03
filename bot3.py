#this version is trying to use arrays that way i can randomize the quiz questions
#3-17 = setting up stuff
import discord
import os
import time
import random

from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix="$")
client = discord.Client(intents=intents)

#variables for the quiz questions, contain the questions for the quiz and then the answers
quizRandom = [0, 1, 2, 3, 4]
quizQuestions = ["T or F: Is Brandon colorblind?", "Which is a Barry B. Benson quote? a. 'You like jazz?' b. 'My sweater is Lacoste, and I have no pants.'", "What year did the first iPhone come out? a) 2005 b) 2006 c) 2007", "Which is the longest river in South Africa? a) Limpopo River b) Orange River c) Vaal River", "T or F: Sir Francis Bacon said 'Knowledge is power'"]
quizAnswers = ["t", "a", "c", "b", "t"]
qOne = 0
qTwo = 0
qThree = 0


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
    #strings together each word the user sent and sends their text back to the channel
    for arg in args:
        response = response + " " + arg
    await ctx.channel.send(response) 

@bot.command(brief='Test your knowledge with a short quiz')
async def quiz(ctx):
    random.shuffle(quizRandom)      
    qOne = quizRandom[0]
    qTwo = quizRandom[1]
    qThree = quizRandom[2]
    await ctx.channel.send(f"1) {quizQuestions[qOne]}\n 2) {quizQuestions[qTwo]}\n 3) {quizQuestions[qThree]}\nTo respond, type $checkQuiz and then your answers.")


@bot.command()
async def checkQuiz(ctx, arg1, arg2, arg3):
    quizScore = 0
    #change their responses to lowercase; check their response with what the response should be based on the answers array; if they typed the correct thing add 1 to their quiz Score
    if arg1.lower() == quizAnswers[qOne]:
        quizScore += 1
    if arg2.lower() == quizAnswers[qTwo]:
        quizScore += 1
    if arg3.lower() == quizAnswers[qThree]:
        quizScore += 1
    #if they got any correct, tell them their score. if not, tell them they suck.
    if quizScore > 0:
        await ctx.channel.send(f"Your score is {round(100*quizScore/3, 2)}%")
    elif quizScore == 0:
        await ctx.channel.send("How did you not get any correct? Your score: 0.00%")


bot.run(TOKEN)
