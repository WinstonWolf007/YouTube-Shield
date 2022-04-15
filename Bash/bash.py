from Bash.splitLine import Split
import Bash.command as command
from Bash.color import colors_string


splits = Split().splits


def run():
    line = splits(input(colors_string('grey', "YoutubeShield") + colors_string('yellow', '~$ ')))
    for x in line:
        if len(x) == 1:
            try:
                command.all_command_dict.get(x[0])['code']()
            except:
                print(colors_string('red', f'SyntaxError: it missing the arguments'))
                break
        if x[0] in command.all_command_dict and 'param' in command.all_command_dict[x[0]]:
            param = {}
            for y, el1 in enumerate(x[1:]):
                for el2 in command.all_command_dict[x[0]]['param']:
                    if el1 == el2:
                        param[el1] = x[1:][y+1]
            if param:
                param2 = {}
                for y in param:
                    param2[y.replace('-', '')] = param[y]
                command.all_command_dict.get(x[0])['code'](param2)
            else:
                try:
                    command.all_command_dict.get(x[0])['code']()
                except TypeError:
                    print(colors_string('red', f'SyntaxError: it missing the arguments'))

        elif x[0] in command.all_command_dict and 'result' in command.all_command_dict[x[0]]:
            if str(command.all_command_dict[x[0]]['result'])[0] == '-':
                if len(x) == 2 and x[1] == command.all_command_dict[x[0]]['result']:
                    command.all_command_dict.get(x[0])['code']()
                else:
                    print(colors_string('red', f"SyntaxError: '{x[0]}': it missing argument '{str(command.all_command_dict[x[0]]['result'])}'"))
            else:
                command.all_command_dict.get(x[0])['code'](x[1])
        else:
            print(colors_string('red', f"SyntaxError: command '{x[0]}' not found..."))
