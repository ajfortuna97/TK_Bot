#!/usr/bin/env python3
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
import sys
# import internal files/functions
from tabletopFunctions import *
from leaderboardFunctions import *
#import musicPlayerFunctions
#import leaderboardFunctions
#import specialWordTriggers
#import specificImageTriggers

# import MySQL database features
import MySQLdb
import _mysql


client = discord.Client()
isMute = False

# establish connection to the server
db = MySQLdb.connect("[hostname]", "[account]", "[password]", "[initial table]")


print("Bot loaded.")

@client.event
@asyncio.coroutine
def on_message(message):
		author = message.author

		# begin tabletop functions
		if message.content.startswith('!pfstatgen'):
			yield from stat_gen(message, client)
		if message.content.startswith('!roll'):
			yield from rolling_dice(message, client)
		# end tabletop functions

		# begin music player functions

		# end music player functions

		# begin leaderboard functions
		if message.content.startswith('!viewleaders'):
			yield from view_leader(message, client, db)
		# end leaderboard functions

		# begin special word triggers

		# end special word triggers

		# begin specific image triggers

		# end special word triggers

		# begin administrative functions
		if message.content.startswith('~mute'):
			isMute = False
		if message.content.startswith('~unmute'):
			isMute = True
		if message.content.startswith('end'):
			print("Closing")
			client.logout()
			print("Closed")
			sys.exit()
		# end administrative functions


#client.run('[BOT TOKEN]')
#client.run('[BOTUSERNAME]', '[BOTPASSWORD]')
