import random
from TicBoard import Board
import Defalt
import MiniMax
from QLearning import PlayQlearning
import matplotlib.pyplot as plt

def trainQLearning(trainNum):
    playerQ1 = PlayQlearning(1)
    playerQ2 = PlayQlearning(2)
    cnt = 0
    while cnt < trainNum:
        cnt += 1
        # random first player
        Player1First = random.choice([True, False])
        # initialize board
        board = Board()
        playerQ1.newGame()
        playerQ2.newGame()
        # play game to finish
        while board.checkWinner() == 0:
            # First Player
            playerQ = playerQ1 if Player1First else playerQ2
            x1, y1 = playerQ.findBestMove(board.getBoard())
            board.playerMove(x1, y1, 1 if Player1First else 2)
            # game finish
            if board.checkWinner() != 0:
                playerQ1.finalResult(board.checkWinner())
                playerQ2.finalResult(board.checkWinner())
                break
            else:
                # second player
                playerQ = playerQ2 if Player1First else playerQ1
                x2, y2 = playerQ.findBestMove(board.getBoard())
                board.playerMove(x2, y2, 2 if Player1First else 1)
                # game finish
                if board.checkWinner() != 0:
                    playerQ1.finalResult(board.checkWinner())
                    playerQ2.finalResult(board.checkWinner())
                    break
    return playerQ1, playerQ2

def play(player1, player2, loopNum, trainNum):
    player1WinCount = 0
    player2WinCount = 0
    tiedCount = 0
    # if q-learning player
    if player1 == 2 or player2 == 2:
        playerQ1, playerQ2 = trainQLearning(trainNum)
    cnt = 0
    # for the image
    x = []
    player1Win = []
    player2Win = []
    tied = []
    while cnt < loopNum:
        cnt += 1
        # random first player
        Player1First = random.choice([True, False])
        # initialize board
        board = Board()
        if player1 == 2 or player2 == 2:
            playerQ1.newGame()
            playerQ2.newGame()
        # play game to finish
        while board.checkWinner() == 0:
            # First Player
            player = player1 if Player1First else player2
            if player1 == 2 or player2 == 2:
                playerQ = playerQ1 if Player1First else playerQ2
        
            if player == 0:
                x1, y1 = Defalt.defaltAlgo(1 if Player1First else 2, board.getBoard())
            elif player == 1:
                x1, y1 = MiniMax.miniMaxAlgo(1 if Player1First else 2, board.getBoard()) 
            elif player == 2:
                x1, y1 = playerQ.findBestMove(board.getBoard())

            board.playerMove(x1, y1, 1 if Player1First else 2)
            # game finish
            if board.checkWinner() != 0:
                if board.checkWinner() == 3:
                    tiedCount += 1
                elif board.checkWinner() == 1:
                    player1WinCount += 1
                elif board.checkWinner() == 2:
                    player2WinCount += 1
                x.append(cnt)
                player1Win.append(player1WinCount/cnt)
                player2Win.append(player2WinCount/cnt)
                tied.append(tiedCount/cnt)
                break
            else:
                # second player
                player = player2 if Player1First else player1
                if player1 == 2 or player2 == 2:
                    playerQ = playerQ2 if Player1First else playerQ1
                
                if player == 0:
                    x2, y2 = Defalt.defaltAlgo(2 if Player1First else 1, board.getBoard())
                elif player == 1:
                    x2, y2 = MiniMax.miniMaxAlgo(2 if Player1First else 1, board.getBoard()) 
                elif player == 2:
                    x2, y2 = playerQ.findBestMove(board.getBoard())

                board.playerMove(x2, y2, 2 if Player1First else 1)
                # game finish
                if board.checkWinner() != 0:
                    if board.checkWinner() == 3:
                        tiedCount += 1
                    elif board.checkWinner() == 1:
                        player1WinCount += 1
                    elif board.checkWinner() == 2:
                        player2WinCount += 1
                    x.append(cnt)
                    player1Win.append(player1WinCount/cnt)
                    player2Win.append(player2WinCount/cnt)
                    tied.append(tiedCount/cnt)
                    break
    
    plt.plot(x,player1Win,color = 'r',label=["Default Win", "Minimax Win", "Q-Learning Win"][player1])
    plt.plot(x,player2Win,color = 'g',label=["Default Win", "Minimax Win", "Q-Learning Win"][player2])
    plt.plot(x,tied,color = 'b',label="Tied")

    plt.xlabel("Game count")
    plt.ylabel("Probability")
    plt.legend(loc = "upper right")
    plt.show()

# 0: defalt  1: minimax  2:q learning
play(1, 2, 1000, 100000)