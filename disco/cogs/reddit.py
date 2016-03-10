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
        await self.get_post(ctx, "ass")

    @commands.command(pass_context=True, no_pm=True)
    async def top(self, ctx, *args: str):
        """Get top images from a subreddit.

        The first argument passed is the subreddit name.
        The second argument is the type of top you want to retrieve from.
        This argument can be any of the letters a, d, h, m, w or y.
            (a)ll time, (d)ay, (h)our, (m)onth, (w)eek, (y)ear

            e.g.: !top aww a
        """
        content_predicate = None
        top_from = "a" # all
        limit = 25
        subreddit = args[0]
        # if we get two arguments, the first is the
        # subreddit and the second is the typ of 'top'
        if len(args) == 2:
            top_from = str(args[1])
            if top_from == "a": # all time
                logger.debug("predicate set to {}".format(top_from))
                content_predicate = lambda x: x.get_top_from_all(limit=limit)
            elif top_from == "d": # day
                content_predicate = lambda x: x.get_top_from_day(limit=limit)
                logger.debug("predicate set to {}".format(top_from))
            elif top_from == "h": # hour
                content_predicate = lambda x: x.get_top_from_hour(limit=limit)
                logger.debug("predicate set to {}".format(top_from))
            elif top_from == "m": # month
                content_predicate = lambda x: x.get_top_from_month(limit=limit)
                logger.debug("predicate set to {}".format(top_from))
            elif top_from == "w": # week
                content_predicate = lambda x: x.get_top_from_week(limit=limit)
                logger.debug("predicate set to {}".format(top_from))
            elif top_from == "y": # year
                content_predicate = lambda x: x.get_top_from_year(limit=limit)
                logger.debug("predicate set to {}".format(top_from))
            else:
                await self.bot.say("There is no type of top named '{0}'. Type !help top for more info.".format(top_from))
        else:
            logger.debug("predicate set to {}".format(top_from))
            content_predicate = lambda x: x.get_top_from_all(limit=limit)

        await self.get_post(ctx, subreddit, predicate=content_predicate)

    @commands.command(pass_context=True, no_pm=True)
    async def hot(self, ctx, *args: str):
        """Get hot images from a subreddit"""
        sub = None
        lim = 25
        if len(args) == 1:
            sub = args[0]
        elif len(args) == 2:
            sub = args[0]
            lim = int(args[1])
        else:
            return # invalid number of arguments
        await self.get_post(ctx, sub, lim)

    async def get_post(self, ctx, sub: str, limit=25, predicate=None):
        """Get a hot-or-top image from a subreddit

        `sub` is the name of the requested subreddit.
        `limit` is the amount of submissons to get from that subreddit.
        `predicate` is a lambda given a RedditContentObject type
            use this to customize what type of posts you want to retrieve

            e.g.: lambda x: x.get_hot(limit=25) # will get the 25 last hot posts
        """
        # blacklist check
        if sub in self.blacklist:
            await self.bot.say("That sub is blacklisted, you perv.")
            return

        try:
            submissions = []
            subreddit_object = self.reddit.get_subreddit(sub)
            if predicate is None:
                submissions = [s for s in subreddit_object.get_hot(limit=limit)]
            else: # get top submissions
                logger.debug("[reddit] using submission_predicate")
                submissions = [s for s in predicate(subreddit_object)]

            # check if we have any submissions at all, for possible empty subreddits
            if len(submissions) == 0:
                await setl.bot.say("It looks like there were no submissions from that subreddit.")

            ext = [ ".jpg", ".png", ".gif", ".webm" ]
            img_priority = []
            use_priority = True
            for s in submissions:
                for e in ext:
                    if s.url.endswith(e):
                        img_priority.append(s)
                        continue
            logger.debug("length of priority: {}".format(str(len(img_priority))))
            if len(img_priority) > 0:
                random_sub_url = random.choice(img_priority).url
            else:
                random_sub_url = random.choice(submissions).url
                use_priority = False

            # there is no embed for webms :(
            if random_sub_url.endswith(".webm") and "imgur" in random_sub_url:
                random_sub_url = random_sub_url.replace(".webm", ".gifv")

            #await self.bot.say(random_sub_url)
            if use_priority:
                # the url is most likely an image of gif, then we upload it
                await try_embed_image(self.bot, ctx, random_sub_url)
            else:
                # if it's not a picture we just post the link to it,
                # we don't embed articles, etc.
                await self.bot.say(random_sub_url)
        except praw.errors.InvalidSubreddit as e:
            await self.bot.say("That subreddit doesn't exist, you perv.")
        except Exception as e:
            logger.warning("[Reddit] Error occured: {}".format(e))

def setup(bot):
    bot.add_cog(Reddit(bot))
