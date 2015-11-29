#!/usr/bin/python
"""
DiscoBot by Syn 
	https://github.com/syntox32

Features:
- Says Hello

Discord Python wrapper:
	https://github.com/Rapptz/discord.py
	rapptz.github.io/discord.py/api.html

"""

import threading
import sys
import disco

def main():
	bot = disco.DiscoBot()
	bot.connect(
		disco.creds["email"],
		disco.creds["pass"]
	)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print "Interrupted."
		log.info("KeyboardInterrupt.. exiting.")
		sys.exit(0)