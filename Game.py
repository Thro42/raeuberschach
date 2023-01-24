import pygame
import pygame.math

from Board import Board
from Color import Color
from ColorFigures import ColorFigures
from Computer import Computer
from Player import Player

class Game():
    colorWhite = None
    colorBlack = None
    player = None
    computer = None
    
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
        self.TheComputer = Computer(self, self.blackPlayer, self.whitePlayer)
        
    def loadImages(self, color: ColorFigures):
        path = "images/"+ color.short

    def hitPiecAt(self, player: Player, pos):
        if player == self.whitePlayer:
            self.blackPlayer.hitPieceAtPlace(pos)
        else:
            self.whitePlayer.hitPieceAtPlace(pos)

    def selectPieceAt(self, pos):
        # print(pos)
        xpos = int(pos[0]/100)
        ypos = 8 - int(pos[1]/100)
        if self.whitePlay:
            #self.board.boardmap.printBord()            
            self.whitePlayer.selectPieceAtXY(xpos,ypos)

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


    def  loop(self):
        while not self.game_over:
            self.HandleKeybord()
            self.board.drawBoard()
            self.whitePlayer.loop()
            self.blackPlayer.loop()
            pygame.display.update()
            self.TheComputer.loop()
            pygame.display.update()
            self.clock.tick(60)
