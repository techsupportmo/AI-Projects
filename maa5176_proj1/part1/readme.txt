Project 1 Part 1 README

Mohammed Ahmed
1001655176

- The programming language used for the task was Python 3.9.1 (not compiled on omega)

----------------- Structure of the code: ---------------------------

# ---- Node ---- #
# [city,  g(n) , parent,  h(n) , f(n) ] #

- This is the representation of a node in my code

Functions:

def findPath(destination_city, expandedList, graph):
------> Prints out the path from the origin to the destination city

def expand(currentNode, graph):
------> Expands the current node and returns a list of successors

def uniformCostSearch(graph, origin_city, destination_city):
------> Performs UCS (or A* depending on heuristic)

def generateDirectedGraph(inputArray):
------> Generates 2D dictionary of all paths to and from nodes given a 2D array with the paths




------------------- How to run the code: -----------------------------

- Make sure Python3 is installed on computer
- Navigate to directory and open terminal
- Compile code



### ----- HOW TO COMPLILE -------- ###
# python3 find_route.py input1.txt Bremen Kassel ---------------------> Uninformed (UCS)
# python3 find_route.py input1.txt London Kassel ---------------------> No path example
# python3 find_route.py input1.txt Bremen Kassel h_kassel.txt --------> Informed