import std
import os
import subprocess
from sys import platform

os_cmds_registry = {}


@std.res.register(os_cmds_registry)
def exit():
    return 2, std.err.MagmaException(None, 'Process died.')


# add ast to this
@std.res.register(os_cmds_registry, options = [
	std.res.create_option(
		name = "path",
		option_type = str,
		required = False
	)
])
def ls(options):
	for i in os.listdir("./"):
		print(i)
	return 0, None

@std.res.register(os_cmds_registry)
def clear():
	if platform in ["linux", "linux2", "darwin"]:
		subprocess.run("clear", shell=True)
	elif platform == "win32":
		subprocess.run("cls", shell=True)
	else:
		return 1, std.err.MagmaException(None, f"Unsupported command for \"{platform}\".")
	return 0, None