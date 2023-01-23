#from Color 
import Color
#from Piece 
import Piece


class King(Piece.Piece):
    def __init__(self, color: Color, place: str):
        super(King, self).__init__(color, place, color.images.king)
        self.pieceName = "king"

    def select(self, select):
        super(King, self).select(select)
        self.possibleFields = []
        do_next = True
        test_x = self.place_x
        test_y = self.place_y
        do_next = self.addPossibleFieldAtPlace(test_x + 1, test_y)
        do_next = self.addPossibleFieldAtPlace(test_x + 1, test_y + 1)
        do_next = self.addPossibleFieldAtPlace(test_x, test_y + 1)
        do_next = self.addPossibleFieldAtPlace(test_x - 1, test_y + 1)
        do_next = self.addPossibleFieldAtPlace(test_x - 1, test_y)
        do_next = self.addPossibleFieldAtPlace(test_x - 1, test_y - 1)
        do_next = self.addPossibleFieldAtPlace(test_x - 1, test_y + 1)
        do_next = self.addPossibleFieldAtPlace(test_x + 1, test_y - 1)
        do_next = self.addPossibleFieldAtPlace(test_x, test_y - 1)
