class MyDesc:
    "Оставлю на память что можно изменить __get__"
    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        "Делаем провергу на валидацию"
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        " Для памяти"
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        "Теперь ищем имена атрибутов"
        self.my_attr = my_attr


class Clothes:
    width = MyDesc()
    height = MyDesc()

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_c(self):
        return self.width / 6.5 + 0.5

    def get_square_j(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Площадь общая ткани \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто {self.square_c}'


class Jacket(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм {self.square_j}'


coat = Coat(2, 4)
jacket = Jacket(1, 2)
coat1 = Coat(-2, 4)
jacket1 = Jacket(1, -2)
print(coat)
print(jacket)
print(coat1)
print(jacket1)

