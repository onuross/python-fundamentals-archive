numberBoxes = 0
numberTaws = 0              # Taken From User For Every Box
tawWeight = 0               # Taken From User For Every Taw In One Box
returnedBox = 0             # Number Of Returned Boxes
returnedTaws = 0            # Number Of Returned Taws
totalTaws = 0               # Total Number Of Taws
equalBox = 0                # Number Of Boxes Which All Taws' Weight Is Equal
lighterBox = 0              # Number Of Boxes Which Have 1 Taw Lighter than The Other Taws In That Box
heavierBox = 0              # Number Of Boxes Which Have 1 Taw Heavier than The Other Taws In That Box
biggestWeightDiff = 0       # Biggest Wight Difference Between Taws In One Box Which Have Just One Different Taw
maxDiffNumber = 2           # If The Number Of Different Taws Equal Or More Than This, Then The Box Will Return
testTaw1 = 0                # Taken From The User For Every Box For Checking Statements
testTaw2 = 0                # Taken From The User For Every Box For Checking Statements
testTaw3 = 0                # Taken From The User For Every Box For Checking Statements
weightDiffHeavier = 0       # Difference Of Different Weighted Taw and
# Normal Taw In One Box Which Have Just One Different Taw
weightDiffLighter = 0       # Difference Of Different Weighted Taw and
# Normal Taw In One Box Which Have Just One Different Taw
totalLighterTaws = 0
totalHeavierTaws = 0
equalHeavierWeight = 0      # The Biggest Weight In Equal Weighted Boxes
equalHeavierNumber = 0      # Number Of Taws In Equal Weighted Box That Have The Biggest Weight
totalPerDiffLight = 0
totalPerDiffHeavy = 0
totalWeightDiffLight = 0
totalWeightDiffHeavy = 0
equalLightCounter = 0
equalHeavierCounter = 0
lighterWeightTest = 0
heavierWeightTest = 0
heavierTest = 0            # In Last Part Of Code, For Checking Did Box Have Heavier Taw
lighterTest = 0            # In Last Part Of Code, For Checking Did Box Have Lighter Taw
equalNumber = 0            # For Checking The Biggest Taw Number In Boxes Which Have Equal Taws
equalWeight = 0            # For Saving The Weight Of Taws In Box Which Have Equal Taws and Biggest Number
biggestDiff = 0
biggestDiffPer = 0
biggestDiffSign = ''      # Heavy or Light
smallestDiff = 99999999
smallestDiffPer = 0
smallestDiffSign = ''      # Heavy or Light
counterTest = 0
toContinue = 'y'

