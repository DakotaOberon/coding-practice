import inspect

from src.Challenge import Challenge


class SetGlobalInFunction(Challenge):
    def __init__(self):
        super(SetGlobalInFunction, self).__init__()
        self.challenge = 'Set a global variable inside of a function'

    def code(self):
        self.create_global()

        print(inspect.getsource(self.create_global))
        print("Global:", global_variable_from_function)

    def create_global(self):
        global global_variable_from_function
        global_variable_from_function = "I am global"
