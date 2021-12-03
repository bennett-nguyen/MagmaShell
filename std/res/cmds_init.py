from std.err import MagmaException
from std.utils import GlobalUtils, CmdsInitUtils


def register(cmds_registry: dict, options: list = None):
    def decorator(function):

        if options:
            CmdsInitUtils.option_inspector(function, options)
            CmdsInitUtils.init_help_message(function, options)

        def wrapper(*args):

            return CmdsInitUtils.option_parser(function, args, options)

        cmds_registry[function.__name__] = wrapper
        return wrapper
    return decorator


def create_option(name: str, choices: list = None) -> dict:
    if choices is None:
        choices = []

    GlobalUtils.type_checker([(name, str), (choices, list)])

    return {
        "name": "-".join(name.strip().split()),
        "choices": choices
    }


def create_choice(name: str, value=None, dynamic: bool = False) -> dict:
    GlobalUtils.type_checker([(name, str), (dynamic, bool)])

    return {
        "name": "-".join(name.strip().split()),
        "value": value,
        "dynamic": dynamic
    }


# def create_user_choice(name: str, value, value_type: str) -> dict:
    
#     GlobalUtils.type_checker([(name, str), (value_type, str)])

#     return {
#         "name": "-".join(name.strip().split()),
#         "value": GlobalUtils.value_type_converter(value_type, value)
#     }