while toContinue in ['y', 'Y']:
    numberBoxes += 1
    numberTaws = int(input("Enter The Number Of Taws In This Box:"))
    while numberTaws < 10:
        print("Number Of Taws In One Box Can't Less Than 10")
        numberTaws = int(input("Enter The Number Of Taws In This Box:"))
    totalTaws += numberTaws
    testTaw1 = int(input("Enter One Of The Taw's Weight:"))
    testTaw2 = int(input("Enter One Of The Taw's Weight:"))
    testTaw3 = int(input("Enter One Of The Taw's Weight:"))
    if testTaw1 != testTaw2 and testTaw2 != testTaw3 and testTaw1 != testTaw3:
        returnedBox += 1
        returnedTaws += numberTaws
        toContinue = input("Is There Other Boxes (y,Y,n,N):")
        while toContinue not in ['y', 'Y', 'n', 'N']:
            print("Incorrect Data Entry, Please Try Again!")
            toContinue = input("Is There Other Boxes (y,Y,n,N):")
    elif (testTaw1 != testTaw2 and testTaw2 == testTaw3) or \
            (testTaw2 != testTaw3 and testTaw3 == testTaw1) or \
            (testTaw1 == testTaw2 and testTaw2 != testTaw3):
        for taw in range(4, numberTaws + 1):
            tawWeight = int(input("Enter One Of The Taw's Weight:"))
            while tawWeight <= 0:
                print("Weight Can Not Be Negative or Equal To Zero!")
                tawWeight = int(input("Enter One Of The Taw's Weight:"))
            counterTest = 0
            if (tawWeight != testTaw1 and testTaw1 == testTaw2) or \
                    (tawWeight != testTaw2 and testTaw3 == testTaw2) or \
                    (tawWeight != testTaw1 and testTaw1 == testTaw3):
                returnedBox += 1
                returnedTaws += numberTaws
                counterTest += 1
                break
        if testTaw2 == testTaw3 and testTaw1 > testTaw2 and counterTest == 0:
            heavierBox += 1
            totalWeightDiffHeavy += testTaw1 - testTaw2
            totalPerDiffHeavy += (testTaw1 - testTaw2) / testTaw2 * 100
            if testTaw1 - testTaw2 >= biggestDiff:
                biggestDiffSign = 'Heavier'
                biggestDiffPer = (testTaw1 - testTaw2) / testTaw2 * 100
                biggestDiff = testTaw1 - testTaw2
            elif testTaw1 - testTaw2 <= smallestDiff:
                smallestDiff = testTaw1 - testTaw2
                smallestDiffPer = (testTaw1 - testTaw2) / testTaw2 * 100
                smallestDiffSign = 'Heavier'
        elif testTaw2 == testTaw3 and testTaw1 < testTaw2 and counterTest == 0:
            totalWeightDiffLight += testTaw2 - testTaw1
            lighterBox += 1
            totalPerDiffLight += (testTaw2 - testTaw1) / testTaw1 * 100
            if testTaw2 - testTaw1 >= biggestDiff:
                biggestDiffSign = 'Lighter'
                biggestDiffPer = (testTaw2 - testTaw1) / testTaw1 * 100
                biggestDiff = testTaw2 - testTaw1
            elif testTaw2 - testTaw1 <= smallestDiff:
                smallestDiff = testTaw2 - testTaw1
                smallestDiffPer = (testTaw2 - testTaw1) / testTaw1 * 100
                smallestDiffSign = 'Lighter'
        elif testTaw3 == testTaw1 and testTaw2 > testTaw3 and counterTest == 0:
            totalWeightDiffHeavy += testTaw2 - testTaw3
            heavierBox += 1
            totalPerDiffHeavy += (testTaw2 - testTaw3) / testTaw3 * 100
            if testTaw2 - testTaw3 >= biggestDiff:
                biggestDiffSign = 'Heavier'
                biggestDiffPer = (testTaw2 - testTaw3) / testTaw3 * 100
                biggestDiff = testTaw2 - testTaw3
            elif testTaw2 - testTaw3 <= smallestDiff:
                smallestDiff = testTaw2 - testTaw3
                smallestDiffPer = (testTaw2 - testTaw3) / testTaw3 * 100
                smallestDiffSign = 'Heavier'
        elif testTaw3 == testTaw1 and testTaw2 < testTaw3 and counterTest == 0:
            totalWeightDiffLight += testTaw3 - testTaw2
            lighterBox += 1
            totalPerDiffLight += (testTaw3 - testTaw2) / testTaw2 * 100
            if testTaw3 - testTaw2 >= biggestDiff:
                biggestDiffSign = 'Lighter'
                biggestDiffPer = (testTaw3 - testTaw2) / testTaw2 * 100
                biggestDiff = testTaw3 - testTaw2
            elif testTaw3 - testTaw2 <= smallestDiff:
                smallestDiff = testTaw3 - testTaw2
                smallestDiffPer = (testTaw3 - testTaw2) / testTaw2 * 100
                smallestDiffSign = 'Lighter'
        elif testTaw1 == testTaw2 and testTaw3 > testTaw2 and counterTest == 0:
            totalWeightDiffHeavy += testTaw3 - testTaw2
            heavierBox += 1
            totalPerDiffHeavy += (testTaw3 - testTaw2) / testTaw2 * 100
            if testTaw3 - testTaw2 >= biggestDiff:
                biggestDiffSign = 'Heavier'
                biggestDiffPer = (testTaw3 - testTaw2) / testTaw2 * 100
                biggestDiff = testTaw3 - testTaw2
            elif testTaw3 - testTaw2 <= smallestDiff:
                smallestDiff = testTaw3 - testTaw2
                smallestDiffPer = (testTaw3 - testTaw2) / testTaw2 * 100
                smallestDiffSign = 'Heavier'
        elif testTaw1 == testTaw2 and testTaw3 < testTaw2 and counterTest == 0:
            totalWeightDiffLight += testTaw2 - testTaw3
            lighterBox += 1
            totalPerDiffLight += (testTaw2 - testTaw3) / testTaw3 * 100
            if testTaw2 - testTaw3 >= biggestDiff:
                biggestDiffSign = 'Lighter'
                biggestDiffPer = (testTaw2 - testTaw3) / testTaw3 * 100
                biggestDiff = testTaw2 - testTaw3
            elif testTaw2 - testTaw3 <= smallestDiff:
                smallestDiff = testTaw2 - testTaw3
                smallestDiffPer = (testTaw2 - testTaw3) / testTaw3 * 100
                smallestDiffSign = 'Lighter'
        toContinue = input("Is There Other Boxes (y,Y,n,N):")
        while toContinue not in ['y', 'Y', 'n', 'N']:
            print("Incorrect Data Entry, Please Try Again!")
            toContinue = input("Is There Other Boxes (y,Y,n,N):")
    else:
        testCounter = 0
        for taw in range(4, numberTaws + 1):
            tawWeight = int(input("Enter One Of The Taw's Weight:"))
            while tawWeight <= 0:
                print("Weight Can Not Be Negative or Equal To Zero!")
                tawWeight = int(input("Enter One Of The Taw's Weight:"))
            if tawWeight != testTaw1:
                maxDiffNumber -= 1    #If maxDiffNumber == 0 Then We Can Say The Taw Series Looks Like 10 10 10 20 20
                if maxDiffNumber <= 0:
                    returnedBox += 1
                    returnedTaws += numberTaws
                    testCounter += 1
                    if equalHeavierCounter == 1:
                        heavierBox -= 1
                        totalPerDiffHeavy -= heavierTest
                        totalWeightDiffHeavy -= heavierWeightTest
                    else:
                        lighterBox -= 1
                        totalPerDiffLight -= lighterTest
                        totalWeightDiffLight -= lighterWeightTest

                    break
                if tawWeight < testTaw1:
                    equalLightCounter += 1
                    lighterBox += 1
                    lighterTest = (testTaw1 - tawWeight) / tawWeight * 100
                    lighterWeightTest = testTaw1 - tawWeight
                    totalPerDiffLight += lighterTest
                    totalWeightDiffLight += lighterWeightTest
                    testCounter += 1
                else:
                    equalHeavierNumber += 1
                    heavierBox += 1
                    heavierTest = (tawWeight - testTaw1) / testTaw1 * 100
                    heavierWeightTest = tawWeight - testTaw1
                    totalPerDiffHeavy += heavierTest
                    totalWeightDiffHeavy += heavierWeightTest
                    testCounter += 1
        if testCounter == 0:
            equalBox += 1
            if tawWeight > equalHeavierWeight:
                equalHeavierNumber = numberTaws
                equalHeavierWeight = tawWeight
            if numberTaws > equalNumber:
                equalNumber = numberTaws
                equalWeight = tawWeight

        toContinue = input("Is There Other Boxes (y,Y,n,N):")
        while toContinue not in ['y', 'Y', 'n', 'N']:
            print("Incorrect Data Entry, Please Try Again!")
            toContinue = input("Is There Other Boxes (y,Y,n,N):")

