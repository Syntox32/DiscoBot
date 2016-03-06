# -*- coding: utf-8 -*-
"""
DiscoBot the Amazing Chat Companion
"""

from .config import Config
from .discobot import DiscoBot
from .utils import configure_logger

# Configure logging
configure_logger("disco", level=Config.LOGGING_LEVEL)
# Setup log-to-file-only for the discord.py logger
configure_logger("discord", stream=False, level=Config.LOGGING_LEVEL)
