import discord
import os
import types

bot = discord.Client()

octo = types.SimpleNamespace()
octo.happy = False

def octo_flip:
    await message.channel.send("OCTO FLIP!")
    octo.happy = not octo.happy
    role = discord.utils.get(message.guild.roles, name='Server Octopus')

    if octo.happy:
  #      try:
  #        av = open('octo_happy.jpg','rb')
  #        await bot.user.edit(avatar=av.read(),color=0x3498db)
  #      finally:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="everyone HAPPILY!"))
        await role.edit(color=0x3498db)

    else:
  #      try:
  #        av = open('octo_angry.jpg','rb')
  #        await bot.user.edit(avatar=av.read(),color=0x2ecc71)
  #      finally:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="everyone ANGRILY!"))
        await role.edit(color=0x2ecc71)

  if message.content.startswith('OCTO'):
    if octo.happy:
      picture = discord.File(open('octo_happy.jpg','rb'))
      await message.channel.send(file=picture)
    else:
      picture = discord.File(open('octo_angry.jpg','rb'))
      await message.channel.send(file=picture)

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
    role = discord.utils.get(message.guild.roles, name='Server Octopus')

    if octo.happy:
#      try:
#        av = open('octo_happy.jpg','rb')
#        await bot.user.edit(avatar=av.read(),color=0x3498db)
#      finally:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="everyone HAPPILY!"))
        await role.edit(color=0x3498db)

    else:
#      try:
#        av = open('octo_angry.jpg','rb')
#        await bot.user.edit(avatar=av.read(),color=0x2ecc71)
#      finally:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="everyone ANGRILY!"))
        await role.edit(color=0x2ecc71)

  if message.content.startswith('OCTO'):
    if octo.happy:
      picture = discord.File(open('octo_happy.jpg','rb'))
      await message.channel.send(file=picture)
    else:
      picture = discord.File(open('octo_angry.jpg','rb'))
      await message.channel.send(file=picture)

bot.run(os.getenv('TOKEN'))

# serverid 386127177114189824