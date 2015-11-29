from setuptools import setup

setup(
	name="DiscoBot",
	version="0.1.0",
	description="A simple plugin-based bot for Discord",
	author="syntox",
	author_email="syntox32@gmail.com",
	url="https://github.com/syntox32/discobot",
	packages=["disco"],
	scripts=["bin/run.sh"]
)