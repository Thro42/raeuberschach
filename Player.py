#from Color 
import Color
#from Game 
import Game
from Piece import Piece


class Player():
    xposmap =["a","b","c","d","e","f","g","h"]
    def __init__(self, game: Game, color_short: str):
        self.game = game
        self.color_short = color_short
        self.color = Color.Color(game, self, color_short )
        self.selectPiece = None
    
    def movePiece(self, piece: Piece, end: str ):
        #fromPlace = self.piece.place
        fieldColor = self.game.board.getColor4Field(end)
        if fieldColor != "-" and fieldColor != self.color_short:
            self.game.hitPiecAt(self, end)
        self.game.board.movePiece(piece, end)
        piece.setAlphaPos(end)
        piece.select(False)

    def hitPieceAtPlace(self, place: str):
        self.color.hitPieceAt(place)

    def selectPieceAtXY(self, x, y):
        print(self.color_short, x,y)
        xpos = self.xposmap[x]
        ypos = str(y)
        place = xpos + ypos
        piece = self.color.getPieceAt(place)
        if piece != None:
            if piece != self.selectPiece:
                if self.selectPiece != None:
                    self.selectPiece.select(False)
            if piece.is_selcted:
                select = False
                self.selectPiece = None
            else:
                select = True
                self.selectPiece = piece
            piece.select(select)
        else:
            if self.selectPiece != None:
                if self.selectPiece.isPossibleField(place):
                    self.movePiece(self.selectPiece, place)
                    self.game.whitePlay = False
                #self.selectPiece.moveToPossibleFields(place)

    def draw(self):
        for xpos in self.xposmap:
            for y in range(1,9):
                place = xpos + str(y)
                piece = self.color.getPieceAt(place)
                if piece != None:
                    piece.draw()

    def loop(self):
        self.draw()
        