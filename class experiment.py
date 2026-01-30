class Enemy:
    def __init___(self, race, hp, size, damage, description)
        self.race = race
        self.hp = hp
        self.size = size
        self.damage = damage
        self. description = description

        def describe (self):
            return f"{self.description}{self.race} that is {self.size} that has {self.hp} hit points and can do {self.damage}"
troll = Enemy ("troll",50, "Large", 10, "ugly, warty, and stinky")
print(f"You encounter a {troll.describe()}!")
class Weapon:
    def __init__(self, damage, name, type, durability):
        self.damage = damage
        self.name = name
        self.type = type
        self.durability = durability
    def attack(self, damage, durability, name):
        return f"{name} did {damage} and has {durability} remaining"
        

    Excalibur = Weapon(100, "Excalibur", "Sword", 10)
    NissanAltima = Weapon(20000, "Nissan Altima", "car", 1)

    class Attack:
        def__init__(self, Enemy, enemy.hp, )