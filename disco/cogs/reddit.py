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

        self.reddit = praw.Reddit(client_id=Config.R_ID,
                                    client_secret=Config.R_TOK,
                                    password=Config.R_SEC,
                                    username=Config.R_USR,
                                    user_agent="disco the chat companion")
        logger.debug("reddit: user authenticated as: {}".format(self.reddit.user.me()))

        # lol u sick nerds
        self.blacklist = ["ttotm", "spacedicks", "rule34", "incest", "rule34lol"]

    @commands.command(pass_context=True, no_pm=True)
    async def booty(self, ctx):
        """A pirates best friend"""
        await self.get_post(ctx, "ass", "hot")

    @commands.command(pass_context=True, no_pm=True)
    async def top(self, ctx, *args: str):
        """Get top images from a subreddit.

        The first argument passed is the subreddit name.
        The second argument is the type of top you want to retrieve from.
        This argument can be any of the letters a, d, h, m, w or y.
            (a)ll time, (d)ay, (h)our, (m)onth, (w)eek, (y)ear

            e.g.: !top aww a
        """
        #content_predicate = None
        top_from = "a" # all
        limit = 25
        subreddit = args[0]
        # if we get two arguments, the first is the
        # subreddit and the second is the typ of 'top'
        if len(args) == 2:
            top_filter = str(args[1])
            await self.get_post(ctx, subreddit, top_filter)
        else:
            logger.debug("predicate set to {}".format(top_from))
            #content_predicate = lambda x: x.get_top_from_all(limit=limit)
            await self.get_post(ctx, subreddit, "all")

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
        await self.get_post(ctx, sub, "hot")

    async def get_post(self, ctx, sub: str, top_filter: str, limit=25):
        """Get a hot-or-top image from a subreddit

        `sub` is the name of the requested subreddit.
        `limit` is the amount of submissons to get from that subreddit.
        `predicate` is a lambda given a RedditContentObject type
            use this to customize what type of posts you want to retrieve

            e.g.: lambda x: x.get_hot(limit=25) # will get the 25 last hot posts
        """
        logger.debug("DEBUG FLAG 3")
        # blacklist check
        if sub in self.blacklist:
            await self.bot.say("That sub is blacklisted, you perv.")
            return

        try:
            submissions = []
            logger.debug(sub)
            subreddit_object = self.reddit.subreddit(sub)
            logger.debug(subreddit_object)

            if top_filter is "hot":
                generator = subreddit_object.hot()
                for _ in range(limit): submissions.append(generator.next())
                submissions = [s for s in subreddit_object.hot(limit=limit)]

            else: # get top submissions
                logger.debug("[reddit] using submission_predicate")
                logger.debug("reddit: subreddit filter set to \'{}\'".format(top_filter))

                generator = None
                if top_filter == "a" or top_filter == "all":
                    generator = subreddit_object.top('all')
                elif top_filter == "d" or top_filter == "day":
                    generator = subreddit_object.top('day')
                elif top_filter == "h" or top_filter == "hour":
                    generator = subreddit_object.top('hour')
                elif top_filter == "m" or top_filter == "month":
                    generator = subreddit_object.top('month')
                elif top_filter == "w" or top_filter == "week":
                    generator = subreddit_object.top('week')
                elif top_filter == "y" or top_filter == "year":
                    generator = subreddit_object.top('year')

                if generator is None: logger.debug("debug warning: generator was none")
                for _ in range(limit): submissions.append(generator.next())

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
            logger.error("[Reddit] Error occured: {}".format(e))

def setup(bot):
    bot.add_cog(Reddit(bot))
