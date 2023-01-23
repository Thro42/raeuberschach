#from Piece 
import Piece

class Field:
    def __init__(self, place, colorName, pieceName):
        self.place = place
        self.colorName = colorName
        self.pieceName = pieceName
        self.piece = None

    def setPiece(self, piece: Piece.Piece):
        self.piece = piece
        if piece != None:
            self.colorName = piece.color.short
            self.pieceName = piece.pieceName
        else:
            self.colorName = ""
            self.pieceName = ""
    