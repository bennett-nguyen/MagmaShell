from PyMShell import process

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

        if type(entry_exit_code) is int and not entry_exit_code or not entry_exit_code.show_error:
            continue

        match entry_exit_code.exit_status:
            case 0:
                continue
            case 1:
                print(entry_exit_code.errors)
            case 2:
                print(entry_exit_code.errors)
                break

except KeyboardInterrupt:
    print("\nExited the program.")
