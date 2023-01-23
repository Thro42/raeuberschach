import pygame
import pygame.math

from Board import Board
from Color import Color
from ColorFigures import ColorFigures
from Player import Player

class Game():
    colorWhite = None
    colorBlack = None
    player = None
    computer = None
    # images_White = ColorFigures("w")
    # images_Black = ColorFigures("b")
    
    def __init__(self):
        self.game_over = False
        size = (800, 800)
        self.screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        self.board = Board(self,800,800)
        self.clock = pygame.time.Clock()
        self.mouseDown = False

        self.whitePlayer = Player(self,"w")
        self.board.setPlayer(self.whitePlayer)
        self.blackPlayer = Player(self,"b")
        self.board.setPlayer(self.blackPlayer)
        self.player = self.whitePlayer
        self.computer = self.blackPlayer
        self.whitePlay = True
        
    def loadImages(self, color: ColorFigures):
        path = "images/"+ color.short

    def hitPiecAt(self, pos):
        self.blackPlayer.hitPieceAtPlace(pos)
        #xpos = int(pos[0]/100)
        #ypos = 8 - int(pos[1]/100)

    def selectPieceAt(self, pos):
        print(pos)
        xpos = int(pos[0]/100)
        ypos = 8 - int(pos[1]/100)
        if self.whitePlay:
            self.whitePlayer.selectPieceAtXY(xpos,ypos)
        # self.blackPlayer.selectPieceAtXY(xpos,ypos)

    def HandleKeybord(self):
        # Tastatur befele verarbeiten
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.mouseDown == False:
                    self.mouseDown = True
                    pos = pygame.mouse.get_pos()
                    self.selectPieceAt(pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouseDown = False
                # pos = pygame.mouse.get_pos()
                #self.selectPieceAt(pos, False)


    def  loop(self):
        while not self.game_over:
            self.HandleKeybord()
            self.board.drawBoard()
            self.whitePlayer.loop()
            self.blackPlayer.loop()
            pygame.display.update()
            self.clock.tick(60)
