# Mohammed Ahmed
# 1001655176

import sys


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
    
    #split apart contents of line by the spaces (seperate each operator/operand)
    tokens = currentline.split(' ')

    inputArray.append(tokens)

    print(tokens)

    

# print(inputArray)
 
# Prints out all the arguments passed in (except for filename)
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
print("\n")

print("The distance between them is:  ", end = "")
print(inputArray[0][2]) # NOT ACTUAL DISTANCE


# Close file
inputFile.close()


