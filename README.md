# DiscoBot

A simple plugin-based bot for Discord using [discord.py](https://github.com/Rapptz/discord.py). https://discordapp.com/

Features
--------
- Plugin system
- It says `AYYLMAO` when you type `!sup` in a discord channel

Plugins
-------

Plugins are added in the file `disco/plugins/__init__.py` like this:

We want to add our plugin with classname `HelloWorld` in file `helloworld.py` as a plugin:

```
[...]

# Custom plugins
from .helloworld import HelloWorld

```

A template plugin can be found in `dicso/plugins/template.py`

An example plugin can be found in `dicso/plugins/helloworld.py` and `dicso/plugins/greetings.py`

Installation
------------

First set an environment variable containing the login credentials for the bot as such

### Linux/Unix
```
export DISCOBOT_LOGIN="<email>;<passwd>"
```

### Windows

In the windows environment variable editor:
	1. add a variable DISCOBOT_LOGIN
	2. give it the value `<email>;<passwd>`

**If you are on windows, make sure to run the program as admin**, or else python
can't retrieve the variable.

Then do the installation.

Download the project and navigate to the folder with `setup.py`. Then run 

```
python setup.py install
```

Start the bot by running `discobot start`.

Development
-----------
Make sure you have `Python 2.7.x` installed.

Run `pip install -r requirements.txt` in the top-directory.

Start the bot with `python main.py`

Requirements
------------
The project requires *Python 2.7.x* to be installed

You will also have intall [discord.py](https://github.com/Rapptz/discord.py) by Rapptz. This can be done by doing `pip install discord.py`

License
-------
The whole project is licensed under an MIT license.