# -*- coding: utf-8 -*-
"""
DiscoBot the Amazing Chat Companion
"""

import logging
from .config import Config
from .utils import configure_logger

import discord
from discord.ext import commands
from discord.ext.commands import Context
from discord import Message, Channel, Member, Server, Role

configure_logger("disco", stream=True, level=Config.LOGGING_LEVEL)
configure_logger("discord", stream=False, level=Config.LOGGING_LEVEL)

logger = logging.getLogger("disco")


class DiscoBot(commands.Bot):
	"""DiscoBot the Amazing Chat Companion"""

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		missing = Config.DISCORD_EMAIL is None or Config.DISCORD_PASS is None
		if missing:
			raise AttributeError("Missing credentials.")

	def go(self):
		"""Go, go, go"""
		self.run(Config.DISCORD_EMAIL, Config.DISCORD_PASS)

	def register_extensions(self, extension: [str]):
		"""Register the required cogs"""
		logger.info("Loading extension...")
		try:
			for ext in extensions:
				logger.info(" loaded cog: {0}".format(ext))
				self.load_extension(ext)
		except Exception as e:
			logger.error("Error loading extension \'{0}\': {1}".format(ext, e))


desc = """Disco the Amazing Chat Companion.
The number one Discord bot for useless things.

Written by Syntox32 with Python 3.5.1 and the discord.py API wrapper by rapptz
DiscoBot at GitHub: github.com/Syntox32/DiscoBot

Find me on discord @syn


List of commands by category:
"""

extensions = [
	"disco.cogs.test",
]

bot = DiscoBot(command_prefix=["!", "?", "$"], description=desc)
bot.register_extensions(extensions)

@bot.event
async def on_ready():
	"""On ready message"""
	logger.info("Connected!")
	logger.info("Username: {0}".format(bot.user.name))
	logger.info("ID: {0}".format(bot.user.id))

@bot.event
async def on_command(command, ctx: Context):
	"""Called whenever a command is called"""
	pass

@bot.event
async def on_message(message: Message):
	"""Called when a message is created and sent to a server."""
	logger.info("loluwot")

	# if we override the on message we need to
	# make sure the bot sees the message if we want
	# any other on_message events to fire
	await bot.process_commands(message)


# Other events, uncomment as needed
# Having them uncommented all the time might
# cause some wierd behaviour with overrides sometimes(?)

#@bot.event
#async def on_error():
#	"""Override normal error handling behaviour"""
#	pass

#@bot.event
#async def on_command_error(error, ctx: Context):
#	"""Called when a command raises an error"""
#	pass

#@bot.event
#async def on_channel_update(before: Channel, after: Channel):
#	"""Called whenever a channel is updated. e.g. changed name, topic, permissions."""
#	msg = "Channel changed name from {0} to {1}".format(before.name, after.name)
#	await self.bot.send_message(after, msg)

#@bot.event
#async def on_member_update(before: Member, after: Member):
#	"""Called when a Member updates their profile."""
#	pass

#@bot.event
#async def on_server_role_update(before: Role, after: Role):
#	"""Called when a Role is changed server-wide."""
#	pass

#@bot.event
#async def on_voice_state_update(before: Member, after: Member):
#	"""Called when a Member changes their voice state."""
#	pass
