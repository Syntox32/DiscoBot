import discord, os, sys
import logging

log = logging.getLogger("discord")
log.setLevel(logging.DEBUG)

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
log.addHandler(handler)

creds = os.getenv("SLUTBOT_LOGIN")
if creds is None:
	log.critical("Could not retrieve login credentials from environment variable. Halting.")
	raise AttributeError("Environment variable SLUTBOT_LOGIN not set.")

login = {
	"email": creds.split(";")[0],
	"pass": creds.split(";")[1]
}

#login = os.getenv("SLUTBOT_LOGIN").split(";")
#EMAIL = login[0] #os.getenv("SLUTBOT_EMAIL")
#PASS = login[1] #os.getenv("SLUTBOT_PASS")