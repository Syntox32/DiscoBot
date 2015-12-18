import logging
from .plugin import Plugin

log = logging.getLogger("discord")

class HelloWorld(Plugin):

	title = "Hello World"
	desc = "What is my purpose?"
	commands = ["!sup", "!fuckoff"]

	def on_ready(self, client):
		log.info("We're rolling!")

	def on_message(self, client, message):
		try:
			pass
			#log.info(message.author.name)

			#if message.author.id != self.user.id:
				#log.info("well, shit")
		except Exception as e:
			pass

		if message.content.startswith("!fuckoff"):
			client.send_message(message.channel, "What the fuck did you just say to me you lill shit? " + message.author.mention())
			#client.logout()

		if message.content.startswith("!sup"):
			client.send_message(message.channel, "AYYYYLMAO")
