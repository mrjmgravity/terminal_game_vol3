from fights import check_monster_level
import enemies_abilities


monster_level = check_monster_level.update_monster_level()

if 1 <= monster_level <= 5:
    enemy_info = enemies_abilities.enemies[monster_level]
    enemy_name = enemy_info["name"]
    enemy_health = enemy_info["Health"]
    min_attack = enemy_info["Damage"]
    max_attack = (enemy_info["Damage"] + enemy_info["Dexterity"] + enemy_info["Skill"])
    min_defense = enemy_info["Defense"]
    max_defense = enemy_info["Defense"] + enemy_info["Dexterity"]
else:
    # Handle invalid monster level
    print("Invalid monster level")
