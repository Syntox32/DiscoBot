# -*- coding: utf-8 -*-
"""
Hold different mixin classes.
"""

import logging

logger = logging.getLogger("disco")

class CogMixin:
	"""
	Class for adding key prefixing to log messages, other
	shared functionality might be also be put here.
	"""
	def __init__(self):
		self.key = self.__class__.__name__

	def prefix_key(self, msg):
		return "[{0}] {1}".format(self.__class__.__name__, msg)

	def info(self, msg, *args, **kwargs):
		logger.info(self.prefix_key(msg), *args, **kwargs)

	def debug(self, msg, *args, **kwargs):
		logger.debug(self.prefix_key(msg), *args, **kwargs)

	def warning(self, msg, *args, **kwargs):
		logger.warning(self.prefix_key(msg), *args, **kwargs)

	def error(self, msg, *args, **kwargs):
		logger.error(self.prefix_key(msg), *args, **kwargs)