print("\n\t\t\tProgram Finished!\n\n\t\t\t******RESULTS*****")
acceptedBoxes = numberBoxes - returnedBox
acceptedTaws = totalTaws - returnedTaws
avgDiffHeavier = totalWeightDiffHeavy / heavierBox
avgDiffLighter = totalWeightDiffLight / lighterBox
perReturnedBox = (returnedBox / numberBoxes) * 100
perLighterBox = (lighterBox / acceptedBoxes) * 100
perHeavierBox = (heavierBox / acceptedBoxes) * 100
perEqualBox = (equalBox / acceptedBoxes) * 100
print(f"Number Of Boxes With Manufacturing Defects: {returnedBox}\n"
      f"Percentage Of Boxes With Manufacturing Defects In All Boxes: %{perReturnedBox:.2f}")
print(f"Number Of Taws Returned: {returnedTaws}\nNumber Of Taws Accepted: {acceptedTaws}")
print(f"Number Of Boxes In Which All Taws Are Equal Weight : {equalBox}\n"
      f"Number Of Boxes Which Have A One Heavier Taw: {heavierBox}\n"
      f"Number Of Boxes Which Have A One Lighter Taw: {lighterBox}\n"
      f"Percentage Of Boxes Which All Taws Are Equal Weight : %{perEqualBox:.2f}\n"
      f"Percentage Of Boxes Which Have A One Heavier Taw: %{perHeavierBox:.2f}\n"
      f"Percentage Of Boxes Which Have A One Lighter Taw: %{perLighterBox:.2f}")
print(f"Average Of Weight Differences Between Heavier and Normal Taws In "
      f"Boxes Which Have One Different Taw: {avgDiffHeavier:.2f}\n"
      f"Average Of Weight Differences Between Lighter and Normal Taws In "
       f"Boxes Which Have One Different Taw: {avgDiffLighter:.2f}\n"
      f"Percentage Of Weight Differences Between Heavier and Normal Taws In "
      f"Boxes Which Has One Different Taw: %{totalPerDiffHeavy/heavierBox:.2f}\n"
      f"Percentage Of Weight Differences Between Lighter and Normal Taws In "
      f"Boxes Which Has One Different Taw: %{totalPerDiffLight/lighterBox:.2f}")
print(f"Number Of Taws In The Box Which Have Highest Equal Taw Number: {equalNumber}\n"
      f"Weight Of Taws In The Box Which Have Highest Equal Taw Number: {equalWeight}")
print(f"Number Of Taws In The Equal Weighted Box Which Have Heaviest Taws: {equalHeavierNumber}\n"
      f"Weight Of Taws In The Equal Weighted Box Which Have Heaviest Taws: {equalHeavierWeight}")
print(f"Biggest Difference Between Two Taws In One Box Is : {biggestDiff}({biggestDiffSign})(%{biggestDiffPer:.2f})")
print(f"Smallest Difference Between Two Taws In One Box Is : {smallestDiff}({smallestDiffSign})(%{smallestDiffPer:.2f})")
print()