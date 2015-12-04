import logging
import os

# Setup logging

level = logging.INFO #DEBUG # INFO, WARNING, ERROR

log = logging.getLogger("discord")
log.setLevel(level)

handle = logging.FileHandler("discord.log", "w", "utf-8")
fmt = logging.Formatter("%(asctime)s::%(name)s[%(levelname)s]: %(message)s")

handle.setFormatter(fmt)
log.addHandler(handle)

# Get the login credentials

login_email = os.getenv("DISCOBOT_EMAIL")
login_pass = os.getenv("DISCOBOT_PASS")

if login_email is None or login_pass is None:
	log.critical("Could not retrieve login credentials from environment variable. Halting.")
	raise AttributeError("Environment variable DISCOBOT_PASS and/or DISCOBOT_EMAIL not set.")

creds = {
	"email": login_email,
	"pass": login_pass
}
