import discord, threading, sys
#from disco.plugins import Plugin
from . import plugins
from .config import version
import logging

log = logging.getLogger("discord")

class DiscoBot(discord.Client):

	def connect(self, email, password):
		log.debug("Email: " + email)
		self.login(email, password)
		
		if not self.is_logged_in:
			print("Login failed.")
			log.error("Login failed.")
			sys.exit(1)

		self.t = threading.Thread(target=self.run)
		self.t.daemon = True
		self.t.start()

		log.info("Thread 'DiscoBot' started.")
		
		while self.is_logged_in:
			self.defcon()

	def defcon(self):
		print("command(s): (exit|e) (leave|l) (join <inv>)")
		cmd = input("> ")
		if cmd == "e" or cmd == "exit":
			log.info("Command: " + cmd)
			log.info("Exiting.")
			self.logout()
			sys.exit(1)
		elif cmd == "leave" or cmd == "l":
			for s in self.servers:
				print("Leaving server: " + s.name)
				log.warning("Leaving server: " + s.name)
				self.leave_server(s)
		elif cmd.split(" ")[0] == "join":
			invite = cmd.split(" ")[1]
			print("Joining server.")
			log.info("Joining server.")
			self.accept_invite(invite)

	def on_ready(self):
		print("Connected!")

		log.info(self.user.name + " successfully connected!")
		log.debug("Username: " + self.user.name)
		log.debug("ID: " + self.user.id)

		log.info("Plugins loaded(%i):" % len(plugins.Plugin.plugins))
		for plugin in plugins.Plugin.plugins:
			if hasattr(plugin, "title"):
				log.info("..." + plugin.title)
		
		for plugin in plugins.Plugin.plugins:
			if hasattr(plugin, "on_ready"):
				plugin.on_ready(plugin, self)


	def on_message(self, message):
		if message.content.startswith("!list"):
			commands = []
			for plugin in plugins.Plugin.plugins:
				if hasattr(plugin, "commands"):
					for c in plugin.commands:
						s = c.split("::")
						cmd = s[0].strip()
						desc = ""
						if len(s) > 1:
							desc = " *%s*" % s[1].strip()
						commands.append("`%s`%s" % (cmd, desc))
			if len(commands) > 0:
				cmd = "\n".join(commands)
				self.send_message(message.channel, "I'm at your service.\n\n%s" % cmd)

		elif message.content.startswith("!plugins"):
			plugs = ""
			for plugin in plugins.Plugin.plugins:
				if hasattr(plugin, "title"):
					plugs += plugin.title + "\n"
			self.send_message(message.channel, "Here be my plugins, master.\n\n" + plugs)

		elif message.content.startswith("!help"):
			credit = "DiscoBot v%s by Syntox <https://github.com/Syntox32/DiscoBot>" % version
			self.send_message(message.channel, credit + "\n\nType `!list` to show all commands")

		for plugin in plugins.Plugin.plugins:
			if hasattr(plugin, "on_message"):
				plugin.on_message(plugin, self, message)


	def on_message_delete(self, message):
		for plugin in plugins.Plugin.plugins:
			if hasattr(plugin, "on_message_delete"):
				plugin.on_message_delete(plugin, self, message)

	def on_message_edit(self, before, after):
		for plugin in plugins.Plugin.plugins:
			if hasattr(plugin, "on_message_edit"):
				plugin.on_message_edit(plugin, self, before,after)


	def on_status(self, member):
		for plugin in plugins.Plugin.plugins:
			if hasattr(plugin, "on_status"):
				plugin.on_status(plugin, self, member)


	def on_channel_delete(self, channel):
		for plugin in plugins.Plugin.plugins:
			if hasattr(plugin, "on_channel_delete"):
				plugin.on_channel_delete(plugin, self, channel)

	def on_channel_create(self, channel):
		for plugin in plugins.Plugin.plugins:
			if hasattr(plugin, "on_channel_create"):
				plugin.on_channel_create(plugin, self, channel)

	def on_channel_update(self, channel):
		for plugin in plugins.Plugin.plugins:
			if hasattr(plugin, "on_channel_update"):
				plugin.on_channel_update(plugin, self, channel)


	def on_member_join(self, member):
		for plugin in plugins.Plugin.plugins:
			if hasattr(plugin, "on_member_join"):
				plugin.on_member_join(plugin, self, member)

	def on_member_remove(self, member):
		for plugin in plugins.Plugin.plugins:
			if hasattr(plugin, "on_member_remove"):
				plugin.on_member_remove(plugin, self, member)

	def on_member_update(self, member):
		for plugin in plugins.Plugin.plugins:
			if hasattr(plugin, "on_member_update"):
				plugin.on_member_update(plugin, self, member)


	def on_server_join(self, server):
		for plugin in plugins.Plugin.plugins:
			if hasattr(plugin, "on_server_join"):
				plugin.on_server_join(plugin, self, server)

	def on_server_remove(self, server):
		for plugin in plugins.Plugin.plugins:
			if hasattr(plugin, "on_server_remove"):
				plugin.on_server_remove(plugin, self, server)

	def on_server_role_create(self, server, role):
		for plugin in plugins.Plugin.plugins:
			if hasattr(plugin, "on_server_role_create"):
				plugin.on_server_role_create(plugin, self, server,role)

	def on_server_role_delete(self, server, role):
		for plugin in plugins.Plugin.plugins:
			if hasattr(plugin, "on_server_role_delete"):
				plugin.on_server_role_delete(plugin, self, server,role)

	def on_server_role_update(self, role):
		for plugin in plugins.Plugin.plugins:
			if hasattr(plugin, "on_server_role_update"):
				plugin.on_server_role_update(plugin, self, role)

	def on_server_available(self, server):
		for plugin in plugins.Plugin.plugins:
			if hasattr(plugin, "on_server_available"):
				plugin.on_server_available(plugin, self, server)

	def on_server_unavailable(self, server):
		for plugin in plugins.Plugin.plugins:
			if hasattr(plugin, "on_server_unavailable"):
				plugin.on_server_unavailable(plugin, self, server)


	def on_voice_state_update(self, member):
		for plugin in plugins.Plugin.plugins:
			if hasattr(plugin, "on_voice_state_update"):
				plugin.on_voice_state_update(plugin, self, member)