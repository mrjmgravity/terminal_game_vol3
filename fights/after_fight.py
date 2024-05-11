import game_constants
import phase.hero_data


def after_battle():
    health = phase.hero_data.hero_health
    print(game_constants.DIVIDER)
    print(f"You survive with {health} health")
    print(game_constants.DIVIDER)

