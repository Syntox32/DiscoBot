# -*- coding: utf-8 -*-
"""
DiscoBot the Amazing Chat Companion
"""

import logging
from .config import Config
from .errors import MissingCredentials
from .cogs.test import TestCog

import discord
from discord.ext import commands

logger = logging.getLogger("disco")


class DiscoBot(commands.Bot):
	"""
	DiscoBot the Amazing Chat Companion
	"""
	def __init__(self, *args, **kwargs):
		"""
		Initalize the bot and do some sanity checks on the login credentials
		"""
		super().__init__(*args, **kwargs)
		logger.debug("Command Prefix: \'{0}\'".format(self.command_prefix))

		if Config.DISCORD_EMAIL is None or Config.DISCORD_PASS is None:
			logger.error("Credentials could not be found. Set the "
				+ "credentials as enviornment variables, and try again.")
			raise MissingCredentials()

		self.register_cogs()
		logger.info("Initalized DiscoBot successfully.")

	def register_cogs(self):
		"""
		Register the required cogs
		"""
		instances = [
			# If you make any new cogs, add them to the list below
			TestCog(self)
		]
		logger.info("Registering cogs...")
		for inst in instances:
			logger.info(" Added cog: {0}".format(type(inst).__name__))
			self.add_cog(inst)

	async def on_ready(self):
		"""
		On ready message
		"""
		logger.info("Connected!")
		logger.info("Username: {0}".format(self.user.name))
		logger.info("ID: {0}\n".format(self.user.id))
