import random

def defaltAlgo(the_player, board):
    global player, opponent
    player = 1
    opponent = 2
    if (the_player == 2):
        opponent = 1
        player = 2

    player_count = 0
    emplty_count = 0
    opponent_count = 0
    temp_x = -1
    temp_y = -1
    # check row player win
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                emplty_count += 1
                temp_x = i
                temp_y = j
            elif board[i][j] == player:
                player_count += 1
            elif board[i][j] == opponent:
                opponent_count += 1
        if ((player_count == 2 or opponent_count==2) and emplty_count == 1):
            return temp_x, temp_y
    # check column player win
    player_count = 0
    opponent_count = 0
    emplty_count = 0
    for j in range(3):
        for i in range(3):
            if board[i][j] == 0:
                emplty_count += 1
                temp_x = i
                temp_y = j
            elif board[i][j] == player:
                player_count += 1
            elif board[i][j] == opponent:
                opponent_count += 1
        if ((player_count == 2 or opponent_count==2) and emplty_count == 1):
            return temp_x, temp_y
    # check diagonals player win
    player_count = 0
    opponent_count = 0
    emplty_count = 0
    for i in range(3):
        if board[i][i] == 0:
            emplty_count += 1
            temp_x = i
            temp_y = i
        elif board[i][i] == player:
            player_count += 1
        elif board[i][i] == opponent:
            opponent_count += 1
        if ((player_count == 2 or opponent_count==2) and emplty_count == 1):
            return temp_x, temp_y
    for i in range(3):
        if board[i][2-i] == 0:
            emplty_count += 1
            temp_x = i
            temp_y = i
        elif board[i][2-i] == player:
            player_count += 1
        elif board[i][2-i] == opponent:
            opponent_count += 1
        if ((player_count == 2 or opponent_count==2) and emplty_count == 1):
            return temp_x, temp_y
    
    choices = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                choices.append(i*3+j)
    last_choice = random.choice(choices)

    return last_choice//3, last_choice%3
    