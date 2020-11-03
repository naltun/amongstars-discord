import random, json

# Basic setup of the bot
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='>')

# External commands
def jsonWrite(fileName, user, data):
	try:
		file = open(fileName).read()
	except:
		open(fileName, 'w').write("{}")
		file = open(fileName).read()
	file = json.loads(file)
	file[str(user)] = data
	file = open(fileName, "w").write(json.dumps(file))

def jsonRead(fileName, user):
	try:
		file = open(fileName).read()
	except:
		open(fileName, 'w').write("{}")
		file = open(fileName).read()
	file = json.loads(file)
	return file[str(user)]

# Commands
@bot.command()
async def ping(ctx):
	author = ctx.message.author.mention
	await ctx.send(f'pong, I am operational :smile: {author}')
	print(f"Sent pong {author}")

@bot.command()
async def land(ctx):
	author = ctx.message.author.mention
	diceRoll = random.randint(1,6)
	jsonWrite("data.json", author, diceRoll)
	await ctx.send(f"{author} just landed on a new planet! :rocket:\n There are {diceRoll} things to discover here. :star:")

@bot.command()
async def discover(ctx):
	author = str(ctx.message.author.mention)
	#d = json.loads(open("data.json").read())
	d = jsonRead("data.json", author)
	if d > 0:
		message = f'{author}'

		event = random.randint(1,4)
		if event == 1:
			message += "You see a natural phenomena (huge crystal formations,mirages, weird liquid, etc) "
		elif event == 2:
			message += "You see an animal (humans, giant insects, dinosaurs, etc) "
		elif event == 3:
			message += "You see a plant (grass, giant trees, glowing seeds, etc) "
		elif event == 4:
			message += "You see a ruin (mysterious obelisks, vine-covered temples, wrecked spaceship, etc) "

		location = random.randint(1,13)
		if location == 1:
			message += "in a field taller than you"
		elif location == 2:
			message += "under the light of the moon(s)"
		elif location == 3:
			message += "by a gentle river"
		elif location == 4:
			message += "in a steep canyon"
		elif location == 5:
			message += "in a treetop"
		elif location == 6:
			message += "on the snowy peak of a mountain"
		elif location == 7:
			message += "near a volcano"
		elif location == 8:
			message += "on a glacier"
		elif location == 9:
			message += "deep underground"
		elif location == 10:
			message += "on a cliff face"
		elif location == 11:
			message += "in the desert"
		elif location == 12:
			message += "in deep water"
		elif location == 13:
			message += "floating in the air"

		difficulty = random.randint(1,3)
		if difficulty == 1:
			message += ", it is arduous to get to."
		elif difficulty == 2:
			message += ", you come upon it suddenly."
		elif difficulty == 3:
			message += ", you spot it as you are resting."

		message += " You can now `>log` it :pencil:"
		await ctx.send(message)
		jsonWrite("data.json", author, d-1)
	else:
		await ctx.send(f"{author} You are still in your spaceship, you can't explore yet. Please `>land` first. :rocket:")

@bot.command()
async def log(ctx, *, content):
	author = ctx.message.author.mention
	try:
		oldContent = jsonRead("log.json", author)
		newContent = oldContent + "\n---\n" + content
	except:
		newContent = content
	jsonWrite("log.json", author, newContent)
	await ctx.send(f"{author} Your log have been saved :book:")

@bot.command()
async def burn(ctx):
	author = ctx.message.author.mention
	deletionList = []
	async for message in ctx.channel.history():
		if ">land" in message.content:
			deletionList.append(message)
			break
		elif message.author.mention == author:
			deletionList.append(message)
		elif author in message.content and message.author.bot:
			deletionList.append(message)

	# Removing the internal log
	jsonWrite("log.json", author, "Your log burned :fire:")
	try:
		await ctx.channel.delete_messages(deletionList)
	except:
		await ctx.send("I don't have the permission to remove the messages in the chat :no_entry:")

@bot.command()
async def read(ctx):
	author = ctx.message.author.mention
	content = jsonRead("log.json", author)
	await ctx.send(f"This is the log of {author}\n---\n{content}")

# Starting up the bot
print("The bot is ready")
token = open("token.txt").read()
bot.run(token)
