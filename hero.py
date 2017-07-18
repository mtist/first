from random import randint

class User:
    count = 0
    levels = 0

    def __init__(self, name, attack=40, hp=100):
        self.name = name
        self.lore = lore
        self.hp = hp

    def win(self):
        return '''    Кто тут батька?
    {0.name} батька!'''.format(User)

    def lose(self):
        return '{0.name} облажался'.format(User)

    def damage(self, target):
        target.hp -= (randint(0, self.attack))