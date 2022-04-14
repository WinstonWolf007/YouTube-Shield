all_command_dict = {}


class Command:
    def add(self, *, name: str, param_dash: bool = False, only_one_param: bool = False, **value):
        def inner(fn):
            def wrapper():
                if not param_dash:
                    if not only_one_param:
                        all_command_dict[name] = {'param': value, 'code': fn}
                    else:
                        all_command_dict[name] = {'code': fn}
                else:
                    if not only_one_param:
                        new_value = {}
                        for x in value:
                            new_value['-'+x] = value[x]
                        all_command_dict[name] = {'param': new_value, 'code': fn}
                    else:
                        all_command_dict[name] = {'code': fn}
            return wrapper()
        return inner
