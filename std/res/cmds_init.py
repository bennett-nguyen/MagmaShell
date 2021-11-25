from std.err import MagmaException
# TODO: add user-specific options
# NOTE: This decoractor helps creating shell cmds, required one more args


def register(cmds_registry: dict, options: list = None):
    def decorator(function):

        if options:

            help_var = ""
            index = 0

            # Initialize command's help message
            for option in options:
                help_var = f"{help_var}\n{option['name']} {[choice for choice in option['choices']]}"
                index += 1

            function.__doc__ = f'{function.__name__}:\n' + help_var

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

    return {
        "name": name,
        "option_type": option_type,
        "required": required,
        "choices": choices
    }


def create_choice(name, value) -> dict:
    return {
        "name": name,
        "value": value
    }
