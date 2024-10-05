class Toy:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type

    def __str__(self):
        return f"Игрушка: {self.name} Цвет: {self.color} Тип: {self.toy_type}"


class CreateToy:
    def __init__(self):

        pass

    def buy_materials(self, name):
        print(f"Закупаем сырье для {name}")

    def production(self, name):
        print(f"Начинаем пошив {name}")

    def paint_toy(self, color):
        print(f"Окрашиваем игрушку в цвет {color}")

    def create_toy(self, name, color, toy_type):
        self.buy_materials(name)
        self.production(name)
        self.paint_toy(color)

        return Toy(name, color, toy_type)


Create = CreateToy()
new_toy = Create.create_toy(name = "Базз лайтер. ", color = "Белый. ", toy_type = "Персонаж мультфильма")

print(new_toy)







