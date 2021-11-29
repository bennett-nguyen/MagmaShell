from std.err import MagmaException
from std.utils import GlobalUtils, CmdsInitUtils


def register(cmds_registry: dict, options: list = None):
    def decorator(function):

        if options:
            CmdsInitUtils.duplicate_checker(function, options)
            CmdsInitUtils.init_help_message(function, options)

        def wrapper(*args):

            return CmdsInitUtils.option_parser(function, args, options)

        cmds_registry[function.__name__] = wrapper
        return wrapper
    return decorator


def create_option(name: str, option_type, choices: list = None) -> dict:
    if choices is None:
        choices = []

    GlobalUtils.type_checker([(name, str), (choices, list)])

    return {
        "name": " ".join(name.strip().split()).replace(" ", "-"),
        "option_type": option_type,
        "choices": choices
    }


def create_choice(name: str, value) -> dict:
    GlobalUtils.type_checker([(name, str)])

    return {
        "name": " ".join(name.strip().split()).replace(" ", "-"),
        "value": value
    }
