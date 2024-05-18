import enemies_abilities
import enemy_data
import game_constants
from phase import hero_data
import random
from fights import check_monster_level
from fights import after_fight
from fights import battle


def fighting():
    monster_level = check_monster_level.update_monster_level()
    hero_health_left = hero_data.hero_health
    enemy_health_left = enemy_data.enemy_health

    battle.hero_prepared()
    battle.enemy_prepared()

    print("You are attacking first\n")
    while hero_health_left >= 0 or enemy_health_left >= 0:

        if monster_level:
            print(f"You have attacked {enemy_data.enemy_name} with damage {hero_dealt_damage()}")
            enemy_health_left -= hero_dealt_damage()
            print(f"{enemy_data.enemy_name} has {enemy_health_left} health left.\n")
            if enemy_health_left <= 0:
                print("Enemy defeated!")
                print(game_constants.DIVIDER)
                after_fight.after_battle()
                break
            print(f"{enemy_data.enemy_name} is attacking with {enemy_dealt_damage()} damage.")
            hero_health_left -= enemy_dealt_damage()
            print(f"You have {hero_health_left} health left.\n")
            if hero_health_left <= 0:
                print(game_constants.DIVIDER)
                print("You have been defeated!")
                print(game_constants.DIVIDER)

        else:
            print("The enemy is already defeated!")
            print(game_constants.DIVIDER)

            break
        print(game_constants.DIVIDER)


def hero_received():
    defense = random.randint(hero_data.min_defense, hero_data.max_defense)
    received_damage = max(enemy_dealt_damage() - defense, 0)
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
    received_damage = max(hero_dealt_damage() - defense, 0)
    return received_damage


def hero_dealt_damage():
    damage = random.randint(hero_data.min_attack, hero_data.max_attack)
    crit_chance = random.randint(0, 100)
    if crit_chance <= hero_data.crit_chance:
        return damage * 3
    else:
        return damage
