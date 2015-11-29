# a simple Python plugin loading system
# see https://gist.github.com/will-hart/5899567

class PluginMount(type):
	"""
	A plugin mount point derived from:
		http://martyalchin.com/2008/jan/10/simple-plugin-framework/
		
	Acts as a metaclass which creates anything inheriting from Plugin
	"""
	def __init__(cls, name, bases, attrs):
		if not hasattr(cls, "plugins"):
			cls.plugins = []
		else:
			cls.register_plugin(cls)

	def register_plugin(cls, plugin):
		instance = plugin()
		cls.plugins.append(instance)

class Plugin(object):
	__metaclass__ = PluginMount
