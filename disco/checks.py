# -*- coding: utf-8 -*-
"""
Checks, yeah
"""

from discord.ext import commands

def is_owner_check(message):
    return message.author.id == ""

def is_owner():
    return commands.check(lambda ctx: is_owner_check(ctx.message))
