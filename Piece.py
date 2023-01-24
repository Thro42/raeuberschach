from __future__ import annotations
from typing import TYPE_CHECKING
import pygame
if TYPE_CHECKING: 
    from Color import Color
#import Game

class Piece:
    xposmap =["a","b","c","d","e","f","g","h"]

    def __init__(self, color: Color, place: str, image):
        self.live = True
        self.is_selcted = False
        self.pieceName = ""
        self.game = color.game
        self.boardmap = color.game.board.boardmap
        self.place = place
        self.place_x = 0
        self.place_y = 0
        self.color = color
        self.color_short = color.short
        self.image = image
        self.setAlphaPos(place)
        self.possibleFields = []

    def setMap(self, map):
        self.boardmap = map

    def setPos(self, place_x, place_y):
        self.place_x = place_x
        self.place_y = place_y

    def setAlphaPos(self, position: str):
        self.place = position
        xName = position[0:1].lower()
        self.place_x = 0
        xnum = 0
        for f in self.xposmap:
            if xName == f:
                self.place_x = xnum
            xnum +=1
        self.place_y = int(position[1:2]) - 1

    def getPlace(self, place_x, place_y):
        place = self.xposmap[place_x] + str(place_y+1)
        return place

    def select(self, select):
        # print(self.color.short, self.pieceName, self.place, select)
        self.is_selcted = select
    
    def drawPossibleFields(self, field):
        xName = field[0:1].lower()
        xnum = 0
        px = 0
        for f in self.xposmap:
            if xName == f:
                px = xnum
            xnum +=1
        py = int(field[1:2]) - 1
        px = px * 100
        py = (7 - py) * 100
        pieceRec = pygame.Rect(px, py, 100, 100)
        s = pygame.Surface((100,100), pygame.SRCALPHA)
        s.fill((0,0,128,64))
        self.game.screen.blit(s, pieceRec)

    def draw(self):
        px = self.place_x * 100
        py = (7 - self.place_y) * 100
        pieceRec = pygame.Rect(px, py, 100, 100)
        if self.is_selcted:
            s = pygame.Surface((100,100), pygame.SRCALPHA)
            s.fill((64,255,64,64))
            self.game.screen.blit(s, pieceRec)
            for field in self.possibleFields:
                self.drawPossibleFields(field)
        self.game.screen.blit(self.image, pieceRec)

    def moveToPossibleFields(self, field):
        for pf in self.possibleFields:
            if pf == field:
                self.game.board.movePiece(self, field)
                self.setAlphaPos(field)
                self.is_selcted = False

    def isPossibleField(self, field):
        isPossible = False
        for pf in self.possibleFields:
            if pf == field:
                isPossible = True
        return isPossible

    def addPossibleFieldAtPlace(self, pos_x, pos_y):
        no_end = True
        if pos_x >= 0 and pos_x < 8 and pos_y >= 0 and pos_y < 8:
            field = self.getPlace(pos_x,pos_y)
            #fieldColor = self.game.board.getColor4Field(field)
            fieldColor = self.boardmap.getFieldColor(field)
            if fieldColor != self.color.short:
                self.possibleFields.append(field)
            if fieldColor != "-":
                no_end = False
        else:
            no_end = False
        return no_end