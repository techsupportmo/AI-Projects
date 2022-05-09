# Mohammed Ahmed
# 1001655176

# HOW TO RUN
# Type into command line:
# compute_a_posteriori CLLCCLLLCCL

import sys

def computeProbability():
    return 1

def printProbability(h_values):
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



n = len(sys.argv)                       # number of arguments passed in

observationCount = 0                    # Observation Count
h = [0.1, 0.2, 0.4, 0.2, 0.1]           # 5 types of bags of candy - 10% are h1, 20% are h2, etc...
lime = {0, 0.25, 0.5, 0.75, 100}        # Percentage of lime candies in the bag
cherry = {100, 0.75, 0.5, 0.25, 0}      # Percentage of cherry candies in the bag


# INITIAL
currentProb = h                         # To start, probability values are same as hypothesis
prevProb = h                            # Initially, the probabilities are the same as the hypothesis

# NO COMMANDS ENTERED
if(n == 1):
    print("No Observations Made\n")
    printProbability(currentProb)       # If there are no commands entered, then the initial hypothesis is printed
    quit()                              # End program


# Q                                     # Take in command line argument - 
Q = sys.argv[1]                         # Q is a string representing a series of observations ex. CLLCCCLLL                               
length = 1#len(Q)                       # Length of Q



# Arguments passed
print("\nObservation sequence Q:", Q)
print("Length of Q:", length)

while(observationCount < length):
    Qj = Q[observationCount]                                # Current letter being observed
    observationCount+=1                                     # Increment observation count (starts at 1)
    print("\n\nAfter observation ", end="")
    print(observationCount, end="")
    print(" = " + Qj + ": ")

    # Check whether observation is a lime or cherry
    if (Qj == 'C'):
        print("Cherry")
    elif(Qj == 'L'):
        print("Lime")


    print("P(h1 | Q) = ", end="")
    print("BLANK")
    print("P(h2 | Q) = ", end="")
    print("BLANK")
    print("P(h3 | Q) = ", end="")
    print("BLANK")
    print("P(h4 | Q) = ", end="")
    print("BLANK")
    print("P(h5 | Q) = ", end="")
    print("BLANK")

    print("Probability that the next candy we pick will be C, given Q: ", end="")
    print("")
    print("Probability that the next candy we pick will be L, given Q: ", end="")
    print("")




print("hello world")