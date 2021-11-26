from std.utils import type_checker

class MagmaException(Exception):

    def __init__(self, errors: str, exit_status: int, show_warning: bool = True, message=None):
        type_checker([(errors, str), (exit_status, int), (show_warning, bool)])

        super().__init__(message)

        self.errors = errors
        self.exit_status = exit_status
        self.show_warning = show_warning
