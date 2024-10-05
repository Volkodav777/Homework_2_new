
class Person:
    def __init__ (self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def __count_damage(self, enemy_armor):
        damage_in_armor = self.damage - (enemy_armor * 0.5)

        return max (damage_in_armor, 0)

    def attack(self, enemy):
        damage = self.__count_damage(enemy.armor)
        print(f'{self.name} атакует {enemy.name} и наносит {damage}')


class EnemyChar(Person):
        def __init__(self, name, health, damage, armor):
            super().__init__(name, health, damage, armor)

class PlayerChar(Person):
        def __init__(self, name, health,damage,armor):
            super().__init__(name, health, damage, armor)


enemy_char = EnemyChar (name = 'Faramir', health = 100, damage = 25, armor = 10)
player_char = PlayerChar (name = 'Boromir', health= 100, damage = 20, armor = 10)

enemy_char.attack(player_char)
player_char.attack(enemy_char)




