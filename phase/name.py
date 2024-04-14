

def set_nickname():
    while True:
        name_input = input("What is your nickname? ")
        print(f"Is this your nickname? {name_input}")
        name_choice = input("0 - Change the nickname\n1 - Confirm the nickname")

        if name_choice not in [0, 1]:
            print("Invalid input")
            continue

        if name_choice == 0:
            name_input = input("What is your nickname? ")
            break
        elif name_choice == 1:
            print(f"Hello {name_input}")
            break

