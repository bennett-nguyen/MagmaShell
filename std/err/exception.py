import std


class MagmaException(Exception):
    __slots__ = "errors", "exit_status", "show_error", "message"
    
    def __init__(self, errors: str, exit_status: int, show_error: bool = True, message = None):
        if message is None:
            message = ""
            
        std.utils.GlobalUtils.type_checker(
            [(errors, str), (exit_status, int), (show_error, bool), (message, str)]
        )

        super().__init__(message)

        self.errors = errors
        self.exit_status = exit_status
        self.show_error = show_error
