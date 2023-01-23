import pygame

class ColorFigures:
    king = None
    lady = None
    runner = None
    jumper = None
    tower = None
    pawn = None
    def __init__(self, short):
        self.short = short
        path = "images/"+ short
        self.king = pygame.image.load(path+"K.png")
        self.queen = pygame.image.load(path+"Q.png")
        self.bishop = pygame.image.load(path+"B.png")
        self.knight = pygame.image.load(path+"N.png")
        self.rook = pygame.image.load(path+"R.png")
        self.pawn = pygame.image.load(path+"P.png")


