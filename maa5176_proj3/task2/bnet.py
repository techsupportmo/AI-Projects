# Mohammed Ahmed
# 1001655176

import sys


n = len(sys.argv)                       # number of arguments passed in

# Possible characters for input:
# Bt, Bf, Et, Ef, At, Af, Jt, Jf, Mt, Mf, given

total_prob = 1          # Total probability calculated
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
maryCalls_dict = {
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




if (n > 2 and n <= 6):
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
        elif(sys.argv[i] == "At"):
            johnCalls_dict["A_value"] = True
            maryCalls_dict["A_value"] = True
        elif(sys.argv[i] == "Af"):
            johnCalls_dict["A_value"] = False
            maryCalls_dict["A_value"] = False
        
        input.append(sys.argv[i])       # Store input

    print(input)

    # Calculate Probability without any givens
    for i in range(len(input) + 1):
        if( sys.argv[i] == "Bt"):
            total_prob = total_prob * p_burglary
            print("INSIDE BT")
        elif(sys.argv[i] == "Bf"):
            total_prob = total_prob * (1 - p_burglary)
            print("INSIDE BF")
        elif(sys.argv[i] == "Et"):
            total_prob = total_prob * p_earthquake
            print("INSIDE ET")
        elif(sys.argv[i] == "Ef"):
            total_prob = total_prob * (1 - p_earthquake)
            print("INSIDE EF")
        elif(sys.argv[i] == "At"):
            if( alarm_dict["B_value"] == True and alarm_dict["E_value"] == True):       # Alarm = T when B = T and E = T
                total_prob = total_prob * p_alarm[0][2]
                print("INSIDE AT - BOTH TRUE")
            if( alarm_dict["B_value"] == True and alarm_dict["E_value"] == False):      # Alarm = T when B = T and E = F
                total_prob = total_prob * p_alarm[1][2]
            if( alarm_dict["B_value"] == False and alarm_dict["E_value"] == True):      # Alarm = T when B = F and E = T
                total_prob = total_prob * p_alarm[2][2]
            if( alarm_dict["B_value"] == False and alarm_dict["E_value"] == False):     # Alarm = T when B = F and E = F
                total_prob = total_prob * p_alarm[3][2]           
        elif(sys.argv[i] == "Af"):
            if( alarm_dict["B_value"] == True and alarm_dict["E_value"] == True):       # Alarm = F when B = T and E = T
                total_prob = total_prob * (1 - p_alarm[0][2])
                print("INSIDE AF - BOTH TRUE")
            if( alarm_dict["B_value"] == True and alarm_dict["E_value"] == False):      # Alarm = F when B = T and E = F
                total_prob = total_prob * (1 - p_alarm[1][2])
            if( alarm_dict["B_value"] == False and alarm_dict["E_value"] == True):      # Alarm = F when B = F and E = T
                total_prob = total_prob * (1 - p_alarm[2][2])
            if( alarm_dict["B_value"] == False and alarm_dict["E_value"] == False):     # Alarm = F when B = F and E = F
                total_prob = total_prob * (1 - p_alarm[3][2])
        elif (sys.argv[i] == "Jt"): 
            if(johnCalls_dict["A_value"] == True):                                      # JohnCalls = T when Alarm = T
                 total_prob = total_prob * p_johnCalls[0][1]
            if(johnCalls_dict["A_value"] == False):                                     # JohnCalls = T when Alarm = F
                 total_prob = total_prob * p_johnCalls[1][1]
        elif (sys.argv[i] == "Jf"):
            if(johnCalls_dict["A_value"] == True):                                      # JohnCalls = F when Alarm = T
                 total_prob = total_prob * (1 - p_johnCalls[0][1])
            if(johnCalls_dict["A_value"] == False):                                     # JohnCalls = F when Alarm = F
                 total_prob = total_prob * (1 - p_johnCalls[1][1])
        elif (sys.argv[i] == "Mt"):
            if(maryCalls_dict["A_value"] == True):
                total_prob = total_prob * p_maryCalls[0][1]                             # MaryCalls = T when Alarm = T
            if(maryCalls_dict["A_value"] == False):
                total_prob = total_prob * p_maryCalls[1][1]                             # MaryCalls = T when Alarm = T
        elif (sys.argv[i] == "Mf"):
            if(maryCalls_dict["A_value"] == True):
                total_prob = total_prob * (1 - p_maryCalls[0][1])                       # MaryCalls = F when Alarm = T
            if(maryCalls_dict["A_value"] == False):
                total_prob = total_prob * (1 - p_maryCalls[1][1])                       # MaryCalls = F when Alarm = F



    # Inference By Enumeration

    # Print Probability
    print(f"The probability is: {total_prob:0.16f}")




# Debug
# Arguments passed
#print("\nName of Python script:", sys.argv[0])
 
#print("\nArguments passed:", end = " ")
#for i in range(1, n):
    #print(sys.argv[i], end = " ")
