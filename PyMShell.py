import sys
import os
import std

libs = [os.path.join(os.getcwd(), directory) for directory in ["std", "std_cmds"]]

sys.path.extend(libs)

from std_cmds.register import registered_cmds

def process(user_in):
	cmd = user_in.split(" ")
    
	if cmd[0] not in registered_cmds:
		return 1, std.err.MagmaException(None, f"{cmd[0]}: command not found")

	exit_code = registered_cmds[cmd[0]]()

	if len(exit_code) != 2:
		return 2, std.err.MagmaException(None, f"\"{cmd[0]}\" command only accept exit code's length of 2 but {len(exit_code)} was given.")
	
	if type(exit_code[0]) is not int or exit_code[0] not in [0, 1, 2]:
		return 2, std.err.MagmaException(None, f"Invalid exit code of \"{cmd[0]}\" command.\n\nExpected: [exit status (0-2), Exception's name]\nGiven exit code: {exit_code}")

	if not exit_code[0] and exit_code[1] is not None:
		return 2, std.err.MagmaException(None, f"{cmd[0]} returned an exception while the exit status is \"0\".") 
	
	return exit_code


		