import time

class Car:
    line = 0
    col = 0
    speed = 1
    direction = "U"
    Finished = False
    filedata = []
    # Constructor method
    def __init__(self):
        self.line = 0
        self.col = 0
        self.TrackInfo = 0
        print("car version: 1.0.0.2")

    def get_trackinfo(self):
        return self.TrackInfo

    def endOfMaze(self):
        # check bounds ot array - stay on track
        #print("Debug: x,y:", self.col, self.line)
        self.TrackInfo = self.filedata[self.line][self.col]
        if self.line > 0 and self.col > 0:
            if self.filedata[self.line][self.col] == "3" or self.filedata[self.line][self.col] == "2":
                self.Finished = True

    def move(self, whichWay):
        # check for collision before allowing the move
        if whichWay == "U":
            if self.lookUp():
                self.moveReal('U')
                self.endOfMaze()
                return True
        if whichWay == "L":
            if self.lookLeft():
                self.moveReal('L')
                self.endOfMaze()
                return True
        if whichWay == "R":
            if self.lookRight():
                self.moveReal('R')
                self.endOfMaze()
            return True
        if whichWay == "D":
            if self.lookDown():
                self.moveReal('D')
                self.endOfMaze()
                return True

        self.endOfMaze()
        return False

    def moveReal(self, way):
        nextpos = self.realposition(way)
        self.direction = way
        self.line = nextpos[0]
        self.col = nextpos[1]

    def lookLeft(self):
        x = self.col - 1
        if x < 0:
            return False
        if self.filedata[self.line][x] == "1":
            return False
        else:
            return True

    def lookRight(self):
        x = self.col + 1
        if x < 0:
            return False
        if self.filedata[self.line][x] == "1":
            return False
        else:
            return True

    def lookDown(self):
        y = self.line + 1
        if self.filedata[y][self.col] == "1":
            return False
        else:
            return True

    def lookUp(self):
        y = self.line - 1
        if self.filedata[y][self.col] == "1":
            return False
        else:
            return True


        return False

    def realposition(self,way):
        if way == 'R':
            return self.line, self.col + 1
        if way == 'L':
            return self.line, self.col - 1
        if way == 'U':
            return self.line - 1, self.col
        if way == 'D':
            return self.line + 1, self.col

    # see if the car is at a junction
    #  there will always be at least one direct return
    #    this would be the existing direction of travel
    # must be related to existing travel direction
    # 100 left
    # 010 ahead
    # 011 right
    def ReadSensor(self):
        time.sleep(0.5)
        junction= [0,0,0]
        if self.lookReal('S'):
            junction[1]=1
        if self.lookReal('L'):
            junction[0]=1
        if self.lookReal('R'):
            junction[2]=1
        return str(junction[0])+str(junction[1]) + str(junction[2])
