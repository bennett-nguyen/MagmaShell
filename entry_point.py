from PyMShell import process
import std.err as err
# One of these are returned after the command is done executing or during execution to mark if the command exit failed or succeed
# exit_failed = 1
# kill_process_after_exception = 2
# exit_succeed = 0

try:
	while True:
		user_input = input(">>> ")
		
		if not user_input:
			continue
			
		entry_exit_code = process(user_input)

		if entry_exit_code[0] == 1:
			print("\n" + entry_exit_code[1].errors)
		elif entry_exit_code[0] == 2:
			print("\n" + entry_exit_code[1].errors)
			break

except KeyboardInterrupt:
	print("\nExited the program.")