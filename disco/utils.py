# -*- coding: utf-8 -*-
"""
Utillity class with things
"""

import os, logging

from discord import Message

def get_destination(msg: Message):
    dest = None
    if msg.channel.is_private:
        dest  = 'Private Message'
    else:
        dest = '#{0.channel.name} ({0.server.name})'.format(msg)
    return dest

def configure_logger(name=__name__, stream=True, level=logging.INFO):
    """
    Function to quickly help you configure several loggers.

        ex.: `configure_logger("awesome-logger", False, logging.DEBUG)`
    """
    loginst = logging.getLogger(name)
    loginst.setLevel(logging.INFO if level is None else level)

    path = os.path.abspath(name + ".log")
    fhnd = logging.FileHandler(path, "w", "utf-8")
    shnd = logging.StreamHandler()

    log_fmt = "%(asctime)s::%(name)s [%(levelname)s]: %(message)s"
    fmt = logging.Formatter(log_fmt) # if log_format is None else log_format)
    fhnd.setFormatter(fmt)
    shnd.setFormatter(fmt)

    loginst.addHandler(fhnd)
    if stream: loginst.addHandler(shnd)

    return loginst
