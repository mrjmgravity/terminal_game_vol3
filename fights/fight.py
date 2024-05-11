import enemies_abilities
import enemy_data
import game_constants
import phase.hero_abilities
from phase import hero_data
import random
from fights import check_monster_level


def fighting():
    monster_level = check_monster_level.update_monster_level()
    is_alive = enemies_abilities.enemies[monster_level]["is_dead"]
    hero_health_left = int(hero_data.hero_health)
    enemy_health_left = int(enemy_data.enemy_health)

    print("You are attacking first\n")
    while hero_health_left > 0 or enemy_health_left > 0:

        if not is_alive:
            print(f"You have attacked an enemy with damage {hero_dealt_damage()}")
            enemy_health_left -= enemy_damage_received()
            print(f"{enemy_data.enemy_name} has {enemy_health_left} left \n")
            print(f"{enemy_data.enemy_name} is attacking with {enemy_dealt_damage()}")
            hero_health_left -= hero_received()
            print(f"You have {hero_health_left} left")
            print(game_constants.DIVIDER)
        else:
            is_alive = True


def hero_received():
    defense = random.randint(hero_data.min_defense, hero_data.max_defense)
    received_damage = enemy_dealt_damage() - defense
    return received_damage


def enemy_dealt_damage():
    enemy_dmg = random.randint(enemy_data.min_attack, enemy_data.max_attack)
    crit_chance = random.randint(0, 99)
    crit = enemies_abilities.enemies[check_monster_level.update_monster_level()]["Luck"]
    if crit_chance <= crit:
        return enemy_dmg * 3
    else:
        return enemy_dmg


def enemy_damage_received():
    defense = random.randint(enemy_data.min_defense, enemy_data.max_defense)
    received_damage = hero_dealt_damage() - defense
    return received_damage


def hero_dealt_damage():
    damage = random.randint(hero_data.min_attack, hero_data.max_attack)
    crit_chance = random.randint(0, 100)
    crit = phase.hero_abilities.abilities["Luck"]["points"]

    if crit_chance <= crit:
        return damage * 3
    else:
        return damage
