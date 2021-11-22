import logging
from discord import utils, File
from discord_slash import cog_ext
from discord.ext.commands import Cog, Context, command
from discord_slash import SlashCommand, SlashContext

from shared import guild_ids

log = logging.getLogger('bot.' + __name__)

class Flip(Cog):
  """Flips octobot from Angry to Happy and back again."""

  def __init__(self, bot):
    self.bot = bot

  @cog_ext.cog_slash(name="flip",
    description="Flip how to feel",
    guild_ids=guild_ids)

  async def flip(self, ctx: SlashContext):
    """Make octobot happy or angry with /flip"""

    from shared import octo
    octo['happy'] = not octo['happy']
    log.info(f'Octo now {octo["happy"]} from {ctx.author}')

    role = utils.get(ctx.guild.roles, name='Server Octopus')

    if octo['happy']:
#      await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="everyone HAPPILY!"))
      await ctx.send(content="OCTO HAPPY!")
      await role.edit(color=0x3498db)
      with open("octo_happy.jpg", 'rb') as fp:
        await ctx.channel.send(files=[File(fp)], delete_after=10)

    else:
      await ctx.send(content="OCTO ANGRY.")
      await role.edit(color=0x2ecc71)
      with open("octo_angry.jpg", 'rb') as fp:
        await ctx.channel.send(files=[File(fp)], delete_after=10)
