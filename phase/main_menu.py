import game_constants
import phase.phase_constants
from phase import hero_abilities
from phase.save_load import save_game
from phase import phase_constants


def menu():
    while True:
        print("0 - Continue to FIGHT")
        print("1 - Edit points")
        print("2 - Save the game")
        print("3 - Quit the game")
        menu_input = input("What is your choice? ")
        print(game_constants.DIVIDER)

        if menu_input not in ["0", "1", "2", "3"]:
            print("Invalid input")
            continue

        if menu_input == "0":
            return phase.phase_constants.FIGHT
        elif menu_input == "1":
            hero_abilities.remove_ability()
            return phase_constants.MENU
        elif menu_input == "2":
            save_game(phase_constants.MENU)
        elif menu_input == "3":
            print("Goodbye")
            print(game_constants.DIVIDER)
            return phase_constants.END
        else:
            print("Invalid input")
