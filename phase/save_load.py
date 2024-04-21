from phase.name import set_nickname
from phase import abilities


def save_game(next_phase):
    while True:
        save_name = input("How do you want to save the game? ")
        if save_name.isalpha():
            file_path = "C:/saved_games/" + save_name + ".txt"
            file_handler = open(file_path, "w", encoding="utf-8")
            file_handler.write(set_nickname().name_input)
            file_handler.write("\n")

            for k, v in abilities.abilities():
                file_handler.write(str(k) + ' - ' + str(v["points"]))
                file_handler.write("\n")

            file_handler.write(next_phase)
            file_handler.write("\n")
            file_handler.close()
            print("Game is saved")
            print()
            break
        else:
            print("Invalid name, you have to type words only")
            continue
