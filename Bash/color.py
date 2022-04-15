colors = {
    'red': '\033[91m',
    'green': '\033[92m',
    'blue': '\033[94m',
    'yellow': '\033[93m',
    'grey': '\033[90m'
}


def colors_string(color_name, *value):
    value = " ".join(value)
    try:
        return colors[color_name] + value + '\033[0m'
    except:
        return value
