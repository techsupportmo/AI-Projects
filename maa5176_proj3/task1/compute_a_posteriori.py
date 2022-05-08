# Mohammed Ahmed
# 1001655176

# HOW TO RUN
# Type into command line:
# compute_a_posteriori CLLCCLLLCCL

import sys

def computeProbability():
    return 1



# Take in command line argument - Q is a string representing a series of observations ex. CLLCCCLLL
Q = sys.argv[1] 
length = 1#len(Q)                   # Length of Q
observationCount = 0                # Observation Count
h = {0.1, 0.2, 0.4, 0.2, 0.1}       # 5 types of bags of candy - 10% are h1, 20% are h2, etc...
lime = {0, 0.25, 0.5, 0.75, 100}    # Percentage of lime candies in the bag
cherry = {100, 0.75, 0.5, 0.25, 0}  # Percentage of cherry candies in the bag


# Arguments passed
print("\nObservation sequence Q:", Q)
print("Length of Q:", length)

while(observationCount < length):
    observationCount+=1
    print("\n\nAfter observation ", end="")
    print(observationCount, end="")
    print(" = " + Q[observationCount-1] + ": ")

    # Check whether observation is a lime or cherry
    if (Q[observationCount-1] == 'C'):
        print("Cherry")
    elif(Q[observationCount-1] == 'L'):
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