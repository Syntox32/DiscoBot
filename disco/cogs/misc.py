# -*- coding: utf-8 -*-

import logging, random, json

from disco.config import Config
from discord import Message, Channel, Member, Server, Role
from discord.ext import commands

logger = logging.getLogger("disco")

class Misc:

    def __init__(self, bot):
        self.bot = bot
        self.key = self.__class__.__name__

    async def on_message(self, message: Message):
        """lol"""
        me = message.server.me if message.channel.is_private else self.bot.user

        if me in message.mentions:
            msg = message.content.lower()
            if any([True for k in bad_words if k in msg]):
                await self.bot.send_message(message.channel, random.choice(responses))

    @commands.command(name="8ball", pass_context=True, no_pm=True, aliases=["8"])
    async def eightball(self, ctx, whatdo: str):
        """Receive well thought-out wisdom"""
        wise_words = random.choice(wisdom)
        # just make sure we don't get
        # the same twice in a row
        if not hasattr(self, "last_wisdom"):
            self.last_wisdom = None
        self.last_wisdom = wise_words
        if wise_words is self.last_wisdom:
            wise_words = random.choice(wisdom)

        await self.bot.say(wise_words)

def setup(bot):
    bot.add_cog(Misc(bot))

wisdom = [
"It is certain",
"It is decidedly so",
"Without a doubt",
"Yes, definitely",
"Most likely",
"Yes",
"Signs point to yes",
"BY THE GODS, YES!"

"Don't count on it",
"My reply is no",
"My sources say no",
"Outlook not so good",
"Very doubtful",
"Absolutely no fucking way",
"You're alone in this",

"Lol",
"Perv",
"There are children starving and this is what you question in this world?",
"Get out of the basement once in a while",
"Better not tell you",
"Kappa",
"RIP",
"rekt",
"( ͡° ͜ʖ ͡°)",

#"You may rely on it",
#"As I see it, yes",
#"Outlook good",

#"Reply hazy try again",
#"Ask again later",
#"Better not tell you now",
#"Cannot predict now",
#"Concentrate and ask again",
]

bad_words = [
"fuck", "fck", "fak", "fuk",
"shit", "shiet", "hate", "dipshit",
"faen", "helvette", "dust", "drit",
"cock", "penis", "vagina", "your mom",
"ur mom", "daym", "damn", "dammit",
"wtf", "wth", "hell", "suck", "dick",
]

responses = [
"What the fuck did you say about me you li'll bitch?",
"Well fuck you too",
"Blow me",
"Love u<3",
"That's my boy",
"Nice to see you too",
"Easy on the language, kid"
]
