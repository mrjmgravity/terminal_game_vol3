import game_constants
import phase.main_menu
from phase import phase_constants
from phase import hero_data
from phase import save_load


def start_game():
    while True:
        print("0 - Start new game")
        print("1 - Load game")
        start_choice = input("What is your choice? ")

        if start_choice not in ["0", "1"]:
            print("Invalid input")
            continue
        print(game_constants.DIVIDER)

        if start_choice == "0":
            return phase_constants.INTRO
        else:
            loaded, next_phase = save_load.load_game()
            if loaded:
                print("Game is loaded, welcome back " + hero_data.hero_name)
                print(game_constants.DIVIDER)
                return phase.main_menu.menu()
            else:
                print(game_constants.DIVIDER)
                continue
