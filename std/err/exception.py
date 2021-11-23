# functions, variables, etc... which starts with a "_" is a hidden part of the module and can't be access from outside

def _type_checker(errors, exit_status, show_warning):
    if type(exit_status) is not int:
        raise TypeError("Exit status must be an integer!")
    if type(errors) is not str:
        raise TypeError("Error messages must be a string!")
    if type(show_warning) is not bool:
        raise TypeError("show_warning must be a boolean!")


class MagmaException(Exception):

    def __init__(self, errors: str, exit_status: int, show_warning: bool = True, message=None):
        _type_checker(errors, exit_status, show_warning)

        super().__init__(message)

        self.errors = errors
        self.exit_status = exit_status
        self.show_warning = show_warning
