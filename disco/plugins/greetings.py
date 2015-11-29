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
		self.channels = {}

	def on_ready(self, client): pass
	def on_message(self, client, message): pass

	def on_voice_state_update(self, client, member):
		"""
		Is called when a member joins, leaves, muted or deafend
		"""

		# get the channel
		chn = member.server.get_default_channel()
		
		if member.voice_channel is None:
			print member.id

		#cid = lambda: str(member.voice_channel.id).encode("utf-8")


		#if not hasattr(self, "channels"):
			#print "Created channel dictionary"
			#self.channels = {}

		# we can only send text to a text-channel
		# we also check to see if the member joined, or left
		# the channel, if they joined, we greet them!
		"""
		if chn.type == "text": # and member.voice_channel != None:

			if cid not in self.channels:
				print "added this voice channel id: " + cid
				self.channels[cid] = []
			prev_members = self.channels[cid]
			for m in member.voice_channel.voice_members:
				print "..." + m.name

			# if the member is not in our list, we add him
			me = find(lambda m: m.name == member.name, prev_members)
			print me
			if me is None:
				#self.channels[cid] = member.voice_channel.voice_members
				print "adding member: " + member.name
				client.send_message(chn, "Welcome %s to channel '%s'!" 
					% (member.name, member.voice_channel.name))

			print self.channels[cid]
		
		self.channels[cid] = member.voice_channel.voice_members
		"""