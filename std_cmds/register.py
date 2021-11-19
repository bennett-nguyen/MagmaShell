from os_cmd import os_cmds_registry
from path_cmd import path_cmds_registry

# if a command is registered then it could be access from the command-line
# which mean normal function will be ignored
 
registered_cmds = {
        **os_cmds_registry,
        **path_cmds_registry
}




