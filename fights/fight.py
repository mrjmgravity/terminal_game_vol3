from phase import hero_data
import enemy_data


def fighting():
    while True:
        print("The fight begins\n")
        print(f"You are attacking with{hero_data.damage}")
        enemy_data.enemy_health -= hero_data.damage


