import inspect
import std


class GlobalUtils:
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
            Example funtion.
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
                    try:
                        option["choices"] = option["option_type"](args[1])
                    except IndexError:
                        print(f"Expected a choice for '{option['name']}'")
                    except ValueError:
                        return std.err.MagmaException(f"Invalid option type '{option['option_type'].__name__}' for '{args[1]}' choice.", 2)

                    return function(option=option)

            else:
                return std.err.MagmaException(f"'{args[0]}' option not found.", 1)

        return function()

    @staticmethod
    def duplicate_checker(function, options):
        '''
        Check if a command has duplicate options/choices

        Syntax:
        Duplicate option(s): {options}; of command 'command'
        Duplicate choice(s): [{choice, option, command}]
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
        choices = []

        for option in options:
            if option["choices"]:
                temp_list = [(choice["name"], option["name"], function.__name__)
                             for choice in option["choices"]]
                choices.extend(temp_list)

        duplicate_choices = set(
            [choice for choice in choices if choices.count(choice) > 1]
        )

        if duplicate_choices:
            raise std.err.MagmaException(
                message=f"\n\nDuplicate choice(s): {duplicate_choices}", errors="", exit_status=2
            )
