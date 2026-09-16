def main():
    possiblePoints = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    windDictionary = {"North": 0,
                      "South": 0,
                      "West": 0,  # Dictionary For Count The Missing Shot's Wind Conditions
                      "East": 0,
                      "Northwestern": 0,
                      "Northeastern": 0,
                      "Southwestern": 0,
                      "Southeastern": 0
                      }

    numberArchers = numberArcher()  # takes the number of archer
    numberShots = numberShot()  # takes the number of shots for everyone of archer
    pointList = listMaker(numberArchers, numberShots)  # creates the pointList for point table
    statistics(numberArchers, numberShots, possiblePoints, pointList, windDictionary)
    pointTableWrite(numberArchers, pointList, possiblePoints, numberShots)
    windTableWrite(windDictionary)


def numberArcher():  # takes the number of archer
    try:
        numberArchers = int(input("Enter The Number Of Archers:"))
        while numberArchers < 10:
            print("Number Of Archers In Competition Should Be At Least 10! Please Try Again.")
            numberArchers = int(input("Enter The Number Of Archers:"))
    except ValueError:
        print("Number Of Archers Should Be A Positive Integer! Please Try Again.")
        numberArchers = int(input("Enter The Number Of Archers:"))

    return numberArchers


def numberShot():  # takes the number of shots for everyone of archer
    try:
        numberShots = int(input("Enter The Number Of Shots:"))
        while numberShots < 0:
            print("Number Of Shots Should Be Positive Integer!")
            numberShots = int(input("Enter The Number Of Shots:"))
    except ValueError:
        print("Number Of Shots Should Be A Positive Integer! Please Try Again.")
        numberShots = int(input("Enter The Number Of Shots:"))

    return numberShots


def listMaker(numberArchers, numberShots):  # creates the pointList for point table
    pointList = []
    for i in range(numberArchers):  # Creating The Two Dimensional Point List [Archers No][Point Of Shot In Index]
        tempList = [0] * numberShots
        pointList.append(tempList)
    return pointList


def statistics(numberArchers, numberShots, possiblePoints, pointList, windDictionary):  # fills up the pointList
    # according to data taken
    # from user for point table
    for shot in range(numberShots):
        for archer in range(numberArchers):
            try:
                point = int(input(f"Enter The Point Of {archer + 1}.Archers {shot + 1}.Shot:"))

                while point < 0:
                    print("Point Should Be Positive Integer!")
                    point = int(input(f"Enter The Point Of {archer + 1}.Archers {shot + 1}.Shot:"))

                while point not in possiblePoints:
                    print("Point Can Take The Values Between 0,10! Please Try Again.")
                    point = int(input(f"Enter The Point Of {archer + 1}.Archers {shot + 1}.Shot:"))

            except ValueError:
                print("Point Should Be Integer And Should Be Equal Or More Than Zero!")
                point = int(input(f"Enter The Point Of {archer + 1}.Archers {shot + 1}.Shot:"))
                while point < 0:
                    print("Point Should Be Positive Integer!")
                    point = int(input(f"Enter The Point Of {archer + 1}.Archers {shot + 1}.Shot:"))

                while point not in possiblePoints:
                    print("Point Can Take The Values Between 0,10! Please Try Again.")
                    point = int(input(f"Enter The Point Of {archer + 1}.Archers {shot + 1}.Shot:"))

            pointList[archer][shot] = point

            windController(point, windDictionary)   # checking for wind data


def pointTableWrite(numberArchers, pointList, possiblePoints, numberShots):  # prints the point table
    print("\n\n")
    print("Archer Reg No    10p    9p     8p     7p     6p     5p     4p     3p     2p     1p     0p    Total")
    print("-------------   ----   ----   ----   ----   ----   ----   ----   ----   ----   ----   ----   -----")
    for archer in range(numberArchers):
        print(f"{archer + 1:<13}", end="  ")
        for point in possiblePoints:
            tempList = pointList[archer]
            pointCount = tempList.count(point)
            print(f"{pointCount:4d}", end="   ")
        total = sum(pointList[archer])
        print(f"{total:4d}", end="   ")
        print()
    allArchersPer(pointList, possiblePoints, numberArchers, numberShots)   # the percentages of archers points


def windController(point, windDictionary):   # arranges the wind dictionary
    if point == 0:
        wind = input("What Was The Wind Conditions In This Shot? (North, South etc.):")
        while wind not in windDictionary:
            print("Wind Condition Should Be Written Like: Northeastern, Northwestern.. Please Try Again.")
            wind = input("What Was The Wind Conditions In This Shot?:")
        windDictionary[wind] += 1
    return windDictionary


def windTableWrite(windDictionary):   # prints the wind dictionary table
    print()
    print(" Wind Name       Missed Shot Rate")
    print("------------     ----------------")
    total = 0
    for value in windDictionary.values():
        total += value
    for name in windDictionary:
        rate = windDictionary[name] / total * 100
        print(f"{name:<12}", end="     ")
        print(f"{rate:<16.2f}")


def allArchersPer(pointList, possiblePoints, numberArchers, numberShots):   # prints the percentages of archers points
    totalShotNumber = numberArchers * numberShots
    print(f"All Archers(%)", end="    ")
    for point in possiblePoints:
        total = 0
        for archer in range(numberArchers):
            tempList = pointList[archer]
            total += tempList.count(point)
        percentage = total / totalShotNumber * 100
        print(f"{percentage:<5.2f}", end="  ")
    print()


main()
