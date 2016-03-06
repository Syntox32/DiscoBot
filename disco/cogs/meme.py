# -*- coding: utf-8 -*-

import logging, random, json
import asyncio, aiohttp

from disco.config import Config
from discord import Message, Channel, Member, Server, Role
from discord.ext import commands

logger = logging.getLogger("disco")

class Meme:

    def __init__(self, bot):
        self.bot = bot
        self.key = self.__class__.__name__

        missing = Config.IMGFLIP_USER is None or Config.IMGFLIP_PASS is None
        if missing:
            raise AttributeError("Missing credentials.")

    async def _make_request(self, top: str, bot: str, id=None):
        meme_id = id
        if meme_id is None:
            meme_id = random.sample(memes.keys(), 1)[0]

        try:
            url = "https://api.imgflip.com/caption_image"
            payload = {
                "template_id": meme_id,
                "text0": top,
                "text1": bot,
                "username": Config.IMGFLIP_USER,
                "password": Config.IMGFLIP_PASS
            }

            success = False
            async with aiohttp.post(url, data=payload) as resp:
                resp_json = await resp.json()
                success = resp_json["success"]
            if success:
                return resp_json["data"]["url"]
            else:
                return None
        except Exception as e:
            logger.error("[Meme] Error fetching meme, lol: {}".format(e))

        return None

    @commands.command(pass_context=True, no_pm=True)
    async def meme(self, ctx, *args : str):
        """Post a hot meme with top and bottom text.

            ex.: !meme <id>(optional) "top" "bot"
        """
        new_hot_meme = None
        is_valid = len(args) == 2 or len(args) == 3
        has_id_args = len(args) == 3

        if is_valid and has_id_args:
            new_hot_meme = await self._make_request(args[0], args[1], args[2])
        elif is_valid:
            new_hot_meme = await self._make_request(args[0], args[1])
        else:
            logger.error("[Meme] Command 'meme' needs 2 or 3 arguments({0} given)".format(len(args)))

        if new_hot_meme is not None:
            logger.info("[Meme] A new hot meme was made(author: {0}, url: {1})"
            .format(ctx.message.author.name, new_hot_meme))
            await self.bot.say(new_hot_meme)
        else:
            logger.error("[Meme] The new meme was not so hot(author: {0}, url: {1})"
            .format(ctx.message.author.name, new_hot_meme))


def setup(bot):
    bot.add_cog(Meme(bot))

memes = {
    "61579": "One Does Not Simply",
    "438680": "Batman Slapping Robin",
    "61532": "The Most Interesting Man In The World",
    "101470": "Ancient Aliens",
    "61520": "Futurama Fry",
    "347390": "X, X Everywhere",
    "5496396": "Leonardo Dicaprio Cheers",
    "61546": "Brace Yourselves X is Coming",
    "61539": "First World Problems",
    "16464531": "But Thats None Of My Business",
    "61527": "Y U No",
    "61582": "Creepy Condescending Wonka",
    "563423": "That Would Be Great",
    "61585": "Bad Luck Brian",
    "101288": "Third World Skeptical Kid",
    "61544": "Success Kid",
    "405658": "Grumpy Cat",
    "8072285": "Doge",
    "1509839": "Captain Picard Facepalm",
    "100947": "Matrix Morpheus",
    "1035805": "Boardroom Meeting Suggestion",
    "61533": "X All The Y",
    "245898": "Picard Wtf",
    "9440985": "Face You Make Robert Downey Jr",
    "14230520": "Black Girl Wat",
    "21735": "The Rock Driving",
    "259680": "Am I The Only One Around Here",
    "235589": "Evil Toddler",
    "40945639": "Dr Evil Laser",
    "61516": "Philosoraptor",
    "444501": "Maury Lie Detector",
    "61580": "Too Damn High",
    "97984": "Disaster Girl",
    "100955": "Confession Bear",
    "6235864": "Finding Neverland",
    "101287": "Third World Success Kid",
    "442575": "Aint Nobody Got Time For That",
    "109765": "Ill Just Wait Here",
    "61556": "Grandma Finds The Internet",
    "124212": "Say That Again I Dare You",
    "13757816": "Awkward Moment Sealion",
    "101711": "Skeptical Baby",
    "922147": "Laughing Men In Suits",
    "101440": "10 Guy",
    "101511": "Dont You Squidward",
    "12403754": "Bad Pun Dog",
    "101716": "Yo Dawg Heard You",
    "1790995": "And everybody loses their minds",
    "195389": "Sparta Leonidas",
    "61583": "Conspiracy Keanu",
    "61581": "Put It Somewhere Else Patrick",
    "718432": "Back In My Day",
    "766986": "Aaaaand Its Gone",
    "15878567": "You The Real MVP",
    "21604248": "Mugatu So Hot Right Now",
    "100952": "Overly Attached Girlfriend",
    "673439": "Confused Gandalf",
    "172314": "Kill Yourself Guy",
    "1367068": "I Should Buy A Boat Cat",
    "61522": "Scumbag Steve",
    "13424299": "Yall Got Any More Of",
    "228024": "Liam Neeson Taken",
    "389834": "Ryan Gosling",
    "1366993": "Spiderman Computer Desk",
    "11557802": "Rick and Carl",
    "61584": "Socially Awesome Awkward Penguin",
    "6531067": "See Nobody Cares",
    "10628640": "Archer",
    "17699": "Buddy Christ",
    "1232104": "Pepperidge Farm Remembers",
    "163573": "Imagination Spongebob",
    "17496002": "Leonardo Dicaprio Wolf Of Wall Street",
    "412211": "Jackie Chan WTF",
    "371382": "Simba Shadowy Place",
    "101462": "Ermahgerd Berks",
    "401687": "Buddy The Elf",
    "265789": "Kevin Hart The Hell",
    "409403": "Obi Wan Kenobi",
    "356615": "Peter Griffin News",
    "146381": "Angry Baby",
    "681831": "Gollum",
    "100948": "Sudden Clarity Clarence",
    "8774527": "So I Got That Goin For Me Which Is Nice",
    "176908": "Shut Up And Take My Money Fry",
    "23909796": "Satisfied Seal",
    "7761261": "Unpopular Opinion Puffin",
    "27920": "Surprised Koala",
    "19194965": "Star Wars No",
    "1202623": "Keep Calm And Carry On Red",
    "516587": "Look At All These",
    "306319": "Pissed Off Obama",
    "107773": "Spiderman Peter Parker",
    "18594762": "Brian Williams Was There",
    "646581": "I Too Like To Live Dangerously",
    "19209570": "What Do We Want",
    "460541": "Jack Sparrow Being Chased",
    "1232147": "Ron Burgundy",
    "53764": "Peter Parker Cry",
    "17258777": "Rick and Carl Long",
    "61554": "Dwight Schrute"
}
