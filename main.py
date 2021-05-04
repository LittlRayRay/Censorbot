import discord
import os
from keep_alive import keep_alive
from discord.ext import commands
from better_profanity import profanity

os.system('python3 -m commands')

profanity.load_censor_words_from_file('./profanity.txt')

client = commands.Bot(command_prefix = '$')
money_registry = []
list1 = ['myself', 'me', 'i']

@client.event
async def on_ready(): 
	print('Bot is ready!')
	await client.change_presence(activity=discord.Game('$help'))

@client.command()
async def displayembed(ctx, *, Title):
    embed = discord.Embed(title= Title, description= Title, color = 6400 ) #,color=Hex code
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round (client.latency * 1000)}ms')

@client.command()
async def kill(ctx, *, WhoToKill):
    embed = discord.Embed(description=f'{WhoToKill} eats some mushrooms from the wild. Too bad they were poisonous...', color= 6400) #,color=Hex code
    await ctx.send(embed=embed)


@client.event
async def on_message(message):
    mention = f'<@!{client.user.id}>'
    if mention in message.content:
      embed = discord.Embed(description=f"_{message.author.mention} :bell: You ping me, I ping you._", color= 6400 )
      await message.channel.send(embed=embed)

    if str(message.channel) == "pictures" and message.content != '':
      if message.author != client.user:
        await message.channel.purge(limit=1)
        embed = discord.Embed(description= f"Sorry{message.author.mention}! Only Pictures!", color = 6400)
        await message.channel.send(embed=embed)
      else:
        pass 

    if '' in message.content:
      embed = discord.Embed(title= "Self Roles", description = "React to this message to get these roles! ")

    if not message.author.bot:
      if profanity.contains_profanity(message.content):
        await message.delete()
        embed = discord.Embed(description= f"{message.author.mention} :octagonal_sign: Mind your language!", color = 6400)
        await message.channel.send(embed=embed)
  
    await client.process_commands(message)


@client.event
async def on_member_join(member):
	print(f'{member} has joined the server! Welcome!')

@client.event
async def on_member_remove(member):
	print(f'{member} has left! Goodbai! GLHF')

keep_alive()
client.run(os.getenv('TOKEN'))
