from src.Challenge import Challenge


class CheckIfInstanceOf(Challenge):
    def __init__(self):
        super(CheckIfInstanceOf, self).__init__()
        self.challenge = 'Check if an instance is of a specific class'

    def code(self):
        a = TestClass()
        b = TestSubclass()

        print(f'a\'s class is {type(a).__name__}')
        print(f'b\'s class is {type(b).__name__}')
        print()
        print('a is a subclass of TestClass?', isinstance(a, TestClass))
        print('b is a subclass of TestClass?', isinstance(b, TestClass))

class TestClass:
    pass

class TestSubclass(TestClass):
    pass
