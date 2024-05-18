import random
from phase import hero_abilities

available_points = 7
hero_name = ""


min_attack = hero_abilities.abilities["Damage"]["points"]
max_attack = (hero_abilities.abilities["Damage"]["points"] + hero_abilities.abilities["Dexterity"]["points"] +
              hero_abilities.abilities["Skill"]["points"])
damage = random.randint(min_attack, max_attack)
min_defense = hero_abilities.abilities["Defense"]["points"]
max_defense = hero_abilities.abilities["Defense"]["points"] + hero_abilities.abilities["Dexterity"]["points"]
hero_health = hero_abilities.abilities["Health"]["points"]
crit_chance = int((hero_abilities.abilities["Skill"]["points"] + hero_abilities.abilities["Luck"]["points"])/2)
crit_perc = random.randint(0, 100)

if crit_chance == crit_perc:
    damage = damage*3

