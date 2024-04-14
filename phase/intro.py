import game_constants


def intro():
    while True:

        print("Welcome to the game called Arcadius. Are you ready?\n0 - Quit game\n1 - Im ready")
        intro_choice = input("What do you want to choose? ")

        if intro_choice not in [0, 1]:
            print("Invalid input")
            print(game_constants.DIVIDER)
            continue

        if intro_choice == 0:
            print("Goodbye")
            print(game_constants.DIVIDER)
            break
        elif intro_choice == 1:
            print("Welcome in world of Arcadius")
            print(game_constants.DIVIDER)
            break
