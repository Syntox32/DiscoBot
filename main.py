#!/usr/bin/python3
"""
SlutBot by Syn 

Features:
- Says Hello

https://github.com/syntox32
https://github.com/Rapptz/discord.py
rapptz.github.io/discord.py/api.html
"""

import discord, threading, sys
from config import log, login

slutbot = discord.Client()
slutbot = SlutBot()
slutthread = threading.Thread(target=slutbot.run)

class SlutBot(discord.Client):
	def __init__(self): pass

	def login(self, email, password):
		log.debug("Email: " + email))
		self.login(email, password)
		
		if not self.is_logged_in:
			print "Login failed."
			log.error("Login failed for 'SlutBot'")
			sys.exit(1)

		self.slutthread = threading.Thread(target=self.run)
		self.slutthread.start()
		log.info("Thread 'slutthread' started.")

	def on_ready(self): pass
	def on_message(self, message):
		self.send_message(message.channel, "Hello World!")

	def on_message_delete(self, message): pass
	def on_message_edit(self, before, after): pass
	def on_status(self, member): pass
	
	def on_channel_delete(self, channel): pass
	def on_channel_create(self, channel): pass
	def on_channel_update(self, channel): pass
	
	def on_member_join(self, member): pass
	def on_member_remove(self, member): pass
	def on_member_update(self, member): pass
	
	def on_server_create(self, server): pass
	def on_server_delete(self, server): pass
	
	def on_server_role_create(self, server, role): pass
	def on_server_role_delete(self, server, role): pass
	def on_server_role_update(self, role): pass

	def on_voice_state_update(self, member): pass

@slutbot.event
def on_ready():
	print "Connected!"
	log.info(slutbot.user.name + " successfully connected!")
	log.debug("Username: " + slutbot.user.name)
	log.debug("ID: " + slutbot.user.id)
	defcon()

def main():
	log.debug("Email: {}".format(login["email"]))
	slutbot.login(login["email"], login["pass"])
	
	if not slutbot.is_logged_in:
		print "Login failed."
		log.error("Login failed for 'SlutBot'")
		sys.exit(1)

	slutthread.start()
	log.info("Thread 'slutthread' started.")

def defcon():
	while True:
		print "command(s): (exit|e)"
		cmd = raw_input("> ")
		if cmd == "e" or cmd == "exit":
			log.info("Command: " + cmd)
			log.info("Exiting.")
			slutbot.logout()
			sys.exit(1)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print "Interrupted."
		log.info("KeyboardInterrupt.. exiting.")
		sys.exit(0)