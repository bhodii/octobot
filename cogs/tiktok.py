from __future__ import unicode_literals
import logging
from io import open
from asyncio import sleep
from youtube_dl import YoutubeDL
from discord import File
from discord_slash import cog_ext
from discord.ext.commands import Cog, Context, command
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option

from shared import guild_ids
log = logging.getLogger('bot.' + __name__)

class Tiktok(Cog):
  def __init__(self, bot):
    self.bot = bot

  @cog_ext.cog_slash(
    name="tiktok",
    description="Takes a tiktok URL and pastes the downloaded video",
    guild_ids=guild_ids,
    options=[
      create_option(
        name="url",
        description="Tiktok URL",
        option_type=3,
        required=True
      )
    ]
  )

  async def tiktok(self, ctx: SlashContext, url: str):
    """Give me a long and shitty tiktok (or youtube-dl supported) URL and I'll do all the work for you"""
    
    await ctx.defer()
    log.info(f'Trying: {url} For: {ctx.author.name}')

    ydl_opts = {
      'noprogress': True,
      'retries': 0,
      'download_archive': "download_archive",
      'nocheckcertificate': True,
      'restrictfilenames': True,
      'updatetime': False,
      'writeinfojson': True,
      'verbose': True,
      'logger': log
      #'progress_hooks': [my_hook],
    }

    # Retry because TikTok breaks for no good reason sometimes
    info = {}
    error = BaseException
    ydl = YoutubeDL(ydl_opts)
    for _ in range(3):
      try:
        info = ydl.extract_info(url) # Also downloads file
        log.info(f'Downloaded: {ydl.prepare_filename(info)} For: {ctx.author.name}')
        # TODO Add in {'requestor': ctx.author.name, 'requestor_id': ctx.author_id } to info json
      except BaseException as err:
        log.error(f'Failed Try #{_}: {err}')
        error = err
        await sleep(3)
        continue
      else:
        with open(ydl.prepare_filename(info), 'rb') as fp:
          await ctx.send(content=f'{info["description"]}', files=[File(fp)])
        break
    else:
      log.error(f'Failed Download: {url} For: {ctx.author.name}')
      await ctx.send(content='Octobot has failed you. Please try again in a minute.')
