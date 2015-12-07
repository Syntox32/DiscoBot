from setuptools import setup
from disco.config import version

lines = []
with open("requirements.txt") as f:
	lines = f.read().splitlines()
	
# Remove comments and empty lines
reqs = [s for s in lines if not s.startswith("#") and s != ""]

setup(
	author="syntox",
	author_email="syntox32@gmail.com",
	url="https://github.com/syntox32/discobot",
	
	name="DiscoBot",
	packages=["disco"],
	version=version,
	description="A simple plugin-based bot for Discord",
	
	install_requires=reqs,
	include_package_data=True,
	scripts=["scripts/disco.py"]
)