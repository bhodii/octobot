"""Shared resources for the bot and cogs.
"""
import shelve
from os import getenv
from dotenv import load_dotenv

load_dotenv()
guild_ids = [int(n) for n in getenv('GUILD_IDS').split(sep=',')]

# Persistent variables
octo = shelve.open('octo')
if not 'happy' in octo:
  octo['happy'] = True 
