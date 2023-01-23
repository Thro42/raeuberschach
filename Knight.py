#from Color 
import Color
#from Piece 
import Piece


class Knight(Piece.Piece):
    def __init__(self, color: Color, place: str):
        super(Knight, self).__init__(color, place, color.images.knight)
        self.pieceName = "knight"

    def select(self, select):
        super(Knight, self).select(select)
        self.possibleFields = []
        test_x = self.place_x + 1
        test_y = self.place_y + 2
        p_end = self.addPossibleFieldAtPlace(test_x,test_y)
        test_x = self.place_x - 1
        test_y = self.place_y + 2
        p_end = self.addPossibleFieldAtPlace(test_x,test_y)
        test_x = self.place_x + 1
        test_y = self.place_y - 2
        p_end = self.addPossibleFieldAtPlace(test_x,test_y)
        test_x = self.place_x - 1
        test_y = self.place_y - 2
        p_end = self.addPossibleFieldAtPlace(test_x,test_y)
        #
        test_x = self.place_x + 2
        test_y = self.place_y + 1
        p_end = self.addPossibleFieldAtPlace(test_x,test_y)
        test_x = self.place_x - 2
        test_y = self.place_y + 1
        p_end = self.addPossibleFieldAtPlace(test_x,test_y)
        test_x = self.place_x + 2
        test_y = self.place_y - 1
        p_end = self.addPossibleFieldAtPlace(test_x,test_y)
        test_x = self.place_x - 2
        test_y = self.place_y - 1
        p_end = self.addPossibleFieldAtPlace(test_x,test_y)

