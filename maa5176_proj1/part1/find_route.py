# Mohammed Ahmed
# 1001655176

import sys
from collections import defaultdict

def expand(currentNode, graph):

    # successors <--- the empty set
    successors = []

    # print(graph)
    print(currentNode)

    # Finds all of the cities currentNode is connected to
    for child in graph[currentNode[0]]:
        # print(child)

        # The distance from the start node is the 
        # cost of the current node(from start) + cost of current node to child
        distance = currentNode[1] + int(graph[currentNode[0]][child])

        # print("The distance is:  ", end="")
        # print(distance)

        # This creates a new node with the child 
        # and direct distance from the start
        s = [child,distance]
        # print(s)

        # Add each successor to the array
        successors.append(s)

    # print(successors)



    # Return array of successors 
    # [name,cost from start] of each child
    return successors


def uniformCostSearch(graph, origin_city, destination_city):
    print("Performing uninformed search....\n")

    closed = []
    fringe = []

    nodesExpanded = 0
    nodesGenerated = 0

    fringe.append([origin_city,0])

    dummyCount = 0

    while True:
        # if the fringe is empty ---> return fail
        if len(fringe) == 0:
            return "search failed"
 

        # pop node from fringe
        currentNode = fringe.pop(0)

        # Goal test
        if (currentNode[0] == destination_city):
            print("Nodes expanded: " + str(nodesExpanded))
            print("Nodes generated: " + str(nodesGenerated))
            print("The distance between them is : " + str(currentNode[1]) + " km")
            print("Route:")
            return "Goal reached"

        # Check if current node is in closed set
        if currentNode[0] not in closed:
            # Add current node to closed set
            closed.append(currentNode[0])

            # Expand node
            successors = expand(currentNode, graph)
            nodesExpanded+=1
            nodesGenerated += len(successors)
            fringe = fringe + successors
            

            # Sort the fringe
            fringe.sort(key=lambda x: x[1])

            print("Fringe:")
            print(fringe)
            print("Closed:")
            print(closed)
            print("\n\n")


            

def generateDirectedGraph(inputArray):
    graph = defaultdict(dict)
    for city1, city2, cost in inputArray:
        graph[city1][city2] = cost
        graph[city2][city1] = cost
    return graph

print("\n\nthis is the find route program\n\n")

# find_route --------------- sys.argv[0]
# input_filename ----------- sys.argv[1]
# origin_city -------------- sys.argv[2]
# destination_city --------- sys.argv[3]
# heuristic_filename ------- sys.argv[4]

# Stores the total number of arguments
n = len(sys.argv)
print("Total arguments passed:", n)
 

# Step 1: Store the command line arguments into variables
input_filename = sys.argv[1]
origin_city = sys.argv[2]
destination_city = sys.argv[3]

if (n == 5):
    heuristic_filename = sys.argv[4]

# Step 2: Store input1.txt into array

# Opens input file and 
# Uses readlines() to store file contents
inputFile = open(input_filename, 'r')
Lines = inputFile.readlines()

# InputArray is a 2D array that is storing the contents of the input file
inputArray = []

for line in Lines:
    # Removes newline
    currentline = line.strip()
    # Removes last line (END OF INPUT)
    if(currentline == 'END OF INPUT'):
        break
    #split apart contents of line by the spaces (seperate each operator/operand)
    tokens = currentline.split(' ')
    inputArray.append(tokens)
    # print(tokens)

    

# print(inputArray)
 
# Prints out all the arguments passed in (except for filename)
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
print("\n")

# Step 3: Perform uninformed/informed search

if (n == 4):
    graph = generateDirectedGraph(inputArray)
    print("\n\n\n\n")
    print(uniformCostSearch(graph, origin_city, destination_city))
    
    


# Close file
inputFile.close()


