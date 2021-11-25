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
    # test command
    print("changed to D:\lol.py")
    return 0


@register(path_cmd_registry, options=[
    create_option(
        name="-something",
        option_type=str,
        required=True,
        choices=[
            create_choice(
                name='hi',
                value="hi"
            )
        ]
    ),
    create_option(
        name="-something else",
        option_type=str,
        required=True,
        choices=[
            create_choice(
                name="aaa",
                value="foo"
            )
        ]
    )
])
def echo(*kwargs):
    pass
    return 0
