# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала'

    def stop(self):
        return f'Машина {self.name} остановилась'

    def turn_right(self):
        return f'Машина {self.name} поехала направо'

    def turn_left(self):
        return f'Машина {self.name} поехала налево'

    def show_speed(self):
        return self.speed




class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed >= 60:
            return f'{self.speed} - Внимание, привышение скорости!'
        else:
            return self.speed

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed >= 40:
            return f'{self.speed} - Внимание, привышение скорости!'
        else:
            return self.speed


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


BMW = SportCar(80, ',белый', 'BMW', False)
renault = TownCar(52, 'серый', 'renault', False)
jeep = WorkCar(65, 'синий', 'jeep', False)
subaru = PoliceCar(71, 'черный',  'subaru', True)

print(jeep.turn_left(),',', BMW.stop())
print(f'{BMW.go()} со скоростью {BMW.show_speed()} км./ч, за ней поехал {jeep.color} {jeep.name} ')
print(f'{subaru.color} {subaru.name} полицейская машина -  {subaru.is_police}')
print(f'{jeep.name} полицейская машина -  {BMW.is_police}')
print(renault.show_speed())
print(jeep.show_speed())
