

class BoardMap:
    xposmap =["a","b","c","d","e","f","g","h"]
    def __init__(self):
        self.fields = [ ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"]]

    def getFieldPos(self,place: str):
        # print("getFieldPos:",place)
        xName = place[0:1].lower()
        xnum = 0
        px = 0
        for f in self.xposmap:
            if xName == f:
                px = xnum
            xnum +=1
        py = int(place[1:2]) - 1
        return (px, py)

    def setFieldColor(self, place: str, color: str):
        pos = self.getFieldPos(place)
        self.fields[pos[0]][pos[1]] = color

    def clearFieldColor(self, place: str):
        pos = self.getFieldPos(place)
        self.fields[pos[0]][pos[1]] = "-"

    def getFieldColor(self, place: str):
        pos = self.getFieldPos(place)
        if pos[0] < 8 and pos[1] < 8:
            return self.fields[pos[0]][pos[1]]
        else:
            return "-"

    def printBord(self):
        for y in range(0,8):
            for x in range(0,8):
                print("[",self.fields[x][y],"]", end='')
            print("\n")
