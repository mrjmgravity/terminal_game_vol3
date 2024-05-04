import fight.battle
import phase.hero_abilities
from phase import hero_data
from battle import enemy_prepared
import random

def fighting(is_alive, health_left):
    while True:
        print("You are attacking first\n")
        print(f"You have attacked an enemy with damage {damage_dealt()}")
        print("")

def damage_dealt():
    damage = random.randint(hero_data.min_attack, hero_data.max_attack)
    crit_chance = random.randint(0, 99)
    crit = phase.hero_abilities.abilities["Luck"]["points"]
    if crit_chance <= crit:
        return damage*3
    else:
        return damage
