# -*- coding: utf-8 -*-
import logging
from .plugin import Plugin
import random, requests, urllib, os

log = logging.getLogger("discord")

IMGFLIP_USER = os.getenv("IMGFLIP_USER")
IMGFLIP_PASS = os.getenv("IMGFLIP_PASS")


class Memes(Plugin):
	"""
	Plugin template class

	API reference here:
		http://rapptz.github.io/discord.py/api.html#
	"""

	title = "Such memes, much plugin"
	desc = "What is my purpose?"

	commands = [
		"!lenny :: prints a lenny face, because",
		"!memelist :: lists all memes available by id",
		"!meme <id>(optional) <quote> <quote> :: make a dank meme"
		]

	def __init__(self): pass
	def on_ready(self, client):
		self.imgflip_login = True

		if IMGFLIP_PASS is None or IMGFLIP_USER is None:
			err_msg = "Heads up, environment variable IMGFLIP_USER and IMGFLIP_PASS" + \
				" is not set for plugin 'Memes'.\n\nYou will not be able do make dank memes before" + \
				" these have been configured, master."
			print err_msg
			log.warning(err_msg)
			self.imgflip_login = False

	def _request_meme(self, top, bot, tem_id=None):
		meme = ""
		if tem_id is not None and tem_id >= 0 and tem_id <= len(meme_list):
			meme = meme_list[tem_id]
		else:
			rand = random.randint(0, len(meme_list))
			meme = meme_list[rand]
		try:
			r = requests.post("https://api.imgflip.com/caption_image",
				data = {
					"template_id": meme["id"], 
					"text0": top, 
					"text1": bot,
					"username": IMGFLIP_USER,
					"password": IMGFLIP_PASS
				})
			succ = bool(r.json()["success"])
			if succ:
				# print r.json()["data"]["url"]
				return r.json()["data"]["url"]
			else:
				return None
		except Exception, e:
			log.exception(e)
			return None

	def on_message(self, client, message):

		if message.content.startswith("!memelist"):
			"""
			Sends a direct message to the author with a list of
			all the available memes
			"""
			output = ""
			meme_len = len(meme_list)
			
			for i in range(0, meme_len):
				output += "dbg %d: %s\n" % (i + 1, meme_list[i]["name"])
				if i == int(meme_len / 2):
					client.send_message(message.author, output)
					output = ""
			client.send_message(message.author, output)

		elif message.content.startswith("!meme"):
			"""
			Returns an image url with a meme given top and bot text
			"""
			if not self.imgflip_login:
				# can't make dank memes without an account
				client.send_message(message.author, "You need to configure imgflip to do that.")
				return

			try:
				sp = message.content.split("\"")
				tem_id = None

				# if we are given an id, use it
				if len(sp[0].split(" ")) > 1 and sp[0].split(" ")[1] != "":
						tem_id = int(sp[0].split(" ")[1]) - 1

				top = sp[1]
				bot = sp[3]
				url = self._request_meme(top, bot, tem_id)
				if url is None:
					client.send_message(message.channel, "Something went wrong, check the logs, master")
				else:
					client.send_message(message.channel, url)
			except Exception, e:
				log.exception(e)

		elif message.content.startswith("!lenny"):
			"""
			Prints a lenny face, cause I can
			"""
			client.send_message(message.channel, "( ͡° ͜ʖ ͡°)")
			

