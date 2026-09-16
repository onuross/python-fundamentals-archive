def main():
    possiblePointList = [10, 9, 8, 7, 6, 5, 0]
    minNumberArcher = 8
    nameList = []
    numberArchers = int(input("Enter The Number Of Archers:"))
    while numberArchers < minNumberArcher:
        print(f"Number Of Archers Should Be More Than {minNumberArcher-1}")
        try:
            numberArchers = int(input("Enter The Number Of Archers:"))
        except ValueError:
            print("Number Of Archers Should Be An Integer! Please Try Again")
            numberArchers = int(input("Enter The Number Of Archers:"))
    takeName(nameList,numberArchers)
    try:
        numberShots = int(input("Enter The Number Of Shots For One Archer:"))
    except ValueError:
        print("Number Of Shots Should Be Integer! Please Try Again.")
        numberShots = int(input("Enter The Number Of Shots For One Archer:"))
    pointList = [0] * numberArchers
    xAreaList = [0] * numberArchers
    tenPointList = [0] * numberArchers
    takePoint(numberShots, pointList, numberArchers, xAreaList,tenPointList, possiblePointList)
    statistics(numberArchers, pointList, nameList, xAreaList, tenPointList)

def takeName(nameList, numberArchers):
    for archerNo in range(numberArchers):
        try:
            name = str(input(f"Enter The Name-Surname For {archerNo+1}.Archer:"))
        except ValueError:
            print("Name Can Not Include A Number! Please Try Again.")
            name = str(input(f"Enter The Name-Surname For {archerNo+1}.Archer:"))
        nameList.insert(archerNo, name)

def takePoint(numberShots, pointList, numberArchers, xAreaList, tenPointList, possiblePointList):
    for shotNo in range(numberShots):
        for archerNo in range(numberArchers):
            try:
                point = int(input(f"Enter The {archerNo+1}.Archer's {shotNo+1}.Shot's Point:"))
            except ValueError:
                print("Point Should Be An Integer! Please Try Again.")
            while point not in possiblePointList:
                print("Points Can Take These Values (10,9,8,7,6,5,0)! Please Try Again.")
                point = int(input(f"Enter The {archerNo+1}.Archer's {shotNo+1}.Shot's Point:"))
            if point==10:
                tenPointList[archerNo] += 1
                xArea = input("Did He/She Hit The X Area (y,n):")
                if xArea=='y':
                    xAreaList[archerNo] += 1
            pointList[archerNo] += point

def statistics(numberArchers, pointList, nameList, xAreaList, tenPointList):
    print("Rank     Name-Surname    Points     10Count     XCount")
    print("----     ------------    ------     -------     ------")
    for archerNo2 in range(1, numberArchers+1):
        try:
            maxIndex = pointList.index(max(pointList))
        except ValueError:
            break
        if pointList.count(pointList[maxIndex]) > 1:
            if max(tenPointList) == 0:
                temp = pointList.count(max(pointList))
                maxIndex = pointList.index(max(pointList))
                for i in range(temp):
                    write(archerNo2, maxIndex, nameList, pointList, tenPointList, xAreaList)
                continue
            else:
                if tenPointList.count(tenPointList[maxIndex]) > 1:
                    if max(xAreaList) == 0:
                        temp = tenPointList.count(max(tenPointList))
                        maxIndex = tenPointList.index(max(tenPointList))
                        for i in range(temp):
                            write(archerNo2, maxIndex, nameList, pointList, tenPointList, xAreaList)
                        continue
                    else:
                        maxIndex = xAreaList.index(max(xAreaList))
                        write(archerNo2, maxIndex, nameList, pointList, tenPointList, xAreaList)
                else:
                    maxIndex = tenPointList.index(max(tenPointList))
                    write(archerNo2, maxIndex, nameList, pointList, tenPointList, xAreaList)
        else:
            maxIndex = pointList.index(max(pointList))
            write(archerNo2, maxIndex, nameList, pointList, tenPointList, xAreaList)

def write(archerNo2,maxIndex, nameList, pointList, tenPointList, xAreaList):
    rank = archerNo2
    maxPoint = pointList[maxIndex]
    pointList.pop(maxIndex)
    maxName = nameList[maxIndex]
    nameList.pop(maxIndex)
    maxTenShot = tenPointList[maxIndex]
    tenPointList.pop(maxIndex)
    maxXAreaShot = xAreaList[maxIndex]
    xAreaList.pop(maxIndex)
    print(f"  {rank}.", end="     ")
    print(f"{maxName:12s}",  end="  ")
    print(f"{maxPoint:6d}",  end="  ")
    print(f"{maxTenShot:9d}",  end="  ")
    print(f"{maxXAreaShot:9d}",  end="  ")
    print()

main()