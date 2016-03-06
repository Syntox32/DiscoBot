import logging, random, requests, urllib
from .plugin import Plugin
import praw

log = logging.getLogger("discord")

class RedditPlugin(Plugin):
	"""
	Plugin template class

	API reference here:
		http://rapptz.github.io/discord.py/api.html#
	"""

	title = "Reddit plugin"
	desc = "What is my purpose?"
	commands = ["!hot <subreddit>"]

	def __init__(self): pass

	def on_ready(self, client): pass

	def on_message(self, client, message):
		# please don't
		blacklist = ["ttotm", "spacedicks", "rule34", "incest", "rule34lol"]

		if not hasattr(self, "reddit"):
			self.reddit = praw.Reddit(user_agent="disco-the-amazing-chat-companion")

		if message.content.startswith("!hot"):
			cmd = message.content.split(" ")
			if len(cmd) < 2:
				client.send_message(message.channel, "Want to give me a subreddit, %s?"
					% message.author.mention())
				return

			prefix = "[%s] User: %s :: Command: '%s'" % (self.title, message.author.name, message.content)
			log.info(prefix)

			sub = cmd[1].strip().lower()
			if sub in blacklist:
				client.send_message(message.channel, "WHAT THE FUCK %s"
					% message.author.mention())
				log.info("[%s] User: %s :: %s is blacklisted, perv" % (self.title, message.author.name, sub))
				return

			try:
				submissions = [s for s in self.reddit.get_subreddit(sub).get_hot(limit=25)]
				rand = random.randint(0, len(submissions))
				submission = submissions[rand]
				client.send_message(message.channel, submission.url)
				log.info("[%s] User: %s :: Success"  % (self.title, message.author.name))
			except praw.errors.InvalidSubreddit as e:
				client.send_message(message.channel, "That subreddit doesn't exist, you perv %s"
					% message.author.mention())
				log.info("[%s] User: %s :: Doesn't exist"  % (self.title, message.author.name))
			except Exception as e:
				log.warning("[Reddit plugin] Exception: %s" % e)
