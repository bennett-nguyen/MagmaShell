from std_cmds.registry import registered_cmds
import sys
import os
from std.err import MagmaException

libs = [os.path.join(os.getcwd(), directory)
        for directory in ["std"]]

sys.path.extend(libs)


def process(user_in):
    cmd = user_in.split(" ")

    if cmd[0] not in registered_cmds:
        return MagmaException(f"{cmd[0]}: command not found", 1)

    exit_code = registered_cmds[cmd[0]]()

    if exit_code is None:
        return MagmaException(f'Expected "{cmd[0]}" to return an exit code but None was returned.', 2)
    
    return exit_code
