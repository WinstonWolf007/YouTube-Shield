from Bash.splitLine import Split
import Bash.command as command
from Bash.color import colors_string


splits = Split().splits


def run():
    line = splits(input(colors_string('grey', "YoutubeShield") + colors_string('yellow', '~$ ')))
    for x in line:
        if x[0] in command.all_command_dict and 'param' in command.all_command_dict[x[0]]:
            param = {}
            for y, el in enumerate(x[1:]):
                if y % 2 == 0:
                    param[el] = x[1:][y+1]

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
                command.all_command_dict.get(x[0])['code']()
            else:
                command.all_command_dict.get(x[0])['code'](x[1])
        else:
            print(colors_string('red', f"SyntaxError: command '{x[0]}' not found..."))
