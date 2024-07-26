# Program design for ONE STOP INSURANCE COMPANY
# Written by: May Basalo
# Date written: July 25,2024

import datetime
import FormatValues as FV


def CalculatePremium(NumCarsIns, PremiumRate, AddCarDiscount):
    return PremiumRate + (PremiumRate * AddCarDiscount * (NumCarsIns - 1))


def CalculateExtraCosts(NumCarsIns, ExtLiability, GlassCvrg, LoanerCar, ExtraLiabilityRate, GlassCoverageRate,
                        LoanerCarRate):
    TotalExtraCosts = 0
    if ExtLiability == "Y":
        TotalExtraCosts += ExtraLiabilityRate * NumCarsIns
    if GlassCvrg == "Y":
        TotalExtraCosts += GlassCoverageRate * NumCarsIns
    if LoanerCar == "Y":
        TotalExtraCosts += LoanerCarRate * NumCarsIns
    return TotalExtraCosts


def CalculateHST(TotalInsPremium, HstRate):
    HST = HstRate * TotalInsPremium
    return HST


def CalcMonthPay(PayMethod, TotalCost, ProcessingFee, DownPay):
    if DownPay != 0:
        TotalCost -= DownPay
        TotalCost += ProcessingFee
        MonthlyPay = TotalCost / 8
    else:
        TotalCost += ProcessingFee
        MonthlyPay = TotalCost / 8
    return MonthlyPay


def GetInvDate():
    return datetime.datetime.now()


def CalcFirstPayDate(CurDate):
    NextMnth = CurDate.replace(day=1) + datetime.timedelta(days=32)
    FirstPayDate = NextMnth.replace(day=1)
    return FirstPayDate


def GetClaims():
    Claims = []
    while True:
        while True:
            ClaimNum = input("Enter the claim number (99999): ")
            if ClaimNum.isdigit() == False:
                print("Date entry error - Claim number must be digits only.")
            elif len(ClaimNum) != 5:
                print("Data entry error - Claim number must be 5 digits.")
            else:
                break

        while True:
            ClaimDate = input("Enter the claim date (YYYY-MM-DD): ")
            try:
                ClaimDate = datetime.datetime.strptime(ClaimDate, "%Y-%m-%d")
                ClaimDate = ClaimDate.date()

                break
            except:
                print("Data entry error - Date is not in valid format.")

        while True:
            ClaimAmt = float(input("Enter the claim amount: "))
            if ClaimAmt <= 0:
                print("Data entry error - Claim amount can not be 0")
            else:
                break
        Claims.append([ClaimNum, ClaimDate, ClaimAmt])

        AddClaim = ""
        while True:
            AddClaim = input("Would you like to add another claim? (Y/N): ").upper()
            if AddClaim != "Y" and AddClaim != "N":
                print("Data entry error - Must be Y or N")
            else:
                break
        if AddClaim == "N":
            break
    return Claims


def SaveClaims(Claims, ClaimFile, PolicyNum, FirstName, LastName, PhoneNum, CustAdd, City, Prov, PostalCode, NumCars,
               ExtLiability, GlassCov, Loaner, PayMethod, DownPay, TotInsPrem):
    with open(ClaimFile, 'a') as file:
        for Claim in Claims:
            CustInfo = str(PolicyNum) + ", " + FirstName + ", " + LastName + ", " + PhoneNum + ", "

            MyClaim = Claim[0] + ", " + str(Claim[1]) + ", " + str(Claim[2]) + ", "

            CustAddress = (CustAdd) + ", " + (City) + ", " + (Prov) + ", " + (PostalCode) + ", "

            Extras = str(NumCars) + ", " + str(ExtLiability) + ", " + str(GlassCov) + ", " + (Loaner) + ", "

            Pay = (PayMethod) + ", " + (DownPay) + ", " + str(TotInsPrem) + "\n"

            file.write(CustInfo)
            file.write(MyClaim)
            file.write(CustAddress)
            file.write(Extras)
            file.write(Pay)
