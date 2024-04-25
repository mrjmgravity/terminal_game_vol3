from phase import hero_data
from phase import hero_abilities


def save_game(next_phase):
    print("How do you want to save? ")
    while True:
        save_name = input("name: ")
        if save_name.isalpha():
            file_path = "saved/" + save_name + ".txt"
            file_handler = open(file_path, "w", encoding="utf-8")
            file_handler.write(hero_data.hero_name + "\n")
            for k, v in hero_abilities.abilities.items():
                file_handler.write(k + " - " + str(v["points"]) + "\n")
            file_handler.write(next_phase + "\n")
            file_handler.close()
            print("Successful saved game")
            break
        else:
            print("Invalid input, try different name")
            continue