meme_list = [{
				"id": "61579",
				"name": "One Does Not Simply"
			}, {
				"id": "438680",
				"name": "Batman Slapping Robin"
			}, {
				"id": "61532",
				"name": "The Most Interesting Man In The World"
			}, {
				"id": "101470",
				"name": "Ancient Aliens"
			}, {
				"id": "61520",
				"name": "Futurama Fry"
			}, {
				"id": "347390",
				"name": "X, X Everywhere"
			}, {
				"id": "5496396",
				"name": "Leonardo Dicaprio Cheers"
			}, {
				"id": "61546",
				"name": "Brace Yourselves X is Coming"
			}, {
				"id": "61539",
				"name": "First World Problems"
			}, {
				"id": "16464531",
				"name": "But Thats None Of My Business"
			}, {
				"id": "61527",
				"name": "Y U No"
			}, {
				"id": "61582",
				"name": "Creepy Condescending Wonka"
			}, {
				"id": "563423",
				"name": "That Would Be Great"
			}, {
				"id": "61585",
				"name": "Bad Luck Brian"
			}, {
				"id": "101288",
				"name": "Third World Skeptical Kid"
			}, {
				"id": "61544",
				"name": "Success Kid"
			}, {
				"id": "405658",
				"name": "Grumpy Cat"
			}, {
				"id": "8072285",
				"name": "Doge"
			}, {
				"id": "1509839",
				"name": "Captain Picard Facepalm"
			}, {
				"id": "100947",
				"name": "Matrix Morpheus"
			}, {
				"id": "1035805",
				"name": "Boardroom Meeting Suggestion"
			}, {
				"id": "61533",
				"name": "X All The Y"
			}, {
				"id": "245898",
				"name": "Picard Wtf"
			}, {
				"id": "9440985",
				"name": "Face You Make Robert Downey Jr"
			}, {
				"id": "14230520",
				"name": "Black Girl Wat"
			}, {
				"id": "21735",
				"name": "The Rock Driving"
			}, {
				"id": "259680",
				"name": "Am I The Only One Around Here"
			}, {
				"id": "235589",
				"name": "Evil Toddler"
			}, {
				"id": "40945639",
				"name": "Dr Evil Laser"
			}, {
				"id": "61516",
				"name": "Philosoraptor"
			}, {
				"id": "444501",
				"name": "Maury Lie Detector"
			}, {
				"id": "61580",
				"name": "Too Damn High"
			}, {
				"id": "97984",
				"name": "Disaster Girl"
			}, {
				"id": "100955",
				"name": "Confession Bear"
			}, {
				"id": "6235864",
				"name": "Finding Neverland"
			}, {
				"id": "101287",
				"name": "Third World Success Kid"
			}, {
				"id": "442575",
				"name": "Aint Nobody Got Time For That"
			}, {
				"id": "109765",
				"name": "Ill Just Wait Here"
			}, {
				"id": "61556",
				"name": "Grandma Finds The Internet"
			}, {
				"id": "124212",
				"name": "Say That Again I Dare You"
			}, {
				"id": "13757816",
				"name": "Awkward Moment Sealion"
			}, {
				"id": "101711",
				"name": "Skeptical Baby"
			}, {
				"id": "922147",
				"name": "Laughing Men In Suits"
			}, {
				"id": "101440",
				"name": "10 Guy"
			}, {
				"id": "101511",
				"name": "Dont You Squidward"
			}, {
				"id": "12403754",
				"name": "Bad Pun Dog"
			}, {
				"id": "101716",
				"name": "Yo Dawg Heard You"
			}, {
				"id": "1790995",
				"name": "And everybody loses their minds"
			}, {
				"id": "195389",
				"name": "Sparta Leonidas"
			}, {
				"id": "61583",
				"name": "Conspiracy Keanu"
			}, {
				"id": "61581",
				"name": "Put It Somewhere Else Patrick"
			}, {
				"id": "718432",
				"name": "Back In My Day"
			}, {
				"id": "766986",
				"name": "Aaaaand Its Gone"
			}, {
				"id": "15878567",
				"name": "You The Real MVP"
			}, {
				"id": "21604248",
				"name": "Mugatu So Hot Right Now"
			}, {
				"id": "100952",
				"name": "Overly Attached Girlfriend"
			}, {
				"id": "673439",
				"name": "Confused Gandalf"
			}, {
				"id": "172314",
				"name": "Kill Yourself Guy"
			}, {
				"id": "1367068",
				"name": "I Should Buy A Boat Cat"
			}, {
				"id": "61522",
				"name": "Scumbag Steve"
			}, {
				"id": "13424299",
				"name": "Yall Got Any More Of"
			}, {
				"id": "228024",
				"name": "Liam Neeson Taken"
			}, {
				"id": "389834",
				"name": "Ryan Gosling"
			}, {
				"id": "1366993",
				"name": "Spiderman Computer Desk"
			}, {
				"id": "11557802",
				"name": "Rick and Carl"
			}, {
				"id": "61584",
				"name": "Socially Awesome Awkward Penguin"
			}, {
				"id": "6531067",
				"name": "See Nobody Cares"
			}, {
				"id": "10628640",
				"name": "Archer"
			}, {
				"id": "17699",
				"name": "Buddy Christ"
			}, {
				"id": "1232104",
				"name": "Pepperidge Farm Remembers"
			}, {
				"id": "163573",
				"name": "Imagination Spongebob"
			}, {
				"id": "17496002",
				"name": "Leonardo Dicaprio Wolf Of Wall Street"
			}, {
				"id": "412211",
				"name": "Jackie Chan WTF"
			}, {
				"id": "371382",
				"name": "Simba Shadowy Place"
			}, {
				"id": "101462",
				"name": "Ermahgerd Berks"
			}, {
				"id": "401687",
				"name": "Buddy The Elf"
			}, {
				"id": "265789",
				"name": "Kevin Hart The Hell"
			}, {
				"id": "409403",
				"name": "Obi Wan Kenobi"
			}, {
				"id": "356615",
				"name": "Peter Griffin News"
			}, {
				"id": "146381",
				"name": "Angry Baby"
			}, {
				"id": "681831",
				"name": "Gollum"
			}, {
				"id": "100948",
				"name": "Sudden Clarity Clarence"
			}, {
				"id": "8774527",
				"name": "So I Got That Goin For Me Which Is Nice"
			}, {
				"id": "176908",
				"name": "Shut Up And Take My Money Fry"
			}, {
				"id": "23909796",
				"name": "Satisfied Seal"
			}, {
				"id": "7761261",
				"name": "Unpopular Opinion Puffin"
			}, {
				"id": "27920",
				"name": "Surprised Koala"
			}, {
				"id": "19194965",
				"name": "Star Wars No"
			}, {
				"id": "1202623",
				"name": "Keep Calm And Carry On Red"
			}, {
				"id": "516587",
				"name": "Look At All These"
			}, {
				"id": "306319",
				"name": "Pissed Off Obama"
			}, {
				"id": "107773",
				"name": "Spiderman Peter Parker"
			}, {
				"id": "18594762",
				"name": "Brian Williams Was There"
			}, {
				"id": "646581",
				"name": "I Too Like To Live Dangerously"
			}, {
				"id": "19209570",
				"name": "What Do We Want"
			}, {
				"id": "460541",
				"name": "Jack Sparrow Being Chased"
			}, {
				"id": "1232147",
				"name": "Ron Burgundy"
			}, {
				"id": "53764",
				"name": "Peter Parker Cry"
			}, {
				"id": "17258777",
				"name": "Rick and Carl Long"
			}, {
				"id": "61554",
				"name": "Dwight Schrute"
			}]