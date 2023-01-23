#from Color 
import Color
#from Piece 
import Piece


class Queen(Piece.Piece):
    def __init__(self, color: Color, place: str):
        super(Queen, self).__init__(color, place, color.images.queen)
        self.pieceName = "queen"

    def select(self, select):
        super(Queen, self).select(select)
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
#
        do_next = True
        test_x = self.place_x
        test_y = self.place_y
        while do_next:
            test_y += 1
            if test_y < 8:
                do_next = self.addPossibleFieldAtPlace(test_x,test_y)
            else:
                do_next = False
        do_next = True
        test_x = self.place_x
        test_y = self.place_y
        while do_next:
            test_y -= 1
            if test_y >= 0:
                do_next = self.addPossibleFieldAtPlace(test_x,test_y)
            else:
                do_next = False
        do_next = True
        test_x = self.place_x
        test_y = self.place_y
        while do_next:
            test_x += 1
            if test_x < 8:
                do_next = self.addPossibleFieldAtPlace(test_x,test_y)
            else:
                do_next = False
        do_next = True
        test_x = self.place_x
        test_y = self.place_y
        while do_next:
            test_x -= 1
            if test_x >= 0:
                do_next = self.addPossibleFieldAtPlace(test_x,test_y)
            else:
                do_next = False
