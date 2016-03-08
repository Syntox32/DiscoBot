# -*- coding: utf-8 -*-

import logging, random, json
import praw

from disco.config import Config
from disco.utils import try_embed_image
from discord import Message, Channel, Member, Server, Role
from discord.ext import commands

logger = logging.getLogger("disco")

class Reddit:

    def __init__(self, bot):
        self.bot = bot
        self.key = self.__class__.__name__

        self.reddit = praw.Reddit(user_agent="disco-the-amazing-chat-companion")

        # lol u sick nerds
        self.blacklist = ["ttotm", "spacedicks", "rule34", "incest", "rule34lol"]

    @commands.command(pass_context=True, no_pm=True)
    async def booty(self, ctx):
        """A pirates best friend"""
        await self.get_hot(ctx, "ass")

    @commands.command(pass_context=True, no_pm=True, aliases=["reddit", "r"])
    async def hot(self, ctx, *args: str):
        """Get hot images from a subreddit"""
        await self.get_hot(ctx, *args)

    async def get_hot(self, ctx, *args: str):
        """Get a hot image from a subreddit"""
        sub = None
        lim = 25
        if len(args) == 1:
            sub = args[0]
        elif len(args) == 2:
            sub = args[0]
            lim = int(args[1])
        else:
            return

        if sub in self.blacklist:
            await self.bot.say("That sub is blacklisted, you perv.")
            return

        try:
            submissions = [s for s in self.reddit.get_subreddit(sub).get_hot(limit=lim)]

            ext = [ ".jpg", ".png", ".gif", ".webm" ]
            priority = []
            for s in submissions:
                for e in ext:
                    if s.url.endswith(e):
                        priority.append(s)
                        continue
            logger.debug("length fo priority: {}".format(str(len(priority))))
            if len(priority) > 0:
                random_sub_url = random.choice(priority).url
            else:
                random_sub_url = random.choice(submissions).url

            # there is no embed for webms :(
            if random_sub_url.endswith(".webm") and "imgur" in random_sub_url:
                random_sub_url = random_sub_url.replace(".webm", ".gifv")

            #await self.bot.say(random_sub_url)
            await try_embed_image(self.bot, ctx, random_sub_url)
        except praw.errors.InvalidSubreddit as e:
            await self.bot.say("That subreddit doesn't exist, you perv.")
        except Exception as e:
            logger.warning("[Reddit] Error occured: {}".format(e))

def setup(bot):
    bot.add_cog(Reddit(bot))
