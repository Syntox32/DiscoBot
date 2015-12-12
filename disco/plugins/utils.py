import logging
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
		"!regret :: clears the last message by Disco"
		]

	def __init__(self): pass

	def on_ready(self, client): pass
	def on_message(self, client, message):

		if message.content.startswith("!regret"):
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

	def _check_can_member_edit(self, member):
		roles = member.roles
		for r in roles:
			p = r.permissions
			if p.can_manage_messages:
				return True
		return False

	def on_message_delete(self, client, message): pass
	def on_message_edit(self, client, before, after): pass

	def on_status(self, client, member): pass
	def on_voice_state_update(self, client, member): pass

	def on_member_join(self, client, member): pass
	def on_member_remove(self, client, member): pass
	def on_member_update(self, client, member): pass

	def on_channel_delete(self, client, channel): pass
	def on_channel_create(self, client, channel): pass
	def on_channel_update(self, client, channel): pass

	def on_server_join(self, client, server): pass
	def on_server_remove(self, client, server): pass
	def on_server_role_create(self, client, server, role): pass
	def on_server_role_delete(self, client, server, role): pass
	def on_server_role_update(self, client, role): pass
	def on_server_available(self, client, server): pass
	def on_server_unavailable(self, client, server): pass