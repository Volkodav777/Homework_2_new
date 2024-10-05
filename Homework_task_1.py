
class TownCar:
    def __init__(self, name, color, speed=0):
        self.speed = speed
        self.name = name
        self.color = color
        self.is_police = True

    def go(self):
        print(f'{self.name} Поехала.')

    def turn(self, direction):
        print(f'{self.name} Повернула {direction}')

    def stop(self):
        print(f'{self.name} Остановилась.')


class SportCar:
    def __init__(self, name, color, speed=0):
        self.speed = speed
        self.name = name
        self.color = color
        self.is_police = True

    def go(self):
        print(f'{self.name} Поехала.')

    def turn(self, direction):
        print(f'{self.name} Повернула {direction}')

    def stop(self):
        print(f'{self.name} Остановилась.')


class WorkCar:
    def __init__(self, name, color, speed=0):
        self.speed = speed
        self.name = name
        self.color = color
        self.is_police = True

    def go(self):
        print(f'{self.name} Поехала.')

    def turn(self, direction):
        print(f'{self.name} Повернула {direction}')

    def stop(self):
        print(f'{self.name} Остановилась.')


class PoliceCar:
    def __init__(self, name, color, speed=0):
        self.speed = speed
        self.name = name
        self.color = color
        self.is_police = True

    def go(self):
        print(f'{self.name} Поехала.')

    def turn(self, direction):
        print(f'{self.name} Повернула {direction}')

    def stop(self):
        print(f'{self.name} Остановилась.')


town_car = TownCar (name = "Ваз 2109", color = "Вишневая", speed = 60)
sport_car = SportCar (name = "Lada granta SPORT", color = "металлик", speed = 99)
work_car = WorkCar (name = "Nissan lsx", color = "Anodized Orange Metallic", speed = 190)
police_car = PoliceCar (name = "ВАЗ 2114", color = "green", speed = 45)


town_car.go()
town_car.turn("в столб")
town_car.stop()

sport_car.go()
sport_car.turn("в управляемый занос")
sport_car.stop()

work_car.go()
work_car.turn("налево")
work_car.stop()

police_car.go()
police_car.turn("направо")
police_car.stop()





