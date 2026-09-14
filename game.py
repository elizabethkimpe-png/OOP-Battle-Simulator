from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Iron Square"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gribble")
    hero=Hero("Eowyn")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    goblin2 = Goblin("Sribble")
    
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")

    print(f"{hero.name} enters the arena with {hero.health} health")

    print(f"{hero.name} is fighting {goblin.name}")
    herodamage=hero.attack()
    goblin.take_damage(herodamage)
    goblindamage=goblin.attack()
    hero.take_damage(goblindamage)



if __name__ == "__main__":
    main()
