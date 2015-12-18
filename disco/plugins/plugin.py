# a simple Python plugin loading system
# see https://gist.github.com/will-hart/5899567
#
# Modified to work with Python 3
#

class PluginMount(type):
	"""
	A plugin mount point derived from:
		http://martyalchin.com/2008/jan/10/simple-plugin-framework/
		
	Acts as a metaclass which creates anything inheriting from Plugin
	"""

	def __init__(cls, name, bases, nmspc):
		if not hasattr(cls, "plugins"):
			cls.plugins = []
		else:
			cls.plugins.append(cls)

class Plugin(object, metaclass=PluginMount):
	title = "__pluginbase__"
