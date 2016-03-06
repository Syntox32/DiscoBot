# -*- coding: utf-8 -*-
"""
TestCog class, showing some basic usage of commands, and available events.
"""

import logging

from discord import Message, Channel, Member, Server, Role
from discord.ext import commands

logger = logging.getLogger("disco")

class TestCog:
    """
    TestCog for showing basic command and event usage.
    """
    def __init__(self, bot):
        self.bot = bot
        self.key = self.__class__.__name__

    @commands.command(name="helloworld", pass_context=True)
    async def do_thing(self, ctx):
        """Simple 'say' command"""
        await ctx.bot.say("Hello, it's me again.")

def setup(bot):
    bot.add_cog(TestCog(bot))
