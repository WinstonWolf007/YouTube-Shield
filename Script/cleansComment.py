from Bash.command import Command

command = Command()


@command.add(name='commit')
def cleans_comment():
    print('in func')

@command.add(name='mkdir', only_one_param=True)
def cleans_2(param):
    print('in func', param)
