class MagmaException(Exception):
	def __init__(self, message, errors):            
		super().__init__(message)
		self.errors = errors            

class ProcessDied(MagmaException):
	def __init__(self, message, errors):
		super().__init__(message, errors)

class InvalidType(MagmaException):
	def __init__(self, message, errors):
		super().__init__(message, errors)

class CommandNotFound(MagmaException):
	def __init__(self, message, errors):
		super().__init__(message, errors)

class UnsupportedPlatform(MagmaException):
	def __init__(self, message, errors):
		super().__init__(message, errors)

class CommandAlreadyExisted(MagmaException):
	def __init__(self, message, errors):
		super().__init__(message, errors)
		