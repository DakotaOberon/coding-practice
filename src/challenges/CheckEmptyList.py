from src.Challenge import Challenge


class CheckEmptyList(Challenge):
    def __init__(self):
        super(CheckEmptyList, self).__init__()
        self.challenge = 'Check if a list is empty'

    def code(self):
        l = []

        print('l =', l, 'is_empty:', len(l) == 0)
        
        l.append('item')

        print('l =', l, 'is_empty:', len(l) == 0)
