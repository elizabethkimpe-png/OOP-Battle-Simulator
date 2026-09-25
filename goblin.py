import random
from enemy import Enemy
from hero import Hero

class Goblin(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name, health=100, attackPower=7)
        self.gold=0

    def stealGold(self):
        """TAKING GOLD"""
        self.gold=self.gold+Hero.gold
        Hero.gold=0
        print("No gold bro")

