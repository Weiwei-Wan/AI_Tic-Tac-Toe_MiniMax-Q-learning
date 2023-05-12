import numpy as np

class Board():
    def __init__(self):
        self.board = np.zeros((3,3))

    def playerMove(self, x, y, player):
        if self.board[x,y]==0:
            self.board[x,y] = player
    
    def getBoard(self):
        return self.board

    # 0: no winner, go on #1: player1 win #2: player2 win #3: tied game
    def checkWinner(self):
        # has winner
        for i in range(3):
            if (self.board[i][0]!=0 and self.board[i][1]==self.board[i][0] and self.board[i][2]==self.board[i][0]):
                return self.board[i][0]
            elif (self.board[0][i]!=0 and self.board[1][i]==self.board[0][i] and self.board[2][i]==self.board[0][i]):
                return self.board[0][i]
        if (self.board[1][1]!=0 and ((self.board[0][0]==self.board[1][1] and self.board[2][2]==self.board[1][1]) or (self.board[0][2]==self.board[1][1] and self.board[2][0]==self.board[1][1]))):
            return self.board[1][1]
        # no winner
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return 0
        # tied
        return 3
