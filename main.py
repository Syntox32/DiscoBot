#!/usr/bin/python
"""
Disco the Amazing Chat Companion!
By Syntox <github.com/syntox32> - I'm also on Discord @syn

Built using Rapptz's Discord API wrapper
Which can be found here: github.com/Rapptz/discord.py
"""

import asyncio, logging, argparse
from disco.discobot import bot
from discord.ext import commands

async def command_listener(bot: commands.Bot):
    """
    Command listener things, used for CLI interaction
    """
    await bot.wait_until_ready()
    print("Welcome to interactive mode, {0}.\n ".format(bot.user.name) \
        + "Commands: e|exit, acceptinv <invite>, leaveall")
    while True:
        cmd = input("#> ")
        if cmd in ("exit", "e"):
            print("Exiting...")
            await bot.logout()
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

	try:
		if args.interactive:
			loop.create_task(command_listener(bot))
		loop.run_until_complete(bot.go())
	except Exception as e:
		loop.run_until_complete(bot.logout())
	finally:
		loop.close()
