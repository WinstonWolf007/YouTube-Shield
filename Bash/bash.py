from Bash.splitLine import Split
import Bash.command as command


splits = Split().splits


def run():
    line = splits(input("YoutubeShield~$ "))
    for x in line:
        if x[0] in command.all_command_dict and len(command.all_command_dict[x[0]]) == 2:
            param = {}
            for y, el in enumerate(x[1:]):
                if y % 2 == 0:
                    param[el] = x[1:][y+1]

            if param:
                command.all_command_dict.get(x[0])['code'](param)
            else:
                command.all_command_dict.get(x[0])['code']()
        elif x[0] in command.all_command_dict and len(command.all_command_dict[x[0]]) == 1:
            if len(x) == 2:
                command.all_command_dict.get(x[0])['code'](x[1])
            else:
                command.all_command_dict.get(x[0])['code']()
