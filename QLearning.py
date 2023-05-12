import numpy as np

# rewards
WIN_VALUE = 1.0
LOSS_VALUE = 0.0 
TIED_VALUE = 0.5

alpha=0.9 # learning rate
gamma=0.95 # discount factor
q_init=0.6 # init q table

class PlayQlearning():
    def __init__(self, player):
        self.QTable = {}
        self.history = []
        self.player = 1
        self.opponent = 2
        if (player == 2):
            self.opponent = 1
            self.player = 2

    def checkWinner(self, the_board):
        # has winner
        for i in range(3):
            if (the_board[i][0]!=0 and the_board[i][1]==the_board[i][0] and the_board[i][2]==the_board[i][0]):
                return the_board[i][0]
            elif (the_board[0][i]!=0 and the_board[1][i]==the_board[0][i] and the_board[2][i]==the_board[0][i]):
                return the_board[0][i]
        if (the_board[1][1]!=0 and ((the_board[0][0]==the_board[1][1] and the_board[2][2]==the_board[1][1]) or (the_board[0][2]==the_board[1][1] and the_board[2][0]==the_board[1][1]))):
            return the_board[1][1]
        # no winner
        for i in range(3):
            for j in range(3):
                if the_board[i][j] == 0:
                    return 0
        # tied
        return 3

    # give the np board a special index
    def indexBoard(self, the_board):
        index = 0
        for i in range(3):
            for j in range(3):
                index += the_board[i][j]
                index *= 10
        index = int(index)
        return index

    def getQValue(self, board_index):
        if board_index in self.QTable:
            value = self.QTable[board_index]
        else:
            value = q_init*np.ones((3,3))
            self.QTable[board_index] = value
        return value
    
    def getQTable(self):
        return self.QTable

    def checkPosAvaliable(self, x, y, the_board):
        if x<0 or x>2 or y<0 or y>2:
            return False
        if the_board[x][y] != 0:
            return False
        return True

    def findBestMove(self, the_board):
        # get the max pos
        boardIndex = self.indexBoard(the_board)
        qValue = self.getQValue(boardIndex)
        while True:
            maxIndex = np.argmax(qValue) # get the max value
            if self.checkPosAvaliable(maxIndex//3, maxIndex%3, the_board):
                break
            else:
                qValue[maxIndex//3, maxIndex%3] = -1.0

        self.history.append((boardIndex, maxIndex))
        #the_board[maxIndex//3, maxIndex%3] = self.player

        return maxIndex//3, maxIndex%3

    def finalResult(self, winner):
        if winner == 3:
            final_value = TIED_VALUE
        elif winner == self.player:
            final_value = WIN_VALUE
        elif winner == self.opponent:
            final_value = LOSS_VALUE

        self.history.reverse()
        next_max = -1.0
        for h in self.history:
            qValue = self.getQValue(h[0])
            if next_max < 0:  # first loop
                qValue[h[1]//3, h[1]%3] = final_value
            else:
                qValue[h[1]//3, h[1]%3] = qValue[h[1]//3, h[1]%3] * (1.0-alpha) + alpha * gamma * next_max

            next_max = qValue.max()
            #self.QTable[h[0]] = qValue
    
    def newGame(self):
        self.history = []