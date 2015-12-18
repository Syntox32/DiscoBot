#!/usr/bin/python
"""
DiscoBot by Syntox
	https://github.com/syntox32

Discord Python wrapper:
	GitHub: https://github.com/Rapptz/discord.py
	API Docs: rapptz.github.io/discord.py/api.html

"""

import threading, sys, disco

def main():
	bot = disco.DiscoBot()
	bot.connect(disco.creds["email"], 
		disco.creds["pass"])

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Interrupted.")
		log.info("KeyboardInterrupt.. exiting.")
		sys.exit(0)