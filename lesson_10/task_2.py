class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=Singleton):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sum(self):
        return self.a + self.b


class RegularClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sum(self):
        return self.a + self.b


x1 = SingletonClass(3, 5)
y1 = SingletonClass(5, 5)
print(x1 is y1)


x2 = RegularClass(2, 3)
y2 = RegularClass(1, 4)
print(x2 is y2)
