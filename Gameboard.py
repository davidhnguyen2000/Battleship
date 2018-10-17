from __future__ import print_function
OPEN_SPACE_CHAR = "*"
BATTLESHIP_CHAR = "@"
class Gameboard:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.board = [[]]
        for yCoor in range(size):
            self.board.append([])
            for xCoor in range(size):
                self.board[yCoor].append(xCoor)
                self.board[yCoor][xCoor] = OPEN_SPACE_CHAR

    def setName(self, newName):
        self.name = newName
        return

    def setSize(self, newSize):
        self.size = newSize
        return

    def displayGameboard(self):
        print('  0 1 2 3 4 5 6 7 8 9')
        for y in range(self.size):
            print(y, end=' ')
            for x in range(self.size):
                print(self.board[x][y], end=' ')
            print()
        return

    def placeBoat(self, xPos, yPos, direction, boatSize):
        noShip = True
        onBoard = True
        if self.board[xPos][yPos] == OPEN_SPACE_CHAR:  # starts placement of the boat if there is a free space
            if direction == 0 or direction == 2:
                if direction == 0:
                    direction2 = -1
                else:
                    direction2 = 1
                for xCoor in range(self.size):  # check if boat placement is good
                    newXCoor = xPos + direction2 * xCoor
                    onBoard = newXCoor < self.size and newXCoor >= 0
                    if onBoard:
                        noShip = self.board[newXCoor][yPos] == OPEN_SPACE_CHAR
                    if not noShip or not onBoard:
                        return False
                if noShip and onBoard:  # places boat
                    for xCoor in range(boatSize):
                        newXCoor = xPos + direction2 * xCoor
                        self.board[newXCoor][yPos] = BATTLESHIP_CHAR
                        # print('placed something')
            elif direction == 1 or direction == 3:
                if direction == 1:
                    direction2 = -1
                else:
                    direction2 = 1
                for yCoor in range(self.size):  # check if boat placement is good
                    newYCoor = yPos + direction2 * yCoor
                    onBoard = newYCoor < self.size and newYCoor >= 0
                    if onBoard:
                        noShip = self.board[xPos][newYCoor] == OPEN_SPACE_CHAR
                    if not noShip or not onBoard:
                        # print('failed placement')
                        return False
                if noShip and onBoard:  # places boat
                    for yCoor in range(boatSize):
                        newYCoor = yPos + direction2 * yCoor
                        self.board[xPos][newYCoor] = BATTLESHIP_CHAR
                        # print('placed something')
            return True
        else:
            return False
