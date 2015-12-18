# DiscoBot

A simple plugin-based bot for Discord using [discord.py](https://github.com/Rapptz/discord.py) API Wrapper. 

If you have no clue what Discord is you can go here: https://discordapp.com/

## Features

- Expandable plugin system
- Included commands are, but is not limited to:  
	`!hot <subreddit>` - posts a hot post from a subreddit  
	`!meme "<toptext>" "<bottext>"` - posts a hot meme with the given text  
	`!fuckoff` - tells you to fuck off  
 
## Plugins

Plugins are added in the file `disco/plugins/__init__.py` like this:

We want to add our plugin with classname `HelloWorld` in file `helloworld.py` as a plugin:

```
[...]

## Custom plugins
from .helloworld import HelloWorld

```

A template plugin can be found in `dicso/plugins/template.py`

An example plugin can be found in `dicso/plugins/helloworld.py` and `dicso/plugins/greetings.py`

You can also read through the other included plugins.

Since the plugins use the [discord.py](https://github.com/Rapptz/discord.py) API Wrapper you can get all the
documentation you need by going to that repo.

## Configuring

Pretty much all credentials is configured by environment variables.

Here is a table of the current environment variables that you need to set on your system.

Name | Value | Type | Plugin
--- | --- | --- | ---
**DISCOBOT_EMAIL** | Discord email | Required | 
**DISCOBOT_PASS** | Discord password | Required | 
**IMGFLIP_USER** | [ImgFlip](https://imgflip.com/) username | Optional | meme.py
**IMGFLIP_PASS** | [ImgFlip](https://imgflip.com/) password | Optional | meme.py

## Installation

#### Option one
If you have pip working and installed, it's pretty straight forward.

```
pip install git+https://github.com/Syntox32/DiscoBot
```

#### Option two

Download the project in some way (.zip or git), `cd` to the directory and run.

```
python setup.py install
```
---

You can now run the script by typing this in the console of your choice.
```
disco.py
```

## Development

Make sure you have `Python 3.4.2+` installed.

Run `pip install -r requirements.txt` in the top-directory.

Start the bot with `python main.py`

## Requirements

The project requires *Python 3.4.2+* to be installed

You also need to install all the requirements 
```
pip install -r requirements.txt
```

## License

The whole project is licensed under an MIT license.
