from phase import main_menu
from phase.intro import intro
from phase.name import set_nickname
from phase import hero_abilities
from phase import phase_constants


current_phase = phase_constants.INTRO

while True:
    if current_phase == phase_constants.INTRO:
        current_phase = intro()
    elif current_phase == phase_constants.END:
        break
    elif current_phase == phase_constants.NAME:
        current_phase = set_nickname()
    elif current_phase == phase_constants.MENU:
        current_phase = main_menu.menu()
    elif current_phase == phase_constants.ABILITIES:
        current_phase = hero_abilities.abilities_assign()
