from config import log
from plugin import Plugin

class HelloWorld(Plugin):

	title = "Hello World"
	desc = "What is my purpose?"

	def on_ready(self, client):
		log.info("We're rolling!")
		print "yay!"

	def on_message(self, client, message):
		try:
			log.info(message.author.name)

			if message.author.id != self.user.id:
				log.info("well, shit")
		except Exception, e:
			pass

		if message.content.startswith("!fuckoff"):
			self.send_message(message.channel, "Bye fuckers")
			self.logout()

		if message.content.startswith("!sup"):
			client.send_message(message.channel, "AYYYYLMAO")
