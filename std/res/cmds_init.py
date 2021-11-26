from std.err import MagmaException
from std.utils import type_checker, init_help_message


def register(cmds_registry: dict, options: list = None):
    def decorator(function):

        # Initialize command's help message
        if options:
            init_help_message(function, options)

        def wrapper(*args):

            if options:
                if not args:
                    print(function.__doc__)
                    return 0

                for option in options:
                    if args[0] == option["name"]:
                        try:
                            option["choices"] = option["option_type"](args[1])
                        except TypeError as e:
                            print(e)

                        return function(option=option)

                else:
                    return MagmaException(f"'{args[0]}' option not found.", 1)

            return function()

        cmds_registry[function.__name__] = wrapper
        return wrapper
    return decorator


def create_option(name: str, option_type, required: bool, choices: list = None) -> dict:
    type_checker([(name, str), (required, bool)])

    return {
        "name": name,
        "option_type": option_type,
        "required": required,
        "choices": choices
    }


def create_choice(name: str, value) -> dict:
    type_checker([(name, str)])

    return {
        "name": name,
        "value": value
    }
