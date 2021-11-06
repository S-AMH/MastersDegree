# 2021-Nov-5

days = int(input("Please enter number of days:"))
RC = float(input("Please enter RC:"))
AWC = float(input("Please enter AWC:"))

CRF = 0.0
PRF = 0.0
PR = 0.0
PD = 0.0
PAET = 0.0

for i in range(0,days):
    print("\nDay #" + str(i+1))

    PET = float(input("Please enter PET:"))
    KC = float(input("Please enter KC:"))
    FC = float(input("Please enter FC:"))
    PWP = float(input("Please enter PWP:"))
    RF = float(input("Please enter RF:"))

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

