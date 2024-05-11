import phase.hero_data


def after_battle():
    health = phase.hero_data.hero_health
    print(f"You survive with{health}")