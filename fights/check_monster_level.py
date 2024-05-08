import enemies_abilities


def update_monster_level():
    monster_level = 0
    if not enemies_abilities.enemies[1]["is_dead"]:
        monster_level = 1
    elif not enemies_abilities.enemies[2]["is_dead"]:
        monster_level = 2
    elif not enemies_abilities.enemies[3]["is_dead"]:
        monster_level = 3
    elif not enemies_abilities.enemies[4]["is_dead"]:
        monster_level = 4
    elif not enemies_abilities.enemies[5]["is_dead"]:
        monster_level = 5
    return monster_level
