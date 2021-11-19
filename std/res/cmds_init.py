# TODO: add user-specific options
import std
# SELF-NOTE: This decoractor helps creating shell cmds, required one more args

def register(cmds_registry: dict):
    def decorator(function):
        cmds_registry.update({function.__name__: function})
        
        def wrapper(*arg, **kwargs):
            return function(*args, **kwargs)
        
        return wrapper
    return decorator

def create_option(name: str, option_type, required: bool, choices: list) -> dict:

    return {
            "name": name,
            "option_type": option_type,
            "required": required,
            "choices": choices
            }

def create_choice(name, value) -> dict:
    return {
            "name": name,
            "value": value
            }