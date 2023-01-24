
#import copy
from copy import copy, deepcopy

import Game

# Grösse festlegen
game = Game.Game()

print(id(game.board.boardmap))
cmap = deepcopy(game.board.boardmap)
print(id(cmap))
game.board.boardmap.printBord()
cmap.clearFieldColor("a1")
cmap.printBord()
game.board.boardmap.printBord()
