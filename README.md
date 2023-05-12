# AI_Tic-Tac-Toe_MiniMax-Q-learning

The default algorithm is a method which would check if there is any possibility of winning or losing for the current step first of all. If there is an empty position could make the default player win or lose, the default player would occupy this position. If not, the default player would choose a random position from all of the empty positions.


# Minimax playing against default opponent

Here, I set Minimax and the default algorithm as two players to play the Tic tac Toe game. To count the win probability, a total of 1000 games were played, and which player plays first is random in each game. And the results are shown below, the default player couldn’t win any games, the Minimax win probability is near 80% and the tied game probability is near 20%. This result proves that miniMax can never lose.

![1](https://github.com/Weiwei-Wan/AI_Tic-Tac-Toe_MiniMax-Q-learning/assets/74362292/5c0c94b3-4e79-4063-b25d-39cb235e99de)


# Tabular Q-learning playing against default opponent

For Tic Tac Toe, there are 958 final boards and 4520 not final boards. If we want our Q-learning algorithm to have good performance, we need to train enough games to make our Q table big enough to cover more boards. Here, I tried several training games from 10 to 100,000. After the training, the Q-learning algorithm player with the trained Q table would play 1000 games with the default player,  which player plays first is also random in each game. The results are shown below. It’s obvious that if the number of training games is more than 30,000, the opponent default algorithm can never win. I also checked the Q table size, and it’s near the max value 4520. Here, because the training speed is very fast, I’ll use 100,000 as training numbers for each comparison.

![2](https://github.com/Weiwei-Wan/AI_Tic-Tac-Toe_MiniMax-Q-learning/assets/74362292/79329544-59d2-4be3-8a14-bf5c66988a82)


After 100,000 games training,  the Q-learning algorithm player with the trained Q table plays 1000 games with the default player,  who plays first is random in each game.  And the results are shown below, the default player couldn’t win any games, the trained Q-learning algorithm’s win probability is near 80% and the tied game probability is near 20%. 
   
![3](https://github.com/Weiwei-Wan/AI_Tic-Tac-Toe_MiniMax-Q-learning/assets/74362292/ae02ce8a-0997-42ff-8fa4-d130adfeec00)


# Tabular Q-learning playing against Minimax

Now I would compare the performance of Q-learning algorithm and minimax. The results are shown below. It looks that these two algorithms could never beat each other, that means both of the two algorithms are perfect in Tic Tac Toe. As both algorithms could never lose, all 1000 games are tied here.

![14](https://github.com/Weiwei-Wan/AI_Tic-Tac-Toe_MiniMax-Q-learning/assets/74362292/346e4a31-bb29-4953-aa7c-0855c5dd248b)


# How to run:

run PlayerVsPlayer.py
line 131: play(player1 = 1, player2 = 2, play_number = 1000, q_learning_train_number = 100000), 

0: defalt  1: minimax  2:q learning
change parameter if you want
