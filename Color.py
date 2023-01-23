#from Bishop 
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING: 
    from Game import Game
if TYPE_CHECKING: 
    from Player import Player

from Bishop import Bishop
from ColorFigures import ColorFigures
from King import King
from Knight import Knight
from Pawn import Pawn
from Queen import Queen
from Rook import Rook


class Color():
    
    #pawns = []
    #rook = []
    #knight = []
    #bishop = []
    def __init__(self, game: Game, player: Player, short):
        self.pieces = []
        self.game = game
        self.player = player
        self.short = short
        if self.short == "w":
            r1 = "1"
            r2 = "2"
        else:
            r1 = "8"
            r2 = "7"

        self.images = ColorFigures(short)
        # Bauern
        self.pieces.append(Pawn(self,"a"+r2))
        self.pieces.append(Pawn(self,"b"+r2))
        self.pieces.append(Pawn(self,"c"+r2))
        self.pieces.append(Pawn(self,"d"+r2))
        self.pieces.append(Pawn(self,"e"+r2))
        self.pieces.append(Pawn(self,"f"+r2))
        self.pieces.append(Pawn(self,"g"+r2))
        self.pieces.append(Pawn(self,"h"+r2))
        # Türme
        self.pieces.append(Rook(self, "a"+r1))
        self.pieces.append(Rook(self, "h"+r1))
        # Springer
        self.pieces.append(Knight(self, "b"+r1))
        self.pieces.append(Knight(self, "g"+r1))
        # Läufer
        self.pieces.append(Bishop(self,"c"+r1))
        self.pieces.append(Bishop(self,"f"+r1))
        # Dame
        self.pieces.append(Queen(self,"d"+r1))
        # König
        self.pieces.append(King(self,"e"+r1))

    def getPieceAt(self, place: str):
        thePiece = None
        for piece in self.pieces:
            if piece.place == place:
                thePiece = piece
        return thePiece
    
    def hitPieceAt(self, place: str):
        for piece in self.pieces:
            if piece.place == place:
                self.pieces.remove(piece)
