import random
from enemy import Enemy
from hero import Hero

class Boss(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name, health=200, attackPower=10)

    def PlayGuitar(self):
        """PLAYING GUITAR"""
        print(f"{self.name} will rock your world!")
        damage=Guitar().attack()
        bonus_damage=10
        return damage + bonus_damage