import std
# from std.err import MagmaException
import os

path_cmd_registry = {}


@std.res.register(path_cmd_registry)
def pwd():
    print(os.getcwd())
    return 0


@std.res.register(path_cmd_registry)
def cd():
    # test command
    print("changed to D:\lol.py")
    return 0
