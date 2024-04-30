from phase.hero_abilities import abilities
from enemies_abilities import enemies


def hero_prepared():
    min_attack = abilities["Damage"]["points"]
    max_attack = min_attack + abilities["Dexterity"]["points"] + abilities["Skill"]["points"]
    min_defense = abilities["Defense"]["points"]
    max_defense = min_defense + abilities["Dexterity"]["points"]
    crit_chance = (abilities["Skill"]["points"] + abilities["Luck"]["points"])/2
    hero_health = abilities["Health"]["points"]

    print("This is how you are prepared")
    print(f"Damage: minimum - {min_attack}, maximum - {max_attack}")
    print(f"Your critical change is {crit_chance}%")
    print(f"Defense: minimum - {min_defense}, maximum - {max_defense}")
    print(f"Health - {hero_health}")


def enemy_prepared(monster_level):
    enemy_name = enemies[monster_level]["name"]

    print(f"You will fight against{enemy_name}")


def battle(fight_level):
    print()
