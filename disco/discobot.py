# -*- coding: utf-8 -*-
"""
DiscoBot the Amazing Chat Companion
"""

import logging
from .config import Config
from .errors import MissingCredentials
from .utils import configure_logger

import discord
from discord.ext import commands
#from discord import Message, Channel, Member, Server, Role

logger = configure_logger("disco", stream=True, level=Config.LOGGING_LEVEL)
configure_logger("discord", stream=False, level=Config.LOGGING_LEVEL)

extensions = [
	# If you make any new cogs, add them to the list below
	"disco.cogs.test",
]

class DiscoBot(commands.Bot):
	"""
	DiscoBot the Amazing Chat Companion
	"""
	def __init__(self, *args, **kwargs):
		"""
		Initalize the bot and do some sanity checks on the login credentials
		"""
		super().__init__(*args, **kwargs)

		credentials_error = """Credentials could not be found. Set the
			credentials as enviornment variables, and try again."""

		if Config.DISCORD_EMAIL is None or Config.DISCORD_PASS is None:
			logger.error(credentials_error)
			raise MissingCredentials()

		self.register_cogs()
		logger.info("Initalized DiscoBot successfully.")

	def register_cogs(self):
		"""Register the required cogs"""
		logger.info("Registering cogs...")
		try:
			for ext in extensions:
				logger.info(" Added cog: {0}".format(ext))
				self.load_extension(ext)
		except Exception as e:
			logger.error("Error ladoing extension \'{0}\': {1}"
				.format(ext, e))

	async def on_ready(self):
		"""
		On ready message
		"""
		logger.info("Connected!")
		logger.info("Username: {0}".format(self.user.name))
		logger.info("ID: {0}".format(self.user.id))
