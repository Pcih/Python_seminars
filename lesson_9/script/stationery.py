"""
еализовать класс Stationery (канцелярская принадлежность).
Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Starting rendering {self.title}'


class Pen(Stationery):

    def draw(self):
        return super().draw()


class Pencil(Stationery):

    def draw(self):
        return super().draw()


class Handle(Stationery):
    def draw(self):
        return super().draw()


def main():
    pen = Pen('pen')
    print(pen.draw())
    pencil = Pencil('pencil')
    print(pencil.draw())
    handle = Handle('handle')
    print(handle.draw())


if __name__ == '__main__':
    main()
