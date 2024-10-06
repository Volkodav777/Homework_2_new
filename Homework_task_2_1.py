class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def __count_damage(self, enemy_armor):
        """Приватный метод для расчета урона с учётом брони противника"""
        damage_in_armor = self.damage - (enemy_armor * 0.5)
        return max(damage_in_armor, 0)

    def attack(self, enemy):
        damage = self.__count_damage(enemy.armor)  # Считаем урон
        print(f'{self.name} атакует {enemy.name} и наносит {damage} урона!')  # Сообщение об атаке
        enemy.take_damage(damage)  # Уменьшаем здоровье у противника

    def take_damage(self, damage):
        self.health -= damage
        print(f'{self.name} потерял {damage} здоровья. Осталось {self.health} здоровья.')

    def is_alive(self):
        return self.health > 0


class EnemyChar(Person):
    def __init__(self, name, health, damage, armor):
        super().__init__(name, health, damage, armor)


class PlayerChar(Person):
    def __init__(self, name, health, damage, armor):
        super().__init__(name, health, damage, armor)


enemy_char = EnemyChar(name='Faramir', health=100, damage=20, armor=10)
player_char = PlayerChar(name='Boromir', health=100, damage=20, armor=10)

while player_char.is_alive() and enemy_char.is_alive():
    enemy_char.attack(player_char)
    if not player_char.is_alive():
        print(f'{player_char.name} проиграл!')
        break

    player_char.attack(enemy_char)
    if not enemy_char.is_alive():
        print(f'{enemy_char.name} проиграл!')
        break
