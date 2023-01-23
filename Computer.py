from Color import Color
from Game import Game
from Piece import Piece


class Computer:
    def __init__(self, game: Game, color: Color):
        self.game = game
        self.color = color

    def checkPieceMove(self, piece: Piece):
        arr = [[0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0]]

    def checkMove(self):
        arr = [[0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0]]
        for p in self.color.pieces:
            p.select(False)
            arr[p.pos_x,p.pos_y] = len(p)*0.15
            for pf in p.possibleFields:
                pf
    def loop(self):
        if self.whitePlay != True:

            pass