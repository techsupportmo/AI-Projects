# Mohammed Ahmed
# 1001655176

import sys
import numpy

n = len(sys.argv)                       # number of arguments passed in

# Possible characters for input:
# Bt, Bf, Et, Ef, At, Af, Jt, Jf, Mt, Mf, given

total_prob = 0          # Total probability calculated
givenPresent = False    # Checks if the keyword 'Given' is present in the code
input = []              # Array to store input

# Dictionary to store alarm value
alarm_dict = {
  "B_value": None,
  "E_value": None,
}

# Dictionary to store johnCalls value
johnCalls_dict = {
  "A_value": None,
}

# Dictionary to store maryCalls value
johnCalls_dict = {
  "A_value": None,
}





# Store the Bayesian Network
p_burglary = 0.001                     # Probability of Burglary
p_earthquake = 0.002                   # Probability of Earthquake

# Probability of Alarm, given Burglary and Earthquake
p_alarm = [[True, True, 0.95],
           [True, False, 0.94],
           [False, True, 0.29],
           [False, False, 0.001]]

# Probability of JohnCalls, given Alarm
p_johnCalls = [[True, 0.9],
               [False, 0.05]]

# Probability of MaryCalls, given Alarm
p_maryCalls = [[True, 0.7],
               [False, 0.01]]


# Base case

# If there is only one input (independent values)
if(n == 2):
    if( sys.argv[1] == "Bt"):
        total_prob = p_burglary
    elif(sys.argv[1] == "Bf"):
        total_prob = 1 - p_burglary
    elif(sys.argv[1] == "Et"):
        total_prob = p_earthquake
    elif(sys.argv[1] == "Ef"):
        total_prob = 1 - p_earthquake

# Print Probability
print(f"The probability is: {total_prob}")

# Parse input
for i in range(1, n):
    print(sys.argv[i], end = " ")

    # Checks if token is 'given' keyword
    if(sys.argv[i] == "given"):
        givenPresent = True
    
    # Updates T/F values for children
    if( sys.argv[i] == "Bt"):
        alarm_dict["B_value"] = True
    elif(sys.argv[i] == "Bf"):
        alarm_dict["B_value"] = False
    elif(sys.argv[i] == "Et"):
        alarm_dict["E_value"] = True
    elif(sys.argv[i] == "Ef"):
        alarm_dict["E_value"] = False
    
    input.append(sys.argv[i])       # Store input

print(input)

# Calculate Probability without any givens



# Inference By Enumeration




# Debug
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
