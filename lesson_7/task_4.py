"""
Task_4
Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).
А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car:
    #  Получаем данные.
    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    
    # Определяем движения автомобиля.
    def go(self):
        return f'The {self.name} went.'
    
    def stop(self):
        return f'The {self.name} has stopped.'
    
    def turn(self, direction):
        return f'The {self.name} turned {direction}'

    def show_speed(self):
        return f'Your speed is {self.speed}'


class TownCar(Car):
    def show_speed(self):
        # Проверяем скоростной режим.
        if self.speed > 60 :
            return f'Yuor speed is higher than allow! Your speed is {self.speed}'
        return f'Speed of {self.name} is normal'


class PoliceCar(Car):

    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
        self.is_police = True


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nYour speed is higher than allow! Your speed is {self.speed}'
        else:
            return f'Speed of {self.name} is normal'



class SportCar(Car):

    def go(self, speed=None):
        if speed and (isinstance(speed, int) or isinstance(speed, float)):
            self.speed = speed
            return f'{self.name} changes the speed to {self.speed} km/h'
        elif self.speed:
            return f'{self.name} rides at a speed of {self.speed} km/h'
        return f'{self.name} can\'t go'


town = TownCar('Audi', 70, 'blue', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('left'), town.turn('right'), town.stop())

sport = SportCar('AudiRS', 170, 'red', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('left'), sport.stop())

work = WorkCar('WAZ', 30, 'red', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())

police = PoliceCar('Kia', 100, 'yellow')
print('4:\n' + police.go(), police.show_speed(), police.turn('right'), police.stop())      