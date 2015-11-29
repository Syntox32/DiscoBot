import logging
from .plugin import Plugin
from discord.utils import find

log = logging.getLogger("discord")

class GreetingPlugin(Plugin):
	"""
	Plugin template class

	API reference here:
		http://rapptz.github.io/discord.py/api.html#
	"""

	title = "Greeting plugin"
	desc = "What is my purpose?"

	def __init__(self): 
		pass

	def on_ready(self, client):
		log.info("Greeting plugin loaded")

	def on_message(self, client, message): 
		pass

	def on_member_join(self, client, member): 
		# get the default text-channel
		channel = member.server.get_default_channel()

		client.send_message(channel, "Welcome to the guild, %s!" % member.name)
	
	def on_member_remove(self, client, member): 
		# get the default text-channel
		channel = member.server.get_default_channel()

		client.send_message(channel, "You lill shit you think u can leave like that, %s" % member.name)