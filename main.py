#!/usr/bin/python
"""
SlutBot by Syn 
	https://github.com/syntox32

Features:
- Says Hello

Discord Python wrapper:
	https://github.com/Rapptz/discord.py
	rapptz.github.io/discord.py/api.html

"""

import discord, threading, sys
from config import log, creds
from plugin import Plugin
from slutbot import SlutBot

# Load plugins
from helloworld import HelloWorld

def main():
	slutbot = SlutBot()
	slutbot.connect(creds["email"], creds["pass"])

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print "Interrupted."
		log.info("KeyboardInterrupt.. exiting.")
		sys.exit(0)