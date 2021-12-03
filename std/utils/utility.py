import inspect
import std

_type_table = {
    "str": str,
    "int": int,
    "float": float,
    "bool": bool
}


class GlobalUtils:

    @staticmethod
    def value_type_converter(desired_value_type: str, value):
        return _type_table[desired_value_type](value)

    @staticmethod
    def type_checker(list_of_args: list):
        for arg in list_of_args:
            arg_name = arg[0]
            arg_type = arg[1]

            if not isinstance(arg_name, arg_type):
                raise TypeError(
                    f"Type of '{arg_name}' should be '{arg_type.__name__}' but '{type(arg_name).__name__}' was given."
                )


class CmdsInitUtils:
    """
    A class that compiles every methods needed
    for the register() decorator to work.
    """

    @staticmethod
    def init_help_message(function, options):
        """
        Initialize help message for a command
        during command's initialization.

        example command:
        @register(registry_dict, options=
            [
                create_option(
                    name = "-a",
                    ...,
                    choices = [
                        create_choice(
                            name = "example-choice",
                            ...
                        )
                    ]
                )
            ]
        )
        def spam(*args, **kwargs):
            '''
            Example function.
            '''
            return 0


        Which creates:

        {user's help message (custom)}
        Example function

        {options and choices (built-in)}
        -a ["example-choice"]
        """

        user_help_message = "" if not function.__doc__ else inspect.cleandoc(  # clean out tabs
            function.__doc__) + "\n\n"

        help_var = []
        index = 0

        for option in options:
            choices = [f"{choice['name']}" for choice in option['choices']]

            help_var.append(
                f"{option['name']} {choices}"
            )
            index += 1

        help_var = "\n".join(help_var)

        function.__doc__ = inspect.cleandoc(f"{user_help_message}{help_var}")

    @staticmethod
    def option_parser(function, args, options):
        """
        Parse through the command's argument
        during function's call.
        """
        if options:
            if not args:
                print(function.__doc__)
                return 0

            for option in options:
                if args[0] == option["name"]:
                    for choice in option["choices"]:
                        if choice['dynamic']:
                            try:
                                return_option = {}
                                return_option.update(option)
                                return_option['choices'] = choice
                                value = args[2]
                                if args[1] == "str":
                                    value = " ".join(args[2:])
                                return_option['choices']['value'] = GlobalUtils.value_type_converter(
                                    args[1], value)
                                return function(option=return_option)
                            except Exception as e:
                                print(e)

                        elif choice['name'] == args[1]:
                            return_option = {}
                            return_option.update(option)
                            return_option['choices'] = choice
                            return function(option=return_option)
                    else:
                        return std.err.MagmaException(f"'{args[1]}' choice not found.", 1)

            else:
                return std.err.MagmaException(f"'{args[0]}' option not found.", 1)

        return function()

    @staticmethod
    def option_inspector(function, options):
        '''
        Check if a command has duplicate options/choices/dynamically typed choices.

        Syntax:
        Duplicate option(s): {options}; of command 'command'
        Duplicate choice(s): [{choice, dynamic, option, command}]
        '''

        # check for duplicate options
        options_names = [option["name"] for option in options]
        duplicate_options = set(
            [option_name for option_name in options_names if options_names.count(option_name) > 1])

        if duplicate_options:
            raise std.err.MagmaException(
                message=f"\n\nDuplicate option(s): {duplicate_options}; of command: '{function.__name__}'", errors="", exit_status=2
            )

        # check for duplicate choices
        # still in revamp
        # choices = []
