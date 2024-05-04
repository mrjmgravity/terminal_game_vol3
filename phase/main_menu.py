import enemies_abilities
import game_constants
from phase import hero_abilities
from phase.save_load import save_game
from phase import phase_constants
from fight import battle


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
            if not enemies_abilities.enemies[1]["is_dead"]:
                battle.battleground(1)
            elif not enemies_abilities.enemies[2]["is_dead"]:
                battle.battleground(2)
            elif not enemies_abilities.enemies[3]["is_dead"]:
                battle.battleground(3)
            elif not enemies_abilities.enemies[4]["is_dead"]:
                battle.battleground(4)
            elif not enemies_abilities.enemies[5]["is_dead"]:
                battle.battleground(5)
            else:
                menu()

        elif menu_input == 1:
            hero_abilities.remove_ability()
            return phase_constants.MENU
        elif menu_input == 2:
            save_game(phase_constants.MENU)
        elif menu_input == 3:
            print("Goodbye")
            print(game_constants.DIVIDER)
            return phase_constants.END
        else:
            print("Invalid input")
