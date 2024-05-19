import game_constants
from phase import hero_data
import enemy_data
import enemies_abilities

def battle(fight_level):
    enemy_data = enemies_abilities.enemies[fight_level]


def hero_prepared():

    print("This is how you are prepared")
    print(f"Damage: minimum - {hero_data.min_attack}, maximum - {hero_data.max_attack}")
    print(f"Your critical change is {hero_data.crit_chance}%")
    print(f"Defense: minimum - {hero_data.min_defense}, maximum - {hero_data.max_defense}")
    print(f"Health - {hero_data.hero_health}")
    print("\n")


def enemy_prepared():
    print(f"This is your enemy {enemy_data.enemy_name}")
    print(f"Damage: minimum - {enemy_data.min_attack}, maximum - {enemy_data.max_attack}")
    print(f"{enemy_data.enemy_name.replace("(LVL 1)", "")} critical chance is {enemy_data.crit_chance}%")
    print(f"Defense: minimum - {enemy_data.min_defense}, maximum - {enemy_data.max_defense}")
    print(f"Health - {enemy_data.enemy_health}")
    print(game_constants.DIVIDER)
