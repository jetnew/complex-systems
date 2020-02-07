from classes import *
from builders import *

game = Game(size=(250, 250))

# Glider
# glider = [Agent((0,0)),
#           Agent((1,1)),
#           Agent((2,1)),
#           Agent((0,2)),
#           Agent((1,2))]
#
# for a in glider:
#     game.add_agent(a)

import random
for i in range(250):
    for j in range(250):
        if random.randint(0,10) < 2:
            game.add_agent(Agent((i,j)))
game.update_board()
game.render(speed=50, frames=(600,600))