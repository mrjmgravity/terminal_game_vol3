import game_constants
from phase import phase_constants
from phase import abilities
from phase.save_load import save_game
from phase.phase_constants import MENU


def menu():
    while True:
        print("0 - Continue to FIGHT")
        print("1 - Edit points")
        print("2 - Save the game")
        print("3 - Quit the game")
        menu_input = int(input("What is your choice? "))

        if menu_input not in [0, 1, 2, 3]:
            print("Invalid input")
            continue

        if menu_input == 0:
            continue
        elif menu_input == 1:
            abilities.remove_ability()
            return phase_constants.MENU
        elif menu_input == 2:
            save_game(MENU)
        elif menu_input == 3:
            print("Goodbye")
            print(game_constants.DIVIDER)
            return phase_constants.END
        else:
            print("Invalid input")
