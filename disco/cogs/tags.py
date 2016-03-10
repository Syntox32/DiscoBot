# -*- coding: utf-8 -*-

import logging, random, json
import asyncio, os

from disco.config import Config
from discord import Message, Channel, Member, Server, Role
from discord.ext import commands

logger = logging.getLogger("disco")

class Tag:

    def __init__(self, bot):
        self.bot = bot
        self.key = self.__class__.__name__

        self.json = {}
        self.need_reload = True
        self.loop = asyncio.get_event_loop()

    async def load(self):
        try:
            with open(self.key + ".json", "r") as f:
                self.json = json.load(f)
        except:
            logger.warning("There isn't a tag.json file yet on this server.")
            self.json = {}

    async def save(self):
        def dump():
            with open(self.key + ".json", "w") as f:
                json.dump(self.json, f)
        await self.loop.run_in_executor(None, dump)

    async def addtag(self, ctx, tagname, value):
        """Add a tag to the json file"""
        if " " in tagname:
            self.bot.say("The tagname cannot contain spaces.")
            return None

        chn_id = str(ctx.message.channel.id)
        if chn_id not in self.json:
            self.json.update({chn_id: {}})

        self.json[chn_id].update({tagname: value})
        await self.save()
        logger.debug("[tag] added tag (name: {0}, value: {1})".format(tagname, value))

    async def gettag(self, ctx, tagname : str):
        if self.need_reload:
            await self.load()
            self.need_reload = False
        chn_id = str(ctx.message.channel.id)
        if chn_id not in self.json:
            await self.bot.say("I couldn't find that tag on this server.")
            return None
        tags = self.json[chn_id]
        if tagname not in tags:
            await self.bot.say("I couldn't find that tag.")
            return None
        tag = tags[tagname]
        await self.bot.say(tag)

    @commands.command(name="tag", pass_context=True, no_pm=True)
    async def _gettag(self, ctx, name : str):
        """Return the contents of a given tag"""
        await self.gettag(ctx, name)

    @commands.command(name="add", pass_context=True, no_pm=True)
    async def _addtagdddd(self, ctx, *args : str):
        """Add a tag with the given name and content"""
        name = args[0]
        content = " ".join(args[1:])
        await self.addtag(ctx, name, content)

    @commands.command(pass_context=True, no_pm=True)
    async def taglist(self, ctx):
        """List all tags registered on this server"""
        if self.need_reload:
            await self.load()
            self.need_reload = False
        chn_id = str(ctx.message.channel.id)
        if chn_id not in self.json:
            await self.bot.say("There are no tags on this server.")
            return None
        tags = self.json[chn_id]

        ret = ""
        for tagname in tags:
            ret += tagname + "\n"
        await self.bot.say("**I have these tags registered:**\n```{}```".format(ret))

def setup(bot):
    bot.add_cog(Tag(bot))
