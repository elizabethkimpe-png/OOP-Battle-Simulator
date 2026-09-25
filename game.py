from goblin import Goblin
from hero import Hero
from boss import Boss


ARENA_NAME = "The Iron Square"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gribble")
    boss=Boss("Leah")
    hero=Hero("Eowyn")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    goblin2 = Goblin("Sribble")
    
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
   

    print(f"{hero.name} enters the arena with {hero.health} health")
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"{hero.name} is fighting {goblin.name}")
    herodamage=hero.attack()
    hero.battle_cry()
    goblin.take_damage(herodamage)
    if hero.health>0:
        print(f"{goblin.name} still alive!")
        goblindamage=goblin.attack()
        hero.take_damage(goblindamage)
        
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"{hero.name} is fighting {boss.name}")
    herodamage=hero.attack()
    hero.battle_cry()
    boss.take_damage(herodamage)
    if hero.health>0:
        print(f"{boss.name} still alive!")
        bossdamage=boss.attack()
        boss.PlayGuitar()
        hero.take_damage(bossdamage)
        boss.take_damage(herodamage)
    



if __name__ == "__main__":
    main()
