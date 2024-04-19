import game_constants
from phase import phase_constants
from phase import abilities


def menu():
    while True:
        print("0 - Continue to FIGHT")
        print("1 - Edit Hero")
        print("2 - Save the game")
        print("3 - Quit the game")
        menu_input = int(input("What is your choice? "))

        if menu_input not in [0, 1, 2, 3]:
            print("Invalid input")
            continue

        if menu_input == 0:
            return phase_constants.FIGHT
        elif menu_input == 1:
            abilities.remove_ability()
            return phase_constants.MENU
            pass
        elif menu_input == 2:
            #TODO ulozenie hry
            pass
        elif menu_input == 3:
            print("Goodbye")
            print(game_constants.DIVIDER)
            return phase_constants.END
        else:
            print("Invalid input")
