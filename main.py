#!/usr/bin/python
"""
Disco the Amazing Chat Companion!
By Syntox <github.com/syntox32> - I'm also on Discord @syn

Built using Rapptz's Discord API wrapper
Which can be found here: github.com/Rapptz/discord.py
"""

import asyncio, logging, argparse
from disco import DiscoBot, Config
from discord.ext import commands

async def command_listener():
    """
    Command listener things, used for CLI interaction
    """
    await client.wait_until_ready()
    print("Welcome to interactive mode, {0}.\n ".format(client.user.name) \
        + "Commands: e|exit, acceptinv <invite>, leaveall")
    while True:
        cmd = input("#> ")
        if cmd in ("exit", "e"):
            print("Exiting...")
            await client.logout()
            print("Logged out.")
            break

if __name__ == "__main__":
	"""
	Main entry point.
	"""
	parser = argparse.ArgumentParser(description="Disco the Amazing Chat Companion!")
	parser.add_argument("-i", "--interactive", action="store_true",
		help="Starts DiscoBot in interactive mode, for your needs and purposes." \
		+ "Blocks other output from showing.")
	args = parser.parse_args()
	loop = asyncio.get_event_loop()

	desc = """Disco the Amazing Chat Companion.
	The number one Discord bot for useless things.

	Written by Syntox32 with Python 3.5.1 and the discord.py API wrapper by rapptz
	DiscoBot at GitHub: github.com/Syntox32/DiscoBot

	Find me on discord @syn


	List of commands by category:
	"""
	bot = DiscoBot(command_prefix="!", description=desc)
	login = lambda conf: bot.run(conf.DISCORD_EMAIL, conf.DISCORD_PASS)

	try:
		if args.interactive:
			loop.create_task(command_listener())
		loop.run_until_complete(login(Config))
	except Exception as e:
		loop.run_until_complete(bot.logout())
	finally:
		loop.close()
		
