import std
import os

path_cmds_registry = {}

@std.res.register(path_cmds_registry)
def pwd():
	print(os.getcwd())
	return [0, None]
