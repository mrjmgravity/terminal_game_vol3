import phase.phase_constants
from game_constants import DIVIDER


def set_nickname():
    while True:
        hero_name = input("What is your nickname? ")
        print(DIVIDER)
        print(f"Is this your nickname? {hero_name}")
        print("0 - Change the nickname\n1 - Confirm the nickname")
        name_choice = int(input("Choose one: "))

        if name_choice not in [0, 1]:
            print("Invalid input")
            print(DIVIDER)
            continue

        if name_choice == 0:
            print(DIVIDER)
            continue
        elif name_choice == 1:
            print(f"Hello {hero_name}")
            print(DIVIDER)
            return phase.phase_constants.ABILITIES
