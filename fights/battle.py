from phase import hero_abilities
import enemies_abilities
from phase import hero_data
import random


def battle(fight_level):
    enemy_data = enemies_abilities.enemies[fight_level]
    hero = {
        "attack": calculate_hero_attack(),
        "critical_hit": min(100, (hero_abilities.abilities["Skill"]["points"] *
                                  hero_abilities.abilities["Šťastie"]["points"]) // 2),
        "defence": (hero_abilities.abilities["Obrana"]["points"],
                    hero_abilities.abilities["Obrana"]["points"] + hero_abilities.abilities["Obratnosť"]["points"]),
        "health": hero_abilities.abilities["Život"]["points"]
    }
    enemy = {
        "name": enemy_data["name"],
        "attack": calculate_enemy_attack(enemy_data),
        "critical_hit": min(100, (enemy_data["Skill"] *
                                  enemy_data["Šťastie"]) // 2),
        "defence": (enemy_data["Obrana"], enemy_data["Obrana"] +
                    enemy_data["Obratnosť"]),
        "health": enemy_data["Život"]
    }
    return simulate_battle(hero, enemy)


def simulate_battle(hero, enemy):
    print("")


def calculate_hero_attack():
    print("")


def calculate_enemy_attack():
    print("")
