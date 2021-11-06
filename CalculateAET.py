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

days = validate(int(input("\tPlease enter number of days:")), "days", lowerBoundry = 0, lowerEqual = False) # Number of days which cycle continous
RC = validate(float(input("\tPlease enter RC:")), "RC", lowerBoundry = 0.0, lowerEqual = True) # Soil Water Holding Capacity
KC = validate(float(input("\tPlease enter KC:")), "KC", lowerBoundry = 0.0, lowerEqual = True) # Crop Coefficient
FC = validate(float(input("\tPlease enter FC:")), "FC", lowerBoundry = 0.0, lowerEqual = True) # Field Capacity
PWP = validate(float(input("\tPlease enter PWP:")), "PWP", lowerBoundry = 0.0, lowerEqual = True) # Permanent Wilting Point

AWC = validate(FC - PWP, "AWC", lowerBoundry = 0.0, lowerEqual = False) # Calculating Available Water Content

CRF = 0.0 # Cumulative Rainfall
PRF = 0.0  # Previous Rainfall
PR = 0.0 # Previous R
PD = 0.0 # Previous D
PAET = 0.0 # Previous Actual EvapoTranspiration

for i in range(0, days):
    print("\nDay #" + str(i+1))

    PET = validate(float(input("Please enter PET:"), "PET")) # Potential EvapoTranspiration
    RF = validate(float(input("Please enter RF:")), "RF", lowerBoundry = 0.0, lowerEqual = True) # Rainfall

    if CRF > 15.0:
        ETM = KC * PET
        if RF < 25.0:
            R = 0
        else:
            R = 0.15 * (RF - 25.0)
        if RF < RC:
            D = 0
        else:
            D = RF - RC
        WS = PRF - (PR + PD + PAET)
        if WS > 0.4 * AWC:
            AET = ETM
        else:
            AET = ETM * WS / (0.4 * AWC)
        PRF = RF
        PR = R
        PD = D
        PAET = AET
    else:
        AET = 0.2 * PET
    print("AET = " + str(AET) + "\n")
    CRF += RF
