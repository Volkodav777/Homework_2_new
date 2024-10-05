class Toy:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type

    def __str__(self):
        return f"Игрушка: {self.name} Цвет: {self.color} Тип: {self.toy_type}"

class AnimalToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color, toy_type = "животное")

    def __str__(self):
        return f"Игрушка: {self.name}, Цвет: {self.color}, Тип: {self.toy_type}"


class CharacterToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color, toy_type= "персонаж мультфильма")

    def __str__(self):
        return f"Игрушка: {self.name}, Цвет: {self.color}, Тип: {self.toy_type}"

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

        if toy_type == "животное":
            return AnimalToy(name, color)
        elif toy_type == "персонаж мультфильма":
            return CharacterToy(name, color)

Create = CreateToy()

animal_toy = Create.create_toy(name = "Фредди Фазберр. ", color = "Коричневый. ", toy_type = "животное")
print(animal_toy)

character_toy = Create.create_toy(name="Базз Лайтер", color=" белый", toy_type="персонаж мультфильма")
print(character_toy)








