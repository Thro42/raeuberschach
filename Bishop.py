from __future__ import annotations
from typing import TYPE_CHECKING
import pygame
if TYPE_CHECKING: 
    from Color import Color
#if TYPE_CHECKING:
from Piece import Piece


class Bishop(Piece):
    def __init__(self, color: Color, place: str):
        super(Bishop, self).__init__(color, place, color.images.bishop)
        self.pieceName = "bishop"

    def select(self, select):
        super(Bishop, self).select(select)
        self.possibleFields = []
        do_next = True
        test_x = self.place_x
        test_y = self.place_y
        while do_next:
            test_x += 1
            test_y += 1
            if test_x < 8 and test_y < 8:
                do_next = self.addPossibleFieldAtPlace(test_x,test_y)
            else:
                do_next = False
        do_next = True
        test_x = self.place_x
        test_y = self.place_y
        while do_next:
            test_x += 1
            test_y -= 1
            if test_x < 8 and test_y < 8:
                do_next = self.addPossibleFieldAtPlace(test_x,test_y)
            else:
                do_next = False
        do_next = True
        test_x = self.place_x
        test_y = self.place_y
        while do_next:
            test_x -= 1
            test_y += 1
            if test_x < 8 and test_y < 8:
                do_next = self.addPossibleFieldAtPlace(test_x,test_y)
            else:
                do_next = False
        do_next = True
        test_x = self.place_x
        test_y = self.place_y
        while do_next:
            test_x -= 1
            test_y -= 1
            if test_x < 8 and test_y < 8:
                do_next = self.addPossibleFieldAtPlace(test_x,test_y)
            else:
                do_next = False
