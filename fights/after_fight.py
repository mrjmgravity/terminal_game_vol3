import game_constants
import phase.hero_data
from phase import hero_data
from phase import hero_abilities
from phase import main_menu


def after_battle():
    hero_data.available_points = 3
    health = phase.hero_data.hero_health
    print(game_constants.DIVIDER)
    print(f"You survive with {health} health")
    print(game_constants.DIVIDER)
    print("After winning fight u can add another ability points")
    print(game_constants.DIVIDER)
    hero_abilities.abilities_assign()
    main_menu.menu()

