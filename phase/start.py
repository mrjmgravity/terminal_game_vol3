from phase import phase_constants
from phase import save_load


def start_game():
    while True:
        print("0 - Start new game")
        print("1 - Load game")
        start_choice = input("What is your choice? ")

        if start_choice not in ["0", "1"]:
            print("Invalid input")
            continue

        if start_choice == 0:
            return phase_constants.INTRO
        else:
            save_load.load_game()
