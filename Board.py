import pygame
import pygame.math
import sys
from BoardMap import BoardMap
#from ColorFigures 
import ColorFigures
from Field import Field
import Game
import Piece
import Player

class Board:
    xposmap =["a","b","c","d","e","f","g","h"]
    fields = [] # [[],[]]
    def __init__(self, game: Game, breite: int, hoehe: int):
        self.breite = breite
        self.hoehe = hoehe
        self.screen = game.screen
        self.bordImage = pygame.image.load("images/brett.png")
        self.boardmap = BoardMap()
        #self.initBoard()

    def drawBoard(self):
        winRect = pygame.Rect(0, 0, self.breite, self.hoehe)
        self.screen.blit(self.bordImage, winRect)
    
    def initBoard(self):
        for x in range(0,8):
            line = []
            for y in range(0,8):
                xpos = self.xposmap[x]
                place = xpos + str(y+1)
                line.append(Field(place,"",""))
                # self.fields[x][y] = Field(place,"","")
            self.fields.append(line)

    def setPlayer(self, player: Player):
        for p in player.color.pieces:
            color_short = p.color.short
            self.boardmap.setFieldColor(p.place, color_short)

    def set_Player(self,player: Player):
         for x in range(0,8):
            for y in range(1,9):
                xpos = self.xposmap[x]
                place = xpos + str(y)
                piece = player.color.getPieceAt(place)
                if piece != None:
                     self.fields[x][y-1].setPiece(piece)
    
    def getXnum(self, place):
        xname = place[0:1].lower()
        xnum = 0
        place_x = 0
        for f in self.xposmap:
            if xname == f:
                place_x = xnum
            xnum +=1
        return place_x

    def getColor4Field(self, place: str):
        #print(place)
        return self.boardmap.getFieldColor(place)

    def getColor_4Field(self,place: str):
        print("Place",place)
        colorName = ""
        place_x = 0
        place_x = self.getXnum(place)
        place_y = int(place[1:2]) - 1
        print("Place",place,"Field",place_x,place_y)
        if place_x >= 0 and place_x < 8 and place_y >= 0 and place_y < 8:
            colorName = self.fields[place_x][place_y].colorName
        return colorName

    def movePiece(self, piece : Piece, toPlace ):
        self.boardmap.clearFieldColor(piece.place)
        self.boardmap.setFieldColor(toPlace, piece.color.short)

    def move_Piece(self, piece : Piece, toPlace ):
        fromPlace = piece.place
        from_x = self.getXnum(fromPlace)
        from_y = int(fromPlace[1:2]) - 1
        to_x = self.getXnum(toPlace)
        to_y = int(toPlace[1:2]) - 1
        self.fields[from_x][from_y].setPiece(None)
        self.fields[to_x][to_y].setPiece(piece)


    def printBord(self):
        pass
        # self.boardmap.printBord()
        #for y in range(0,8):
        #    for x in range(0,8):
        #        print("[",self.fields[x][y].colorName,"]", end='')
        #    print("\n")
