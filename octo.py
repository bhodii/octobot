import discord
import os
import types

client = discord.Client()

octo = types.SimpleNamespace()
octo.happy = False


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
      return


  if message.content.startswith('OCTO FLIP'):
    await message.channel.send("OCTO FLIP!")
    octo.happy = not octo.happy
  
  if message.content.startswith('OCTO'):
    if octo.happy:
      picture = discord.File(open('octo_happy.jpg','rb'))
      await message.channel.send(file=picture)
    else:
      picture = discord.File(open('octo_angry.jpg','rb'))
      await message.channel.send(file=picture)

client.run(os.getenv('TOKEN'))
