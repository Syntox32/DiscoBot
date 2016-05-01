import logging, os

class Config:
	"""
	Config class used by the the class `DiscoBot`
	"""
	VERSION = "0.4.0-beta"
	OWNER_ID = "88251130613604352"

	LOGGING_LEVEL = logging.DEBUG # DEBUG, INFO, WARNING, ERROR
	LOGGING_FORMAT = "%(asctime)s::%(name)s [%(levelname)s]: %(message)s"

	# Discord login
	DISCORD_TOKEN = os.environ.get("DISCOBOT_TOKEN", None)
	DISCORD_ID = os.environ.get("DISCOBOT_ID", None)

	# Imgflip login, used by `plugins/meme.py`
	# If these are not the the plugin will just be disabled
	IMGFLIP_PASS = os.environ.get("IMGFLIP_PASS", None)
	IMGFLIP_USER=  os.environ.get("IMGFLIP_USER", None)
