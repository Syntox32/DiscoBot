import logging, os

class Config:
	"""
	Config class used by the the class `DiscoBot`
	"""
	OWNER_ID = "88251130613604352"

	LOGGING_LEVEL = logging.DEBUG # DEBUG, INFO, WARNING, ERROR
	LOGGING_FORMAT = "%(asctime)s::%(name)s [%(levelname)s]: %(message)s"

	# Discord login
	DISCORD_TOKEN = os.environ.get("DISCO_TOKEN", None)

	# Imgflip login, used by `plugins/meme.py`
	# If these are not the the plugin will just be disabled
	IMGFLIP_PASS = os.environ.get("IMGFLIP_PASS", None)
	IMGFLIP_USER=  os.environ.get("IMGFLIP_USER", None)

	R_ID  = os.environ.get("R_ID", None)
	R_SEC = os.environ.get("R_SEC", None)
	R_USR = os.environ.get("R_USR", None)
	R_TOK = os.environ.get("R_TOK", None)
