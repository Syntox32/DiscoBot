# -*- coding: utf-8 -*-
"""
Holds the different errors that can occur
"""

class DiscoException(Exception):
    pass

class MissingCredentials(DiscoException):
    """
    Happens when the bot can't find any credentials to login with.
    """
    pass
