import std
from std.err import MagmaException
from std.res import register, create_option, create_choice
import os
import subprocess
from sys import platform

os_cmd_registry = {}


@register(os_cmd_registry)
def exit():
    return MagmaException('Process died.', 2)


@register(os_cmd_registry)
def ls():
    for i in os.listdir("./"):
        print(i)
    return 0


@register(os_cmd_registry)
def clear():
    if platform in ["linux", "linux2", "darwin"]:
        subprocess.run("clear", shell=True)
    elif platform == "win32":
        subprocess.run("cls", shell=True)
    else:
        return MagmaException(f"Unsupported command for \"{platform}\".", 1)
    return 0
