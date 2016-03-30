# -*- coding: utf-8 -*-
"""
Utillity class with things
"""

import os, io, logging
import asyncio, aiohttp

from discord import Message
from discord.ext import commands

logger = logging.getLogger("disco")


def get_destination(msg: Message):
    dest = None
    if msg.channel.is_private:
        dest  = 'Private Message'
    else:
        dest = '#{0.channel.name} ({0.server.name})'.format(msg)
    return dest

def get_channel_permissions(ctx):
    return ctx.message.channel.permissions_for(ctx.message.author)

def can_attach_links(ctx):
    """Check if the user can upload files in the given context"""
    permissions = get_channel_permissions(ctx)
    return permissions.attach_files

async def try_embed_image(bot: commands.Bot, ctx, url: str, content=None):
    """
    Embeds an image in a message. If it can't embed
    you the url file, it will just do the normal bot.say
    """
    try:
        logger.debug("[embed image] {}".format(url))
        can_send_file = can_attach_links(ctx)
        logger.debug("can_send_file: {}".format(str(can_send_file)))
        if can_send_file:
            with aiohttp.ClientSession() as session:
                async with session.request(url=url, method="GET") as resp:
                    with io.BytesIO(await resp.read()) as f:
                        await bot.send_file(ctx.message.channel, f, filename=url, content=content)
        else:
            logger.debug("[embed image] warning: cannot attach files in this channel")
            if content is None:
                await bot.say(url)
            else:
                await bot.say("{0} {1}".format(str(content), url))
    except Exception as e:
        logger.warning("Could not embed image, error: {}".format(e))

def configure_logger(name=__name__, stream=True, level=logging.INFO):
    """
    Function to quickly help you configure several loggers.

        ex.: `configure_logger("awesome-logger", False, logging.DEBUG)`
    """
    loginst = logging.getLogger(name)
    loginst.setLevel(logging.INFO if level is None else level)

    path = os.path.abspath(name + ".log")
    #fhnd = logging.FileHandler(path, "w", "utf-8")
    shnd = logging.StreamHandler()
    rhnd = logging.RotatingFileHandler(path, mode="a", maxBytes=10000000,
        backupCount=10, encoding="utf-8")

    log_fmt = "%(asctime)s::%(name)s [%(levelname)s]: %(message)s"
    fmt = logging.Formatter(log_fmt) # if log_format is None else log_format)
    #fhnd.setFormatter(fmt)
    shnd.setFormatter(fmt)
    rhnd.setFormatter(fmt)

    #loginst.addHandler(fhnd)
    loginst.addHandler(rhnd)
    if stream: loginst.addHandler(shnd)

    return loginst
