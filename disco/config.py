import logging
import os

# Setup logging

level = logging.DEBUG # INFO, WARNING, ERROR

log = logging.getLogger("discord")
log.setLevel(level)

handle = logging.FileHandler("discord.log", "w", "utf-8")
fmt = logging.Formatter("%(asctime)s::%(name)s[%(levelname)s]: %(message)s")

handle.setFormatter(fmt)
log.addHandler(handle)

# Get the login credentials

login = os.getenv("DISCOBOT_LOGIN")
if login is None:
	log.critical("Could not retrieve login credentials from environment variable. Halting.")
	raise AttributeError("Environment variable DISCOBOT_LOGIN not set.")

login = login.split(";")

creds = {
	"email": login[0],
	"pass": login[1]
}
