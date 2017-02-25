#!/usr/bin/python3

"""
Disco the Amazing Chat Companion!
By Syntox <github.com/syntox32> - Also on Discord @syn#1389

Built using Rapptz's Discord API wrapper
Which can be found here: github.com/Rapptz/discord.py
"""

from disco.config import Config
from disco.discobot import bot

if __name__ == "__main__":
    try:
        bot.run(Config.DISCORD_TOKEN)
    except Exception as e:
        print(e)
