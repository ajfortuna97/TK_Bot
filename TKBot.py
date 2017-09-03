# here we go, bot time
# begin outside imports
import discord
import asyncio
import random
import ctypes
import io
from discord import opus
import time
import urllib

# import internal files/functions
import tabletopFunctions
import musicPlayerFunctions
import leaderboardFunctions
import specialWordTriggers
import specificImageTriggers

# import MySQL database features
import MySQLdb


client = discord.Client()

@client.event
@asyncio.coroutine
def on_message(message):
	author = message.author

	# begin tabletop functions

	# end tabletop functions

	# begin music player functions

	# end music player functions

	# begin leaderboard functions

	# end leaderboard functions

	# begin special word triggers

	# end special word triggers

	# begin specific image triggers

	# end special word triggers

