# Written by S.AmirMohammad Hasanli (amir.hasanli@ut.ac.ir)
# GNU General Public License v2.0
# This document is available online at following public repository:
# https://github.com/S-AMH/MastersDegree/blob/main/CalculateAET.py
# 2021-Nov-5

def validate (input, inputName, lowerBoundry = None, upperBoundry = None, upperEqual = False, lowerEqual = False): # Validates input with given boundries
    counter = 0
    if lowerBoundry != None:
        if lowerEqual:
            if input >= lowerBoundry:
                counter += 1
            else:
                print("Error: Invalid " + inputName)
                exit()
        else:
            if input > lowerBoundry:
                counter += 1
            else:
                print("Error: Invalid " + inputName)
                exit()
    else:
        counter += 1
    if upperBoundry != None:
        if upperEqual:
            if input <= upperBoundry:
                counter += 1
            else:
                print("Error: Invalid " + inputName)
                exit()
        else:
            if input < upperBoundry:
                counter += 1
            else:
                print("Error: Invalid " + inputName)
                exit()
    else:
        counter += 1
    if counter == 2:
        return input

print("Initializing field variables:")

days = validate(int(input("\tPlease enter number of days:")), "days", lowerBoundry = 0, lowerEqual = False) # Number of days which cycle continues
RC = validate(float(input("\tPlease enter RC:")), "RC", lowerBoundry = 0.0, lowerEqual = True) # Soil Water Holding Capacity
KC = validate(float(input("\tPlease enter KC:")), "KC", lowerBoundry = 0.0, lowerEqual = True) # Crop Coefficient
FC = validate(float(input("\tPlease enter FC:")), "FC", lowerBoundry = 0.0, lowerEqual = True) # Field Capacity
PWP = validate(float(input("\tPlease enter PWP:")), "PWP", lowerBoundry = 0.0, lowerEqual = True) # Permanent Wilting Point

AWC = validate(FC - PWP, "AWC", lowerBoundry = 0.0, lowerEqual = False) # Calculating Available Water Content

CRF = 0.0 # Cumulative Rainfall
PR = 0.0 # Previous R
PD = 0.0 # Previous D
AET = list() # List of calculated actual evapotranspirations
RF = list() # List of entered rainfalls
PET = list() # List of entered potential evapotranspirations

for i in range(0, days):
    print("\nDay #" + str(i+1))

    PET.append(validate(float(input("Please enter PET:")), "PET")) # Potential EvapoTranspiration
    RF.append(validate(float(input("Please enter RF:")), "RF", lowerBoundry = 0.0, lowerEqual = True)) # Rainfall

    CRF += RF[i] # Adds up today's rainfall and total cumulative rainfall and assigns it to CRF variable
    print("CRF: " + str(CRF))
    if CRF > 15.0:
        ETM = KC * PET[i]
        print("ETM: " + str(ETM))
        if RF[i] < 25.0:
            R = 0
        else:
            R = 0.15 * (RF[i] - 25.0)
        print("R: " + str(R))
        if RF[i] < RC:
            D = 0
        else:
            D = RF[i] - RC
        print("D: " + str(D))
        WS = RF[i-1] - (PR + PD + AET[i-1])
        print("WS: " + str(WS))
        if WS > 0.4 * AWC:
            AET.append(ETM)
        else:
            AET.append(ETM * WS / (0.4 * AWC))
        PR = R # Update previous R
        PD = D # Update previous D
    else:
        AET.append(0.2 * PET[i])
    if(AET[i] < 0):
        AET[i] = 0
    print("AET = " + str(AET[i]) + "\n")

print("\t## END OF CYCLE ##")
_bPlot = input("Do you want to see output plot?(y/n) ")
if _bPlot == "y" or _bPlot == "Y": # Draws the output plot
    import matplotlib.pyplot as plt
    plt.plot(AET, "g")
    plt.plot(PET, "r")
    plt.plot(RF, "b")
    plt.xlabel("Day")
    plt.ylabel("mm/d")
    plt.xticks(list(range(1,days+1)))
    plt.yticks(list(range(int(min(AET + PET + RF)), int(max(AET + PET + RF))+2, 2))) # Adjusting Y ticks with values
    plt.title("Rain, Potential and Actual evapotranspiration")
    ax = plt.gca()
    ax.legend(["Actual Evapotranspiration", "Potential Evapotranpiration", "Daily Rainfall"])
    plt.show()
