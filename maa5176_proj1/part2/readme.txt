Project 1 Part 2 README

Mohammed Ahmed
1001655176

- The programming language used for the task was Python 3.9.1 (not compiled on omega)

------------ Structure of the code: -----------

This program was created by modifying the sample code provided on the course website

- functions like interactiveGame(currentGame) and aiPlay(self) we modified

Additional functions:

minimax(self, depth, alpha, beta, maximizingPlayer, player): 
-----> returns eval value and column to place piece

def unplayPiece(self, column): 
----> This unplays the most recent piece of a certain column


--------- How to run the code: ----------------

1. Make sure python3 is installed on computer
2. Navigate to directory where code is stored and open terminal
3. Compile code

### HOW TO COMPILE ###
# python3 maxconnect4.py one-move input1.txt output1.txt 3 ----> one move mode
# python3 maxconnect4.py interactive input1.txt computer-next 3 ----> Interactive (Computer Next)
# python3 maxconnect4.py interactive input1.txt human-next 3 ----> Interactive (Human Next)


Execution Time at Different Depths:
-----------------------------------

  Depth    |   Time (sec)
---------------------------
    1      |     0.035
    2      |     0.042
    3      |     0.042
    4      |     0.045 
    5      |     0.057 
    6      |     0.103
    7      |     0.240
    8      |     0.502
    9      |     1.387
    10     |     3.426
    11     |     17.067
    12     |     43.468
    13     |     1m and 44.946 seconds