from phase import phase_constants
from phase import hero_data
from phase.save_load import load_game
from phase import main_menu


def start_game():
    while True:
        print("0 - Start new game")
        print("1 - Load game")
        start_choice = input("What is your choice? ")

        if start_choice not in ["0", "1"]:
            print("Invalid input")
            continue

        if start_choice == "0":
            return phase_constants.INTRO
        else:
            loaded, next_phase = load_game
            if loaded:
                print("Game is loaded, welcome back" + hero_data.hero_name)
                return main_menu.menu()
            else:
                continue
