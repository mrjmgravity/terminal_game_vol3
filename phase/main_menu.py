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
        print(game_constants.DIVIDER)

        if menu_input not in [0, 1, 2, 3]:
            print("Invalid input")
            continue

        if menu_input == 0:
            for enemy_number, enemy in enemies_abilities.enemies.items():
                if not enemy["is_dead"]:
                    battle.battleground(enemy_number)
                    break
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
