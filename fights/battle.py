import game_constants
from phase.hero_abilities import abilities
from enemies_abilities import enemies
from phase import hero_data
import enemy_data


def hero_prepared():
    hero_data.min_attack = abilities["Damage"]["points"]
    hero_data.max_attack = hero_data.min_attack + abilities["Dexterity"]["points"] + abilities["Skill"]["points"]
    hero_data.min_defense = abilities["Defense"]["points"]
    hero_data.max_defense = hero_data.min_defense + abilities["Dexterity"]["points"]
    hero_data.crit_chance = (abilities["Skill"]["points"] + abilities["Luck"]["points"])/2
    hero_data.hero_health = abilities["Health"]["points"]

    print("This is how you are prepared")
    print(f"Damage: minimum - {hero_data.min_attack}, maximum - {hero_data.max_attack}")
    print(f"Your critical change is {hero_data.crit_chance}%")
    print(f"Defense: minimum - {hero_data.min_defense}, maximum - {hero_data.max_defense}")
    print(f"Health - {hero_data.hero_health}")
    print("\n")


def enemy_prepared(monster_level):
    enemy_data.enemy_name = enemies[monster_level]["name"]
    enemy_data.min_attack = enemies[monster_level]["Damage"]
    enemy_data.max_attack = enemy_data.min_attack + enemies[monster_level]["Dexterity"] + enemies[monster_level]["Skill"]
    enemy_data.min_defense = enemies[monster_level]["Defense"]
    enemy_data.max_defense = enemy_data.min_defense + enemies[monster_level]["Dexterity"]
    enemy_data.crit_chance = (enemies[monster_level]["Skill"] + enemies[monster_level]["Luck"]) / 2
    enemy_data.hero_health = enemies[monster_level]["Health"]

    print(f"This is your enemy {enemy_data.enemy_name}")
    print(f"Damage: minimum - {enemy_data.min_attack}, maximum - {enemy_data.max_attack}")
    print(f"{enemy_data.enemy_name.replace("(LVL 1)", "")} critical change is {enemy_data.crit_chance}%")
    print(f"Defense: minimum - {enemy_data.min_defense}, maximum - {enemy_data.max_defense}")
    print(f"Health - {enemy_data.hero_health}")
    print(game_constants.DIVIDER)


def battleground(monster_level):
    hero_prepared()
    enemy_prepared(monster_level)
