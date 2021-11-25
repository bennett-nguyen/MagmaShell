import os
import importlib


# if a command is registered using the register() decorator then it can be access from the command-line
# which mean normal function will be ignored

registered_cmds = {

}

"""
Automated import files mechanism:

Import any python file starts with "mag_" and cut out the ".py" suffix
Access the registry inside the file by using "entry[3:-3]" (slice "mag_" and ".py") then add "_registry" as suffix
Splat (**) it to registered_cmds 
"""

for entry in os.listdir("./std_cmds"):
    if entry.startswith("mag_") and entry.endswith(".py"):

        module = importlib.import_module(
            name=f".{entry[:-3]}",
            package="std_cmds"
        )
        try:
            registered_cmds.update(
                {
                    **getattr(module, f"{entry[4:-3]}_registry")
                }
            )
        except AttributeError as e:
            print(e)
