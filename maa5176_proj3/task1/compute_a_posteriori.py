# Mohammed Ahmed
# 1001655176

# HOW TO RUN
# Type into command line:
# compute_a_posteriori CCCCC

import sys
import os

# FILE HANDLING
f = open("result.txt", "w")             # Creates file if it doesn't exist already

# -----------------------------------------------------------------------------------
# Function: WriteResults()
# Purpose:  Write the probabilities (same output as print statements) to results.txt file
# Input:    Array with h values, Cherry next probability, Lime next probability
# Output:   Nothing, only print statements
def writeResults(h_values, c_next, l_next):
    f.write(f"P(h1 | Q) = {h_values[0]:0.5f}\n")
    #f.write("0.5%h_values[0])
    f.write(f"P(h2 | Q) = {h_values[1]:0.5f}\n")
    #f.write(str(h_values[1]))
    f.write(f"P(h3 | Q) = {h_values[2]:0.5f}\n")
    #f.write(str(h_values[2]))
    f.write(f"P(h4 | Q) = {h_values[3]:0.5f}\n")
    #f.write(str(h_values[3]))
    f.write(f"P(h5 | Q) = {h_values[4]:0.5f}\n")
    #.write(str(h_values[4]))

    f.write(f"Probability that the next candy we pick will be C, given Q: {c_next:0.5f}\n")
    #f.write(str(c_next))
    f.write(f"Probability that the next candy we pick will be L, given Q: {l_next:0.5f}\n")
    #f.write(str(l_next))
# -----------------------------------------------------------------------------------





# -----------------------------------------------------------------------------------
# Function: PrintProbability()
# Purpose:  Print out probability values to the screen
# Input:    Array with h values, Cherry next probability, Lime next probability
# Output:   Nothing, only print statements
def printProbability(h_values, c_next, l_next):
    print("P(h1 | Q) = ", end="")
    print(h_values[0])
    print("P(h2 | Q) = ", end="")
    print(h_values[1])
    print("P(h3 | Q) = ", end="")
    print(h_values[2])
    print("P(h4 | Q) = ", end="")
    print(h_values[3])
    print("P(h5 | Q) = ", end="")
    print(h_values[4])

    print("Probability that the next candy we pick will be C, given Q: ", end="")
    print(c_next)
    print("Probability that the next candy we pick will be L, given Q: ", end="")
    print(l_next)
# -----------------------------------------------------------------------------------


n = len(sys.argv)                       # number of arguments passed in

observationCount = 0                    # Observation Count
h = [0.1, 0.2, 0.4, 0.2, 0.1]           # 5 types of bags of candy - 10% are h1, 20% are h2, etc...
lime = [0, 0.25, 0.5, 0.75, 1]        # Percentage of lime candies in the bag
cherry = [1, 0.75, 0.5, 0.25, 0]      # Percentage of cherry candies in the bag


# INITIAL
currentProb = h                         # To start, probability values are same as hypothesis
prevProb = h                            # Initially, the probabilities are the same as the hypothesis
lime_prob = lime
cherry_prob = cherry
c_next = 0.5
l_next = 0.5

# NO COMMANDS ENTERED
if(n == 1):
    print("No Observations Made\n")
    f.write("No Observations Made\n")
    printProbability(currentProb, c_next, l_next)       # If there are no commands entered, then the initial hypothesis is printed
    writeResults(currentProb, c_next, l_next)
    quit()                                              # End program


# Q                                     # Take in command line argument - 
Q = sys.argv[1]                         # Q is a string representing a series of observations ex. CLLCCCLLL                               
length = len(Q)                         # Length of Q



# Arguments passed
print("\nObservation sequence Q: ", Q)
f.write(f"\nObservation sequence Q: {Q}\n")

print("Length of Q:", length)
f.write(f"Length of Q:{length}\n")

while(observationCount < length):
    Qj = Q[observationCount]                                # Current letter being observed
    observationCount+=1                                     # Increment observation count (starts at 1)

    print("\n\nAfter observation ", end="")
    print(observationCount, end="")
    print(" = " + Qj + ": ")

    f.write(f"\n\nAfter observation {observationCount}\n")


    # Check whether observation is a lime or cherry
    if (Qj == 'C'):
        print("Cherry")


        # Calculate Pt(hi)
        # (constant cherry probability * previous prob of cherry)/ probability of cherry next computed previously
        for i in range (5):
            currentProb[i] = cherry[i] * currentProb[i] / c_next

        # Resetting probability of cherry next so I can calculate new value, based on updated probability
        c_next = 0                                          
        for i in range (5):
            c_next += cherry[i] * currentProb[i]

        # Compute the probability of lime next, which is 1 - probability of cherry next
        l_next = 1 - c_next 

        printProbability(currentProb, c_next, l_next)
        writeResults(currentProb, c_next, l_next)


    elif(Qj == 'L'):
        print("Lime")

        # Calculate Pt(hi)
        # (constant cherry probability * previous prob of cherry)/ probability of cherry next computed previously
        for i in range (5):
            currentProb[i] = lime[i] * currentProb[i] / l_next

        # Resetting probability of cherry next so I can calculate new value, based on updated probability
        l_next = 0                                          
        for i in range (5):
            l_next += lime[i] * currentProb[i]

        # Compute the probability of lime next, which is 1 - probability of cherry next
        c_next = 1 - l_next 

        printProbability(currentProb, c_next, l_next)
        writeResults(currentProb, c_next, l_next)




f.close()       # Close file