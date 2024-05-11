from fights import check_monster_level
import enemies_abilities


if check_monster_level.update_monster_level() == 1:
    enemy_name = enemies_abilities.enemies[1]["name"]
    enemy_health = enemies_abilities.enemies[1]["Health"]
    min_attack = enemies_abilities.enemies[1]["Damage"]
    max_attack = (enemies_abilities.enemies[1]["Damage"] + enemies_abilities.enemies[1]["Dexterity"] +
                  enemies_abilities.enemies[1]["Skill"])
    min_defense = enemies_abilities.enemies[1]["Defense"]
    max_defense = enemies_abilities.enemies[1]["Defense"] + enemies_abilities.enemies[1]["Dexterity"]

elif check_monster_level.update_monster_level() == 2:
    enemy_name = enemies_abilities.enemies[2]["name"]
    enemy_health = enemies_abilities.enemies[2]["Health"]
    min_attack = enemies_abilities.enemies[2]["Damage"]
    max_attack = (enemies_abilities.enemies[2]["Damage"] + enemies_abilities.enemies[2]["Dexterity"] +
                  enemies_abilities.enemies[2]["Skill"])
    min_defense = enemies_abilities.enemies[2]["Defense"]
    max_defense = enemies_abilities.enemies[2]["Defense"] + enemies_abilities.enemies[2]["Dexterity"]

elif check_monster_level.update_monster_level() == 3:
    enemy_name = enemies_abilities.enemies[3]["name"]
    enemy_health = enemies_abilities.enemies[3]["Health"]
    min_attack = enemies_abilities.enemies[3]["Damage"]
    max_attack = (enemies_abilities.enemies[3]["Damage"] + enemies_abilities.enemies[3]["Dexterity"] +
                  enemies_abilities.enemies[3]["Skill"])
    min_defense = enemies_abilities.enemies[3]["Defense"]
    max_defense = enemies_abilities.enemies[3]["Defense"] + enemies_abilities.enemies[3]["Dexterity"]

elif check_monster_level.update_monster_level() == 4:
    enemy_name = enemies_abilities.enemies[4]["name"]
    enemy_health = enemies_abilities.enemies[4]["Health"]
    min_attack = enemies_abilities.enemies[4]["Damage"]
    max_attack = (enemies_abilities.enemies[4]["Damage"] + enemies_abilities.enemies[4]["Dexterity"] +
                  enemies_abilities.enemies[4]["Skill"])
    min_defense = enemies_abilities.enemies[4]["Defense"]
    max_defense = enemies_abilities.enemies[4]["Defense"] + enemies_abilities.enemies[4]["Dexterity"]

elif check_monster_level.update_monster_level() == 5:
    enemy_name = enemies_abilities.enemies[5]["name"]
    enemy_health = enemies_abilities.enemies[5]["Health"]
    min_attack = enemies_abilities.enemies[5]["Damage"]
    max_attack = (enemies_abilities.enemies[5]["Damage"] + enemies_abilities.enemies[5]["Dexterity"] +
                  enemies_abilities.enemies[5]["Skill"])
    min_defense = enemies_abilities.enemies[5]["Defense"]
    max_defense = enemies_abilities.enemies[5]["Defense"] + enemies_abilities.enemies[5]["Dexterity"]

