import logging
from .plugin import Plugin

log = logging.getLogger("discord")

class AdminPlugin(Plugin):
	"""
	Plugin template class

	API reference here:
		http://rapptz.github.io/discord.py/api.html#
	"""

	title = "Admin- and role-administration"
	desc = "What is my purpose?"

	def __init__(self): pass

	def on_ready(self, client): pass
	def on_message(self, client, message): pass

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
