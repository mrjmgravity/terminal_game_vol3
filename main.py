from phase.intro import intro
from phase.name import set_nickname
from phase.abilities import abilities_assign
from phase import phase_constants
from phase import menu


current_phase = phase_constants.INTRO

while True:
    if current_phase == phase_constants.INTRO:
        current_phase = intro()
    elif current_phase == phase_constants.END:
        break
    elif current_phase == phase_constants.NAME:
        current_phase = set_nickname()
    elif current_phase == phase_constants.MENU:
        current_phase = menu
    elif current_phase == phase_constants.ABILITIES:
        abilities_assign()
        print("Are you ready for your first fight?")
        break
