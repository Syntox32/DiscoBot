# -*- coding: utf-8 -*-

import logging, random, json

from disco.config import Config
from discord import Message, Channel, Member, Server, Role
from discord.ext import commands

logger = logging.getLogger("disco")

class Mood:

    def __init__(self, bot):
        self.bot = bot
        self.key = self.__class__.__name__

    def get_mood(self):
        rand_mood_index = random.randint(0, len(moods) - 1)
        mood_cat_len = len(moods[rand_mood_index])
        rand_index = random.randint(0, mood_cat_len - 1)
        return moods[rand_mood_index][rand_index]

    @commands.command(pass_context=True, no_pm=True, aliases=[])
    async def mood(self, ctx):
        """Receive well thought-out wisdom"""

        first = self.get_mood()
        second = self.get_mood()

        prefix = prefixes[random.randint(0, len(prefixes) - 1)]
        template = "{0} is {1} {2} and {3}"
        capitalize = lambda x: x[:1].upper() + x[1:]
        res = template.format(capitalize(ctx.message.author.name),
            prefix, first, second)
        await self.bot.say(res)

def setup(bot):
    bot.add_cog(Mood(bot))

prefixes = [
    "really", "not really",
    "very", "not very",
    "extremely", "a tad bit",
    "obnoxiously", "tremendously",
    "just", "only", "feeling"
]

moods = [
    ["Fear", "Nothing", "Angst", "Serious", "Overworked", "Stormy", "Depressed", "Intense"],
    ["Anxious", "Cool", "Cautious", "Distracted", "Mellow", "So-So"],
    ["Stressed", "Nervous", "Mixed", "Confused", "Upset", "Challenged", "Indignant"],
    ["Mixed Emotions", "Restless", "Irritated", "Distressed", "Worried", "Hopeful"],
    ["Normal", "Alert", "No Great Stress", "Sensitive", "Jealous", "Envious", "Guarded"],
    ["Upbeat", "Pleased", "Somewhat Relaxed", "Motivated", "Flirtatious"],
    ["Normal", "Optimistic", "Accepting", "Calm", "Peaceful", "Pleasant"],
    ["Deeply Relaxed", "Happy", "Lovestruck", "Bliss", "Giving"],
    ["Love", "Romance", "Amorous", "Heat", "Mischievous", "Moody", "Dreamer", "Sensual"],
    ["Very Happy", "Warm", "Affectionate", "Loving", "Infatuated", "Curious"],
]
