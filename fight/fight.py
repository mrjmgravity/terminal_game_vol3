import enemies_abilities
import enemy_data
import phase.hero_abilities
from phase import hero_data
import random


def fighting():
    hero_health = int(hero_data.hero_health)
    enemy_health = int(enemy_data.hero_health)

    while hero_health > 0 and enemy_health > 0:
        print("You are attacking first\n")

        enemy_damage = enemy_dealt_damage()
        hero_health -= max(0, enemy_damage - hero_received())

        if hero_health <= 0:
            print("You have been defeated!")
            break

        print(f"You have attacked the enemy dealing {hero_dealt_damage()} damage.")

        enemy_health -= max(0, hero_dealt_damage() - enemy_received())

        if enemy_health <= 0:
            print("You have defeated the enemy!")
            break

        print(f"The enemy attacks you dealing {enemy_damage} damage.")

        print(f"You have {hero_health} health left.")
        print(f"The enemy has {enemy_health} health left.\n")


def hero_received():
    defense = random.randint(hero_data.min_defense, hero_data.max_defense)
    return defense


def enemy_received():
    defense = random.randint(enemy_data.min_defense, enemy_data.max_defense)
    return defense


def enemy_dealt_damage():
    enemy_dmg = random.randint(enemy_data.min_attack, enemy_data.max_attack)
    crit_chance = random.randint(0, 99)
    crit = enemies_abilities["Luck"]
    if crit_chance <= crit:
        return enemy_dmg * 3
    else:
        return enemy_dmg


def hero_dealt_damage():
    damage = random.randint(hero_data.min_attack, hero_data.max_attack)
    crit_chance = random.randint(0, 99)
    crit = phase.hero_abilities.abilities[enemies_abilities.enemies]["Luck"]
    if crit_chance <= crit:
        return damage * 3
    else:
        return damage
