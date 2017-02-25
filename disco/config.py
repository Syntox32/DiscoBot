import logging, os, json

class Config:
	"""
	Config class used by the the class `DiscoBot`
	"""
	OWNER_ID = "88251130613604352"

	LOGGING_LEVEL = logging.DEBUG # DEBUG, INFO, WARNING, ERROR
	LOGGING_FORMAT = "%(asctime)s::%(name)s [%(levelname)s]: %(message)s"

	use_cred_file = True
	if os.path.exists("creds.json"):
		with open("creds.json", "r") as f:
			creds = json.load(f)
		if "_use_me" in creds:
			use_cred_file = creds["_use_me"]


	if os.path.exists("creds.json") and use_cred_file:
		print("Found file 'creds.json', using this instead of environment variables")

		with open("creds.json", "r") as f:
			creds = json.load(f)

		#if "owner_id" in creds:
		#	OWNER_ID = creds["owner_id"]

		DISCORD_TOKEN = creds.get("token", None)

		# Imgflip login, used by `plugins/meme.py`
		# If these are not the the plugin will just be disabled
		IMGFLIP_PASS = creds.get("imgflip_pass", None)
		IMGFLIP_USER=  creds.get("imgflip_user", None)

		R_ID  = creds.get("reddit_id", None)
		R_SEC = creds.get("reddit_pass", None)
		R_USR = creds.get("reddit_user", None)
		R_TOK = creds.get("reddit_token", None)

	else:
		# Discord login
		DISCORD_TOKEN = os.environ.get("DISCO_TOKEN", None)

		#OWNER_ID = os.environ.get("DISCO_OWNER", OWNER_ID)

		# Imgflip login, used by `plugins/meme.py`
		# If these are not the the plugin will just be disabled
		IMGFLIP_PASS = os.environ.get("IMGFLIP_PASS", None)
		IMGFLIP_USER=  os.environ.get("IMGFLIP_USER", None)

		R_ID  = os.environ.get("R_ID", None)
		R_SEC = os.environ.get("R_SEC", None)
		R_USR = os.environ.get("R_USR", None)
		R_TOK = os.environ.get("R_TOK", None)
