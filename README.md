
# DiscoBot
A small pluggable bot for Discord using [discord.py](https://github.com/Rapptz/discord.py).

If you have no clue what Discord is you can go here: https://discordapp.com/


## Installation

```
<install python3.5>
sudo apt-get install libffi-dev python3.5-dev supervisor python-virtualenv
```

Linux is currently the only tested environment.

The bot needs *Python >= v3.5.1* to be able to run, due to the use of `asyncio`.

It's recommended you also use a virtual environment when installing dependencies:
```
$ virtualenv -p python3.5 venv --always-copy
$ source ./venv/bin/activate
```

You also need to install all the requirements

```
$ pip install -r requirements.txt
```

Then run the bot:
```
$ python main.py
```

## Keeping it online

If you want to run your bot online 24/7 you might consider setting up a [supervisor](http://supervisord.org/) config.
If you do end up using supervisor, it's worth noting you **must set the credentials inside
the config**.

A sample supervisor config file can be found togheter with this repo.

## License

The whole project is licensed under an MIT license.
