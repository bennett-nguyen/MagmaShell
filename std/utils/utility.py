import inspect

def type_checker(list_of_args: list):
    for arg in list_of_args:
        if not isinstance(arg[0], arg[1]):
            raise TypeError(
                f"Type of '{arg[0]}' should be '{arg[1].__name__}' but '{type(arg[0]).__name__}' was given."
            )

def init_help_message(function, options):
    user_help_message = "" if not function.__doc__ else inspect.cleandoc(
                function.__doc__) + "\n\n"

    help_var = []
    index = 0

    for option in options:
        choices = [choice for choice in option['choices']]

        help_var.append(
            f"{option['name']} {choices}")
        index += 1

    help_var = "\n".join(help_var)

    function.__doc__ = inspect.cleandoc(f"{user_help_message}{help_var}")