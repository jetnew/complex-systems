from classes import *
from builders import *

game = Game(size=(100,100))

# game.board[10:13, 10:13] = glider()
game.board[1:10, 1:37] = glider_gun()
# game.render(frames=100, speed=50)
game.record(frames=100, speed=50)
