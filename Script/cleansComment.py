from Bash.command import Command


command = Command()

"""
When I put just one key

packageX64 -version

the program put an error:
    File "/home/winstonwolf007/Prog/python/YouTube-Shield/Bash/bash.py", line 15, in run
        param[el] = x[1:][y+1]
        IndexError: list index out of range
"""

@command.add(name='pluginX64', param_dash=True, v=str)
def open_application():
    print('Version: 20.00.4')
