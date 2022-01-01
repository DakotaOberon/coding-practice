import inspect

from src.Challenge import Challenge


class ChainDecorators(Challenge):
    def __init__(self):
        super(ChainDecorators, self).__init__()
        self.challenge = 'Chain multiple decorators together'

    def code(self):
        starting_string = 'Middle'
        print('starting_string =', starting_string)

        ending_string = surround_string('Middle')
        print('ending_string =', ending_string)

        decorator_one_func = inspect.getsource(decorator_one)
        decorator_two_func = inspect.getsource(decorator_two)
        print('\nFirst decorator function:\n', decorator_one_func)
        print('Second decorator function:\n', decorator_two_func)
        print('Actual function:\n', '@decorator_one\n @decorator_two\n def surround_string(string):\n    return string')

def decorator_one(func):
    def inner_func(string):
        x = func(string)
        return 'Start ' + x

    return inner_func

def decorator_two(func):
    def inner_func(string):
        x = func(string)
        return x + ' End'

    return inner_func

@decorator_one
@decorator_two
def surround_string(string):
    return string
