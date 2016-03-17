# -*- coding: utf-8 -*-

import logging, random, json

from disco.config import Config
from discord import Message, Channel, Member, Server, Role, VoiceClient
from discord.ext import commands
from discord import utils, opus

logger = logging.getLogger("disco")

class Music:

    def __init__(self, bot):
        self.bot = bot
        self.key = self.__class__.__name__
        self.follow = True
        self.vclients = {}

    async def join_owner_on_server(self, server):
        """Given a server, seek out the owner and join
        the current voice channel he is in, if it exists.
        """
        member = utils.get(server.members, id=Config.OWNER_ID)
        if member is not None:
            logger.debug("Found member: {}".format(member.name))
            vchan = member.voice_channel
            if vchan is not None:
                logger.info("Joining voice channel: {}".format(vchan.name))
                if server.id not in self.vclients:
                    logger.debug("Creating voice client with ID: {}".format(server.id))
                    self.vclients.update({ server.id: { "client": None, "player": None }})
                self.vclients[server.id]["client"] = await self.bot.join_voice_channel(vchan)
                logger.debug("Voice connectd: {}".format(self.vclients[server.id]["client"].is_connected()))
            else:
                logger.debug("No voice channel found.")
        else:
            logger.debug("Member not found.")

    @commands.command(name="follow", pass_context=True, no_pm=True, aliases=[])
    async def follow_owner(self, ctx):
        await self.join_owner_on_server(ctx.message.server)

    async def on_ready(self):
        logger.info("Opus loaded: {}".format(opus.is_loaded()))

        if self.follow:
            logger.info("Follow enabled.")
            for server in self.bot.servers:
                await self.join_owner_on_server(server)

    @commands.command(pass_context=True, no_pm=True, aliases=[])
    async def play(self, ctx, url : str):
        voice = self.vclients[ctx.message.server.id]
        voice["player"] = await voice["client"].create_ytdl_player(url) #"https://www.youtube.com/watch?v=N9qYF9DZPdw")
        voice["player"].start()

    @commands.command(pass_context=True, no_pm=True, aliases=[])
    async def stop(self, ctx):
        voice = self.vclients[ctx.message.server.id]
        voice["player"].stop()

    @commands.command(pass_context=True, no_pm=True, aliases=["q", "que"])
    async def queue(self, ctx, url : str):
        voice = self.vclients[ctx.message.server.id]
        player = voice["player"]
        if player.is_playing():
            player.stop()
            logger.debug("Stopping player in progress")
        voice["player"] = await voice["client"].create_ytdl_player(url)
        voice["player"].start()

def setup(bot):
    bot.add_cog(Music(bot))
