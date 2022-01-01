class ChallengeGroup:
    def __init__(self):
        self.challenges = []
    
    def add(self, *args):
        for c in args:
            print(c)
            self.challenges.append(c)
    
    def get_challenges(self):
        return self.challenges
    
    def run_challenges(self):
        length = len(self.challenges)
        print(f'Running {length} Challenge{"s" if length > 1 else ""}')
        for x in self.challenges:
            x.run()

class Challenge:
    def __init__(self):
        self.name = self.__class__.__name__

    def run(self):
        title = f'##### Running Challenge: {self.name} #####'
        print(title)
        print(self.challenge)
        self.code()
        print('#' * len(title))

    def code(self):
        '''Replace with challenge code'''
        return
