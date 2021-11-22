import datetime
import logging
from os import getenv
from pathlib import Path
from dotenv import load_dotenv
from discord import Client, Intents, Embed, Game
from discord.ext.commands import Bot, CommandOnCooldown
from discord_slash import SlashCommand, SlashContext


from cogs.flip import Flip
from cogs.tiktok import Tiktok

load_dotenv()
logdir = Path(getenv('LOGDIR'))
token = getenv('TOKEN')

intents = Intents.default()
intents.members = True

def setup_logger() -> logging.Logger:
  """Create and return the master Logger object."""
  logdir.mkdir(exist_ok=True)
  timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
  logfile = logdir / f'{timestamp}.log'
  logger = logging.getLogger('bot')  # the actual logger instance
  logger.setLevel(logging.DEBUG)  # capture all log levels
  console_log = logging.StreamHandler()
  console_log.setLevel(logging.DEBUG)
  file_log = logging.FileHandler(logfile, 'w', 'utf8')
  file_log.setLevel(logging.DEBUG)  # log levels to be written to file
  formatter = logging.Formatter('{asctime} - {name} - {levelname} - {message}', style='{')
#                      format='%(levelname)-8s %(module) 10s: %(funcName)s %(message)s')
  console_log.setFormatter(formatter)
  file_log.setFormatter(formatter)
  logger.addHandler(console_log)
  logger.addHandler(file_log)
  return logger

def main():
  log = setup_logger()
  activity = Game("TikTok")
  
  bot = Bot(command_prefix='!', activity=activity, intents=intents)
  slash = SlashCommand(bot, sync_commands=True) # slash not used but needed to sync commands

  @bot.event
  async def on_ready():
      log.info(f'Logged in as {bot.user}.')

  @bot.event
  async def on_command_error(ctx, error):
      if isinstance(error, CommandOnCooldown):
          await ctx.send(f'Please wait {error.retry_after:.0f} seconds.')
      raise error  # re-raise the error so all the errors will still show up in console

  bot.add_cog(Flip(bot))
  bot.add_cog(Tiktok(bot))
  bot.run(getenv('TOKEN'))

if __name__ == '__main__':
    main()
