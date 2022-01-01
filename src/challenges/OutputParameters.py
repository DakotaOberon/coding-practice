import inspect

from src.Challenge import Challenge


class OutputParameters(Challenge):
    def __init__(self):
        super(OutputParameters, self).__init__()
        self.challenge = 'Function with output parameters'

    def code(self):
        a = 0
        b = 0

        print('a =', a, '\nb =', b)
        a, b = self.output(a, b)
        print('\nfunction:\n', inspect.getsource(self.output))
        print('a =', a, '\nb =', b)

    def output(self, a, b):
        a = a + 101
        b = b + 202
        return a, b
