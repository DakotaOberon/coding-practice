from src.Challenge import Challenge


class SwitchValues(Challenge):
    def __init__(self):
        super(SwitchValues, self).__init__()
        self.challenge = 'Switch the values of 2 variables'

    def code(self):
        a = 'A'
        b = 'B'

        print('a =', a, '\nb =', b)
        a, b = b, a
        print('---After---\na =', a, '\nb =', b)
