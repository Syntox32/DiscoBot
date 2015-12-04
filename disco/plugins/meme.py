# -*- coding: utf-8 -*-
import logging
from .plugin import Plugin

import random, requests, urllib, os
from imgflip import PASS, USER

log = logging.getLogger("discord")

IMGFLIP_USER = os.getenv("IMGFLIP_USER")
IMGFLIP_PASS = os.getenv("IMGFLIP_PASS")

meme_names = [
"One Does Not Simply",
"Batman Slapping Robin",
"The Most Interesting Man In The World",
"Ancient Aliens",
"Futurama Fry",
"X, X Everywhere",
"Leonardo Dicaprio Cheers",
"Brace Yourselves X is Coming",
"First World Problems",
"But Thats None Of My Business",
"Y U No",
"Creepy Condescending Wonka",
"Bad Luck Brian",
"That Would Be Great",
"Success Kid",
"Third World Skeptical Kid",
"Grumpy Cat",
"Captain Picard Facepalm",
"Doge",
"Matrix Morpheus",
"Boardroom Meeting Suggestion",
"X All The Y",
"Picard Wtf",
"Face You Make Robert Downey Jr",
"Black Girl Wat",
"The Rock Driving",
"Am I The Only One Around Here",
"Evil Toddler",
"Dr Evil Laser",
"Philosoraptor",
"Maury Lie Detector",
"Too Damn High",
"Disaster Girl",
"Third World Success Kid",
"Finding Neverland",
"Confession Bear",
"Aint Nobody Got Time For That",
"Ill Just Wait Here",
"Grandma Finds The Internet",
"Say That Again I Dare You",
"Awkward Moment Sealion",
"Skeptical Baby",
"Dont You Squidward",
"Laughing Men In Suits",
"10 Guy",
"Yo Dawg Heard You",
"And everybody loses their minds",
"Bad Pun Dog",
"Sparta Leonidas",
"Conspiracy Keanu",
"Put It Somewhere Else Patrick",
"Back In My Day",
"Aaaaand Its Gone",
"Confused Gandalf",
"Kill Yourself Guy",
"Overly Attached Girlfriend",
"Scumbag Steve",
"Mugatu So Hot Right Now",
"You The Real MVP",
"I Should Buy A Boat Cat",
"Yall Got Any More Of",
"Liam Neeson Taken",
"Ryan Gosling",
"Spiderman Computer Desk",
"Rick and Carl",
"Socially Awesome Awkward Penguin",
"See Nobody Cares",
"Buddy Christ",
"Imagination Spongebob",
"Pepperidge Farm Remembers",
"Leonardo Dicaprio Wolf Of Wall Street",
"Archer",
"Ermahgerd Berks",
"Jackie Chan WTF",
"Simba Shadowy Place",
"Peter Griffin News",
"Kevin Hart The Hell",
"Sudden Clarity Clarence",
"Angry Baby",
"So I Got That Goin For Me Which Is Nice",
"Obi Wan Kenobi",
"Gollum",
"Shut Up And Take My Money Fry",
"Satisfied Seal",
"Star Wars No",
"Buddy The Elf",
"Surprised Koala",
"Unpopular Opinion Puffin",
"Brian Williams Was There",
"I Too Like To Live Dangerously",
"Spiderman Peter Parker",
"Keep Calm And Carry On Red",
"Pissed Off Obama",
"Rick and Carl Long",
"Ron Burgundy",
"Look At All These",
"What Do We Want",
"Peter Parker Cry",
"Jack Sparrow Being Chased",
"Dwight Schrute",
]

memes = ["61579","438680","61532","101470","61520","347390","5496396","61546","61539","16464531","61527","61582","563423","61585","101288","61544","405658","1509839","8072285","100947","1035805","61533","245898","9440985","14230520","21735","259680","235589","40945639","61516","444501","61580","97984","101287","6235864","100955","442575","109765","61556","124212","101711","13757816","922147","101511","101440","12403754","101716","1790995","195389","61583","61581","718432","766986","15878567","100952","172314","21604248","673439","1367068","61522","13424299","228024","389834","1366993","11557802","61584","6531067","17699","10628640","1232104","163573","17496002","101462","371382","412211","356615","409403","265789","401687","146381","100948","8774527","681831","176908","23909796","27920","19194965","7761261","18594762","1202623","516587","306319","107773","19209570","646581","17258777","1232147","61554","460541","53764"]

class Memes(Plugin):
	"""
	Plugin template class

	API reference here:
		http://rapptz.github.io/discord.py/api.html#
	"""

	title = "Such memes, much plugin"
	desc = "What is my purpose?"
	commands = [ "!lenny", "!memelist", "!meme <id>(optional) <quote> <quote>" ]

	def __init__(self): pass
	def on_ready(self, client): pass

	def _request_meme(self, top, bot, tem_id=None):
		meme = ""
		if tem_id is not None and tem_id >= 0 and tem_id <= len(memes):
			meme = memes[tem_id]
		else:
			rand = random.randint(0, len(memes))
			meme = memes[rand]
		try:
			r = requests.post("https://api.imgflip.com/caption_image",
				data = {
					"template_id": meme, 
					"text0": top, 
					"text1": bot,
					"username": IMGFLIP_USER,
					"password": IMGFLIP_PASS
				})
			succ = bool(r.json()["success"])
			if succ:
				print r.json()["data"]["url"]
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
			meme = ""
			for i, m in enumerate(meme_names):
				meme += str(i) + ": " + m + "\n"
				if i == int(len(memes) / 2):
					client.send_message(message.author, meme)
					meme = ""
			client.send_message(message.author, meme)
		elif message.content.startswith("!meme"):
			"""
			Returns an image url with a meme given top and bot text

			!meme <id>(optional) <quote> <quote>
			"""
			try:
				sp = message.content.split("\"")
				tem_id = None

				# if we are given an id, use it
				if len(sp[0].split(" ")) > 1 and sp[0].split(" ")[1] != "":
						tem_id = int(sp[0].split(" ")[1])

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
