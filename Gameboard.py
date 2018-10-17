from __future__ import print_function
class Gameboard:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.board = [[]]
        for yCoor in range(size):
            self.board.append([])
            for xCoor in range(size):
                self.board[yCoor].append(xCoor)
                self.board[yCoor][xCoor] = "*"

    def setNmae(self, newName):
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
