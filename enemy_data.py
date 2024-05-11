from fights import check_monster_level
import enemies_abilities
from enemies_abilities import enemies


monster_level = check_monster_level.update_monster_level()

if 1 <= monster_level <= 5:
    enemy_info = enemies_abilities.enemies[monster_level]
    is_dead = enemy_info["is_dead"]
    enemy_name = enemy_info["name"]
    enemy_health = enemy_info["Health"]
    min_attack = enemy_info["Damage"]
    max_attack = (enemy_info["Damage"] + enemy_info["Dexterity"] + enemy_info["Skill"])
    min_defense = enemy_info["Defense"]
    max_defense = enemy_info["Defense"] + enemy_info["Dexterity"]
    crit_chance = (enemies[monster_level]["Skill"] + enemies[monster_level]["Luck"]) / 2
else:
    print("Invalid monster level")
