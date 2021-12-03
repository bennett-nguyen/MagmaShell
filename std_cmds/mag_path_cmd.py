from std.err import MagmaException
from std.res import register, create_choice, create_option
import os

path_cmd_registry = {}


@register(path_cmd_registry)
def pwd():
    print(os.getcwd())
    return 0


@register(path_cmd_registry)
def cd():
    print("changed to D:\lol.py")
    return 0

@register(path_cmd_registry, options=[
    create_option(
        name="-m",
        choices=[
            create_choice(
                name="dynamic-choice",
                dynamic=True
            )
        ]
    )
])

def echo(*args, **kwargs):
    """
    Print out anything from argument.
    """
    print(kwargs["option"]["choices"]["value"])
    return 0
