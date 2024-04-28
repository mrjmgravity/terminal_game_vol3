from phase import hero_data
from phase import hero_abilities
from os import listdir


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
            file_handler.write(str(hero_data.available_points+"\n"))
            file_handler.close()
            print("Successful saved game")
            break
        else:
            print("Invalid input, try different name")
            continue


def load(save):
    print(f"Loading save {save.replace(".txt", "")}")

    file_handler = open("saved/" + save, "r", encoding="utf-8")

    name_loaded = False
    abilities_loaded = False
    ability_loaded_counter = 0
    next_phase = ""
    next_phase_loaded = False
    available_points_loaded = False

    for file in file_handler:
        file = file.rstrip()
        if not name_loaded:
            hero_name = file.rstrip()
            hero_data.hero_name = hero_name
            name_loaded = True
        elif not abilities_loaded:
            ability_key, points = file.split(" - ")
            hero_abilities.abilities[ability_key]["points"] = int(points)
            ability_loaded_counter += 1
            if ability_loaded_counter == len(hero_abilities.abilities):
                abilities_loaded = True
        elif not next_phase_loaded:
            next_phase = file
            next_phase_loaded = True
        elif not available_points_loaded:
            hero_data.available_points = int(file)
            available_points_loaded = True
    return True, next_phase


def load_game():
    saved_list = []
    for item in listdir("saved"):
        saved_list.append(item)

    if len(saved_list) > 0:
        print("0 - Back")
        for i, save in enumerate(saved_list):
            print(str(i + 1) + " - " + save.replace(".txt", ""))

        while True:
            save_input = input("What do you want to load? ")
            if save_input == "0":
                return False, ""

            if not save_input.isdigit() or int(save_input) not in list(range(1, len(saved_list) + 1)):
                print("Invalid input")
                continue
            else:
                game_to_load = saved_list[int(save_input) - 1]
                return load(game_to_load)

    else:
        print("No saved games")
        return False, ""
