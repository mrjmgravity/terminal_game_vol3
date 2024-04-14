from game_constants import DIVIDER


def set_nickname():
    while True:
        name_input = input("What is your nickname? ")
        print(f"Is this your nickname? {name_input}")
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
            print(f"Hello {name_input}")
            print(DIVIDER)
            break
