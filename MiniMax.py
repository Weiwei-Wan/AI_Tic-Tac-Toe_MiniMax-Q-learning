def miniMaxAlgo(the_player, board):
    global player, opponent
    player = 1
    opponent = 2
    if (the_player == 2):
        opponent = 1
        player = 2
    return findBestMove(board)
            
def checkWinner(the_board):
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

def miniMax(the_board, depth, isMax, alpha, beta):
    score = 0
    if checkWinner(the_board) == 3: # tied
        return 0
    elif checkWinner(the_board) == player: # win
        score = 10
        return score
    elif checkWinner(the_board) == opponent: # lose
        score = -10
        return score

    if isMax:	
        best = -1000
        for i in range(3) :		
            for j in range(3) :
                if (the_board[i][j]==0) :
                    the_board[i][j] = player
                    new_best = max(best, miniMax(the_board, depth + 1, not isMax, alpha, beta))
                    the_board[i][j] = 0
                    # alpha-beta pruning
                    if new_best > best:
                        best = new_best
                    if best >= beta:
                        return best
                    if best > alpha:
                        alpha = best
        return new_best
    else:
        best = 1000
        for i in range(3) :		
            for j in range(3) :
                if (the_board[i][j] == 0) :
                    the_board[i][j] = opponent
                    new_best = min(best, miniMax(the_board, depth + 1, not isMax, alpha, beta))
                    the_board[i][j] = 0
                    # alpha-beta pruning
                    if new_best < best:
                        best = new_best
                    if best <= alpha:
                        return best
                    if best < beta:
                        beta = best
        return new_best

def findBestMove(the_board) :
    bestVal = -1000
    bestMove = (-1, -1)
    for i in range(3):	
        for j in range(3):
            if (the_board[i][j] == 0) :
                # move
                the_board[i][j] = player
                moveVal = miniMax(the_board, 0, False, -1000, 1000)
                #print(moveVal)
                the_board[i][j] = 0
                if (moveVal > bestVal):				
                    bestMove = (i, j)
                    bestVal = moveVal
    return bestMove