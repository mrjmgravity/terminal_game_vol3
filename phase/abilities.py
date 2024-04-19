from game_constants import DIVIDER
import hero_data
import phase_constants

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
            print(f"{ability}: {details['points']} points", end=", ")
        break


def abilities_assign():
    hero_data.available_points = 7
    while hero_data.available_points > 0:
        print(f"You have {hero_data.available_points} points to assign")
        print_abilities()
        assign_input = int(input("What you want upgrade? "))

        if assign_input not in [1, 2, 3, 4, 5, 6]:
            print("Invalid input")
            print(DIVIDER)
            continue

        if assign_input == 1:
            abilities["Damage"]["points"] += 1
        elif assign_input == 2:
            abilities["Defense"]["points"] += 1
        elif assign_input == 3:
            abilities["Dexterity"]["points"] += 1
        elif assign_input == 4:
            abilities["Skill"]["points"] += 1
        elif assign_input == 5:
            abilities["Health"]["points"] += 5
        else:
            abilities["Luck"]["points"] += 1
        hero_data.available_points -= 1

        print("You have assigned all your points.")
        print(DIVIDER)


def remove_ability():
    hero_data.available_points = 0
    while True:
        print_abilities()
        remove_input = input("\nWhich ability you want to remove? ")

        if remove_input not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid input")
            print(DIVIDER)
            continue

        if remove_input == "1":
            abilities["Damage"]["points"] -= 1
        elif remove_input == "2":
            abilities["Defense"]["points"] -= 1
        elif remove_input == "3":
            abilities["Dexterity"]["points"] -= 1
        elif remove_input == "4":
            abilities["Skill"]["points"] -= 1
        elif remove_input == "5":
            abilities["Health"]["points"] -= 5
        else:
            abilities["Luck"]["points"] -= 1
        hero_data.available_points += 1
        print(DIVIDER)

        print("0 - Back to the menu")
        print("1 - Remove one more point")
        print("2 - Assign ability")
        again_input = input("Do you want remove one more point? ")

        if again_input not in ["0", "1", "2"]:
            print("Invalid input")
            continue

        if again_input == "0":
            return phase_constants.MENU
        elif again_input == "1":
            return remove_ability()
        else:
            abilities_assign()
