from phase.intro import intro
from phase.name import set_nickname
from phase.abilities import abilities_assign


if intro():
    set_nickname()
    abilities_assign()
else:
    pass

