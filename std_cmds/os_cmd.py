import std
import os
import subprocess
from sys import platform

os_cmds_registry = {}


@std.res.register(os_cmds_registry)
def exit():
    return 2, std.err.MagmaException(None, 'Process died.')

@std.res.register(os_cmds_registry)
def ls():
	for i in os.listdir("./"):
		print(i)
	return 0, None

@std.res.register(os_cmds_registry)
def clear():
	if platform in ["linux", "linux2", "darwin"]:
		print("system:")
		os.system("clear")
	elif platform == "win32":
		print("system:")
		os.system("cls")
	else:
		return 1, std.err.MagmaException(None, f"Unsupported command for \"{platform}\".")
	return 0, None