#from Color 
import Color
#from Piece 
import Piece


class Pawn(Piece.Piece):
    def __init__(self, color: Color, place: str):
        super(Pawn, self).__init__(color, place, color.images.pawn)
        self.pieceName = "pawn"

    def selectWhite(self):
        if self.place_y < 7:
            field = self.getPlace(self.place_x,self.place_y+1)
            fieldColor = self.boardmap.getFieldColor(field)
            #fieldColor = self.game.board.getColor4Field(field)
            if fieldColor == "-":
                self.possibleFields.append(field)
        if self.place_y == 1:
            field = self.getPlace(self.place_x,self.place_y+2)
            fieldColor = self.boardmap.getFieldColor(field)
            #fieldColor = self.game.board.getColor4Field(field)
            if fieldColor == "-":
                self.possibleFields.append(field)
        if self.place_x < 7:
            field = self.getPlace(self.place_x+1,self.place_y+1)
            fieldColor = self.boardmap.getFieldColor(field)
            #fieldColor = self.game.board.getColor4Field(field)
            #print(field, "-", fieldColor)
            if fieldColor != "-" and fieldColor != self.color.short:
                self.possibleFields.append(field)
        if self.place_x > 0:
            field = self.getPlace(self.place_x-1,self.place_y+1)
            fieldColor = self.boardmap.getFieldColor(field)
            #fieldColor = self.game.board.getColor4Field(field)
            #print(field, "-", fieldColor)
            if fieldColor != "-" and fieldColor != self.color.short:
                self.possibleFields.append(field)

    def selectBlack(self):
        if self.place_y > 0:
            field = self.getPlace(self.place_x,self.place_y-1)
            fieldColor = self.boardmap.getFieldColor(field)
            if fieldColor == "-":
                self.possibleFields.append(field)
        if self.place_y == 6:
            field = self.getPlace(self.place_x,self.place_y-2)
            fieldColor = self.boardmap.getFieldColor(field)
            if fieldColor == "-":
                self.possibleFields.append(field)
        if self.place_x < 7 and self.place_y > 0:
            field = self.getPlace(self.place_x+1,self.place_y-1)
            fieldColor = self.boardmap.getFieldColor(field)
            #print(field, "-", fieldColor)
            if fieldColor != "-" and fieldColor != self.color.short:
                self.possibleFields.append(field)
        if self.place_x > 0 and self.place_y > 0:
            field = self.getPlace(self.place_x-1,self.place_y-1)
            fieldColor = self.boardmap.getFieldColor(field)
            #print(field, "-", fieldColor)
            if fieldColor != "-" and fieldColor != self.color.short:
                self.possibleFields.append(field)

    def select(self, select):
        super(Pawn, self).select(select)
        self.possibleFields = []
        if self.color_short == "w":
            self.selectWhite()
        else:
            self.selectBlack()
        #self.game.board.printBord()
        #print(self.place_x, self.place_y, self.possibleFields)

