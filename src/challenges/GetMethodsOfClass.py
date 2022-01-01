from src.Challenge import Challenge


class GetMethodsOfClass(Challenge):
    def __init__(self):
        super(GetMethodsOfClass, self).__init__()
        self.challenge = 'Get a list of methods from an instance'

    def code(self):
        c = UserCreatedClass()
        print('Methods and attributes of instance c\n')
        print(dir(c))

class UserCreatedClass:
    def __init__(self):
        self.first = 1
        self.second = 2
        self.third = 3
    
    def a_function(self):
        return
