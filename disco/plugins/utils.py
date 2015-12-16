import logging, random, os
from .plugin import Plugin

log = logging.getLogger("discord")

class UtilityPlugin(Plugin):
	"""
	Plugin template class

	API reference here:
		http://rapptz.github.io/discord.py/api.html#
	"""

	title = "Utility Plugin"
	desc = "What is my purpose?"
	commands = [
		"!regret :: clears the last message by Disco",
		"!8ball <question>(optional) :: The magic 8ball gives it's widsom in desperate times"
		]

	def __init__(self): pass

	def on_ready(self, client): pass
	def on_message(self, client, message):

		if message.content.startswith("!regret"):
			"""
			For when you sit in the front of the classroom
			"""
			msg_q = client.messages
			# check if the member has permissions to edit messages
			# useful if you want to keep people from spaming
			#can_edit = self._check_can_member_edit(message.author)

			while len(msg_q) != 0:
				m = msg_q.pop()
				is_disco = client.user.name.lower() == m.author.name.lower()
				same_channel = m.channel.id == message.channel.id
				if is_disco and same_channel: # and can_edit
					client.edit_message(m, "<snipped by %s>" % message.author.mention())
					prefix = "[%s] User: %s :: Command: '%s'" % (self.title, message.author.name, message.content)
					log.info(prefix)
					break

		if message.content.startswith("!8ball"):
			"""
			May an object used in pool table make decisions in your life
			"""
			try:
				ran = random.randint(0, len(wisdom) - 1)
				if not hasattr(self, "_last_random"):
					self._last_random = ran
				elif ran == self._last_random:
					ran = random.randint(0, len(wisdom) - 1)
				choice = wisdom[ran]
				client.send_message(message.channel, "%s" % choice)
				prefix = "[%s] User: %s :: Command: '%s'" % (self.title, message.author.name, message.content)
				log.info(prefix)
			except Exception as e:
				log.warning("[%s] Exception: %s" % (self.title, e))

	def _check_can_member_edit(self, member):
		roles = member.roles
		for r in roles:
			p = r.permissions
			if p.can_manage_messages:
				return True
		return False

# https://en.wikipedia.org/wiki/Magic_8-Ball
wisdom = [
	"It is certain",
	"It is decidedly so",
	"Without a doubt",
	"Yes, definitely",
	"You may rely on it",
	"As I see it, yes",
	"Most likely",
	"Outlook good",
	"Yes",
	"Signs point to yes",
	"Reply hazy try again",
	"Ask again later",
	"Better not tell you now",
	"Cannot predict now",
	"Concentrate and ask again",
	"Don't count on it",
	"My reply is no",
	"My sources say no",
	"Outlook not so good",
	"Very doubtful"
]