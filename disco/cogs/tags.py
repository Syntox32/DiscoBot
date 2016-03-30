# -*- coding: utf-8 -*-

import logging, random, json
import asyncio, os

from disco.config import Config
from discord import Message, Channel, Member, Server, Role
from discord.ext import commands

logger = logging.getLogger("disco")

class AsyncJson:
    """A simple async file wrapper for json"""

    def __init__(self, filename, *, loop=None, pretty=False, data=None):
        self.data = {} if data is None else data
        self.filename = os.path.abspath(filename)
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self.pretty = pretty

    def _dump(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            kwargs = {}
            if self.pretty:
                kwargs = { "indent": 4 }
            f.write(json.dumps(self.data, **kwargs))

    async def save(self):
        await self.loop.run_in_executor(None, self._dump)

    async def load(self):
        if not os.path.exists(self.filename):
            logger.warning("[asyncjson] no file of name exists: {}"
                .format(self.filename))
            await self.save()
            return self.data
        with open(self.filename, "r", encoding="utf-8") as f:
            self.data = json.loads(f.read())

    def get(self, key):
        if key not in self.data:
            self.data[key] = {}
            logger.error("RESETTING LOL")
        return self.data[key]

    def put(self, key, value):
        if key not in self.data:
            self.data[key] = {}
            logger.error("RESETTING LOL")
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]


class Tag:
    """Simple cog for adding and fetching tags on different servers"""

    def __init__(self, bot):
        self.bot = bot

        self.storage = AsyncJson("Tag.json")
        self.backup = AsyncJson("Tag.bak")
        self.has_loaded = False

    async def prepare(self):
        if not self.has_loaded:
            await self.storage.load()
            self.has_loaded = True

            # at each fresh start, the bot creates a backup of the last tag file,
            # if the current file is not empty, because it did that one time,
            # and it was a bitch to recover all the tags. so this is an attempt
            # at atleast trying to detect it, sigh.
            if self.storage.data is not None and len(self.storage.data) != 0 and self.storage.data != "":
                self.backup.data = self.storage.data
                await self.backup.save()
            else:
                logger.warning("[tag] tag file was probably corrupted, you should check that out")

    async def add_tag(self, ctx, tagname, value, author):
        await self.prepare()

        if len(tagname) > 200:
            await ctx.bot.say("The tag name cannot be over 200 characters.")
        if len(value) > 2000:
            await ctx.bot.say("The tag value cannot be over 2000 characters.")

        data = { "content": value, "author": author }
        json_data = self.storage.get(ctx.message.server.id)
        json_data[tagname] = data
        self.storage.put(ctx.message.server.id, json_data)
        await self.storage.save()

        logger.debug("[tag] adding tag: {0} (content: {1}, author: {2})"
            .format(tagname, value, author))
        await ctx.bot.say("\U0001f44c")

    async def get_tag(self, ctx, tagname):
        await self.prepare()

        data = self.storage.get(ctx.message.server.id)
        if tagname not in data:
            await ctx.bot.say("I couldn't find that tag.")
            return
        tag_val = data[tagname]["content"]

        logger.debug("[tag] fetching tag: {0} (content: {1})"
            .format(tagname, tag_val))
        await ctx.bot.say(tag_val)

    async def del_tag(self, ctx, tagname):
        await self.prepare()

        data = self.storage.get(ctx.message.server.id)
        if tagname not in data:
            await ctx.bot.say("I couldn't find that tag.")
            return

        tag_val = data[tagname]["content"]
        del data[tagname]
        self.storage.put(ctx.message.server.id, data)
        await self.storage.save()

        logger.debug("[tag] deleting tag: {0} (content: {1}, author: {2})"
            .format(tagname, tag_val, ctx.message.author.name))
        await ctx.bot.say("\U0001f44c")

    async def list_tags(self, ctx):
        await self.prepare()

        data = self.storage.get(ctx.message.server.id)
        ret = ""
        for tagname in sorted(data.keys()):
            name = tagname # or else 'tagname' would not update wtf?
            ret += "`{}` ".format(name)

        await self.bot.say("**I have these tags registered({0}):**\n{1}"
            .format(str(len(data)), ret))

    @commands.command(pass_context=True, no_pm=True, aliases=["t"])
    async def tag(self, ctx, name : str):
        """Fetch a tag with the given name."""
        await self.get_tag(ctx, name)

    @commands.command(pass_context=True, no_pm=True)
    async def add(self, ctx, name : str, content : str):
        """Add a tag with the given name and content."""
        await self.add_tag(ctx, name, content, ctx.message.author.name)

    @commands.command(name="del", pass_context=True, no_pm=True)
    async def _del(self, ctx, name : str):
        """Delete a tag using the given name."""
        await self.del_tag(ctx, name)

    @commands.command(pass_context=True, no_pm=True, aliases=["listtags", "taglist"])
    async def tags(self, ctx):
        """List all tags available."""
        await self.list_tags(ctx)

def setup(bot):
    bot.add_cog(Tag(bot))
