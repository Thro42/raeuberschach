#from Color 
import Color
#from Piece 
import Piece


class Rook(Piece.Piece):
    def __init__(self, color: Color, place: str):
        super(Rook, self).__init__(color, place, color.images.rook)
        self.pieceName = "rook"

    def select(self, select):
        super(Rook, self).select(select)
        self.possibleFields = []
        do_next = True
        y_start = self.place_y
        while do_next:
            y_start += 1
            if y_start < 8:
                do_next = self.addPossibleFieldAtPlace(self.place_x,y_start)
            else:
                do_next = False
        do_next = True
        y_start = self.place_y
        while do_next:
            y_start -= 1
            if y_start >= 0:
                do_next = self.addPossibleFieldAtPlace(self.place_x,y_start)
            else:
                y_end = False
        do_next = True
        x_start = self.place_x
        while do_next:
            x_start += 1
            if x_start < 8:
                do_next = self.addPossibleFieldAtPlace(x_start,self.place_y)
            else:
                do_next = False
        do_next = True
        x_start = self.place_x
        while do_next:
            x_start -= 1
            if x_start >= 0:
                do_next = self.addPossibleFieldAtPlace(x_start,self.place_y)
            else:
                do_next = False
