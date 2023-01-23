import pygame
import pygame.math

import Game

# PYGame Initialisieren
pygame.init()
# Grösse festlegen
game = Game.Game()

# Start Loop
game.loop()

# Close the window and quit.
pygame.quit()
