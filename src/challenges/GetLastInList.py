from src.Challenge import Challenge


class GetLastInList(Challenge):
    def __init__(self):
        super(GetLastInList, self).__init__()
        self.challenge = 'Get the last item in a list'

    def code(self):
        l = ['1st', '2nd', '3rd']

        print('l =', l)
        print('l[-1] =', l[-1])
