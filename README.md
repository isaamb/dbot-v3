# dbot-v3
This bot's functions (add to a discord channel to see them in action!): 
  
  -Type "$ping", and the bot responds with "Pong!"
  
  -Type "$joke", and the bot with respond with a joke
 
  -Type "$echo [insert text here]", and the bot will echo your text
 
  -Type "$quiz" to receive 3 quiz questions, and respond with "$checkQuiz [insert answers with spaces between]" (ex. #checkQuiz x y z) to check them and get your score

The main source I used to begin developing this bot is https://betterprogramming.pub/how-to-make-discord-bot-commands-in-python-2cae39cbfd55

Command handling is where rather than having a long string of "if, elif" statments, the main node calls out to another file that contains the commands. In my bot, I do still have everything in the main bot.py file, but each command is a separate function (and specified as such by @bot.command)

My bot's commands work because after the bot has logged in, it is listening to user input. On line 16, the bot defines any command called to it as using the symbol "$", so it knows that when a message follows "$", it checks for a command that aligns with that input. Each command that has an assignment is defined after the "async def" line below "@bot.command" (for example, async def ping(ctx) means that it will perform the following function anytime $ping is called.) Following that, the rest of the code just runs whatever the function is meant to achieve (in $ping's case, just responding with "Pong!")
