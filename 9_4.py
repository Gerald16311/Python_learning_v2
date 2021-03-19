# Реализуйте базовый класс Car:
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула(куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60(TownCar) и 40(WorkCar) должно выводиться сообщение о
# превышении скорости. Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} начал движение')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'У {self.name} скорость = {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if int(self.speed) > 60:
            print('Превышение скорости')
        else:
            print(f'У {self.name} скорость = {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if int(self.speed) > 40:
            print('Превышение скорости')
        else:
            print(f'У {self.name} скорость = {self.speed}')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


sport_car = SportCar(180, "Красый", "Феррари")
town_car = TownCar(60, "оранжевый", "Троллейбус")
work_car = WorkCar(40, "Black", "KAMAZ")
police_Car = PoliceCar(100, "Белая", "Гранта", True)

sport_car.go()
town_car.go()
work_car.go()
police_Car.go()

sport_car.stop()
town_car.stop()
work_car.stop()
police_Car.stop()

sport_car.turn("направо")
town_car.turn("налево")
work_car.turn("назад")
police_Car.turn("направо")

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_Car.show_speed()