# -*- coding: utf-8 -*-
"""
TestCog class, showing some basic usage of commands, and available events.
"""

import logging

from ..mixin import CogMixin

from discord import Message, Channel, Member, Server, Role
from discord.ext import commands

logger = logging.getLogger("disco")

class TestCog(CogMixin):
    """
    TestCog for showing basic command and event usage.
    """
    def __init__(self, bot=None, *args, **kwargs):
    	self.bot = bot

    # Commands

    @commands.command(name="helloworld",
        pass_context=True,
        description="prints a thing to the channel")
    async def do_thing(self, ctx):
        """
        Simple 'say' command
        """
        await ctx.bot.say("Hello, it's me again.")

    # Events

    async def on_ready(self):
    	"""Called when the client is done preparing the data received from Discord."""
    	pass

    async def on_message(self, message: Message):
    	"""Called when a message is created and sent to a server."""
    	pass

    async def on_channel_update(self, before: Channel, after: Channel):
    	"""Called whenever a channel is updated. e.g. changed name, topic, permissions."""
    	msg = "Channel changed name from {0} to {1}".format(before.name, after.name)
    	await self.bot.send_message(after, msg)

    async def on_member_update(self, before: Member, after: Member):
    	"""Called when a Member updates their profile."""
    	pass

    async def on_server_role_update(self, before: Role, after: Role):
    	"""Called when a Role is changed server-wide."""
    	pass

    async def on_voice_state_update(self, before: Member, after: Member):
    	"""Called when a Member changes their voice state."""
    	pass
