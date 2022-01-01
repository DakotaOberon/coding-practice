from src.Challenge import Challenge


class CheckClassOrSubclass(Challenge):
    def __init__(self):
        super(CheckClassOrSubclass, self).__init__()
        self.challenge = 'Check if an instance is a class or subclass'

    def code(self):
        c = TestClass()
        subc = TestSubclass()
        n = object()

        print('c =', c.__class__.__name__, '\nsubc =', subc.__class__.__name__, '\nn = ', n.__class__.__name__)
        print(f'c is a {self.check_class(c, TestClass)}')
        print(f'subc is a {self.check_class(subc, TestClass)}')
        print(f'n is {self.check_class(n, TestClass)}')

    def check_class(self, _obj, _cls):
        if isinstance(_obj, _cls):
            if type(_obj) is _cls:
                return 'Class'
            else:
                return 'Subclass'

        return 'Neither'

class TestClass:
    pass

class TestSubclass(TestClass):
    pass
