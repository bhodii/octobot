import discord
import os
import types

bot = discord.Client()
#profile = discord.ClientUser()

octo = types.SimpleNamespace()
octo.happy = False

@bot.event
async def on_ready():
  print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
  if message.author == bot.user:
      return

  if message.content.startswith('OCTO FLIP'):
    await message.channel.send("OCTO FLIP!")
    octo.happy = not octo.happy
  
  if message.content.startswith('OCTO'):
    if octo.happy:
      picture = discord.File(open('octo_happy.jpg','rb'))
      av = open('octo_happy.jpg','rb')
      await bot.change_presence(status="OCTO HAPPY!")
      await message.channel.send(file=picture)
      await bot.user.edit(avatar=av.read())

    else:
      picture = discord.File(open('octo_angry.jpg','rb'))
      av = open('octo_angry.jpg','rb')
      await bot.change_presence(status="OCTO ANGRY!")
      await message.channel.send(file=picture)
      await bot.user.edit(avatar=av.read())

bot.run(os.getenv('TOKEN'))
