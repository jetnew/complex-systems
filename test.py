from classes import *
from builders import *

game = Game(size=(100, 100))

# Glider
game.add_agent((0,0))
game.add_agent((1,1))
game.add_agent((2,1))
game.add_agent((0,2))
game.add_agent((1,2))

# Blinker
# game.add_agent((1,0))
# game.add_agent((1,1))
# game.add_agent((1,2))

game.render(speed=50)