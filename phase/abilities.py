from game_constants import DIVIDER


abilities = {
    "Damage": {
        "points": 1,
        "description": "Damage is needed when attacking."
    },
    "Defense": {
        "points": 1,
        "description": "Defense is calculating by defense + dexterity."
    },
    "Dexterity": {
        "points": 1,
        "description": "Dexterity is important when defending and damaging."
    },
    "Skill": {
        "points": 1,
        "description": "SKill is important when damage and when crit damage."
    },
    "Health": {
        "points": 50,
        "description": "Health can be restored after every fight."
    },
    "Luck": {
        "points": 1,
        "description": "Luck is important for crit damage."
    }
}


def print_abilities():
    while True:
        print("This is your abilities: ")
        for ability, details in abilities.items():
            print(f"{ability}: {details['points']} points")
        break


def abilities_assign():
    first_assign = 7
    while first_assign > 0:
        print(f"You have {first_assign} points to assign")
        print_abilities()
        assign_input = int(input("What you want upgrade? "))

        if assign_input not in [1, 2, 3, 4, 5, 6]:
            print("Invalid input")
            print(DIVIDER)
            continue

        if assign_input == 1:
            abilities["Damage"]["points"] += 1
            first_assign -= 1
        elif assign_input == 2:
            abilities["Defense"]["points"] += 1
            first_assign -= 1
        elif assign_input == 3:
            abilities["Dexterity"]["points"] += 1
            first_assign -= 1
        elif assign_input == 4:
            abilities["Skill"]["points"] += 1
            first_assign -= 1
        elif assign_input == 5:
            abilities["Health"]["points"] += 5
            first_assign -= 1
        elif assign_input == 6:
            abilities["Luck"]["points"] += 1
            first_assign -= 1

        print("You have assigned all your points.")
        print(DIVIDER)
