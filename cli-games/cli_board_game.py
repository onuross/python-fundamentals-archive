def main():
    cont = 'Y'
    player1, player2 = takePlayer()
    while cont == 'Y':
        counter = 1
        area = takeArea()
        areaList = playingArea(area, player1, player2)
        finish = False
        printArea(area, areaList)
        while not finish:
            if counter % 2 == 0:
                player = player2
                row, column = takeMoves(areaList, player)
                try:
                    lockedNo, lockedLet = stoneEater(area, areaList, player2, player1, row, column)
                    printArea(area, areaList)
                    print(f"The Stone At Position {lockedNo}{lockedLet} Was Locked And Removed.")
                except TypeError:
                    printArea(area, areaList)
            else:
                player = player1
                row, column = takeMoves(areaList, player)
                try:
                    lockedNo, lockedLet = stoneEater(area, areaList, player1, player2, row, column)
                    printArea(area, areaList)
                    print(f"The Stone At Position {lockedNo}{lockedLet} Was Locked And Removed.")
                except TypeError:
                    printArea(area, areaList)
            counter += 1
            finish = finishChecker(areaList, player1, player2)
        cont = input("Would You Like To Play Again(Y/N)?:")
        while cont not in ['Y','N']:
            print("Incorrect Entry! Please Try Again.")
            cont = input("Would You Like To Play Again(Y/N)?:")

def takeArea():
    try:
        area = int(input("Enter The Row/Column Number Of Playing Field (4-8):"))
        while area < 4 or area > 8:
            print("The Playing Field Should Be At Least 4x4 or Most 8x8! Please Enter Again.")
            area = int(input("Enter The Row/Column Number Of Playing Field (4-8):"))
    except ValueError:
        print("The Numbers That Determine The Playing Field Must Be Positive Integers! Please Enter Again.")
        area = int(input("Enter The Row/Column Number Of Playing Field (4-8):"))
    return area

def takePlayer():
    player1 = input("Enter A Character To Represent Player 1:")
    while len(player1) > 1 or player1 == " " or player1 == "":
        print("Please Enter One Character For Every Player!")
        player1 = input("Enter A Character To Represent Player 1:")
    player2 = input("Enter A Character To Represent Player 2:")
    while len(player2) > 1 or player2 == " " or player2 == "":
        print("Please Enter One Character For Every Player!")
        player2 = input("Enter A Character To Represent Player 2:")
    return player1, player2

def playingArea(area, player1, player2):
    areaList = []
    for i in range(area):
        tempList = [" "] * area
        areaList.append(tempList)
    for i in range(area):
        areaList[area - 1][i] = player1
        areaList[0][i] = player2
    return areaList

def printArea(area,areaList):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    print(" ", end="")
    for i in range(area):
        print("   ", end="")
        print(letters[i], end="")
    print()
    if area == 4:
        print("  -----------------")
    elif area == 5:
        print("  ---------------------")
    elif area == 6:
        print("  -------------------------")
    elif area == 7:
        print("  -----------------------------")
    elif area == 8:
        print("  ---------------------------------")
    for i in range(area):
        print(numbers[i], "|", end="")
        for j in range(area):
            print(f" {areaList[i][j]} |", end="")
        print('', numbers[i])
        if area == 4:
            print("  -----------------")
        elif area == 5:
            print("  ---------------------")
        elif area == 6:
            print("  -------------------------")
        elif area == 7:
            print("  -----------------------------")
        elif area == 8:
            print("  ---------------------------------")
    print("  ", end="")
    for i in range(area):
        print("  ", end="")
        print(letters[i], end=" ")
    print()

def checkPath(areaList, movement, fromRow, fromColumn, toRow, toColumn, player):
    checker = True
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    tempList = []
    if fromRow == toRow:
        if fromColumn > toColumn and fromColumn - toColumn > 1:
            tempList = areaList[fromRow][toColumn + 1 : fromColumn]
            if len(tempList) != tempList.count(" "):
                checker = False
        elif fromColumn < toColumn and toColumn - fromColumn > 1:
            tempList = areaList[fromRow][fromColumn + 1 : toColumn]
            if len(tempList) != tempList.count(" "):
                checker = False
    elif fromColumn == toColumn:
        if fromRow > toRow and fromRow - toRow > 1:
            for i in range(fromRow - toRow - 1):
                tempList.append(areaList[fromRow - i - 1][fromColumn])
            if len(tempList) != tempList.count(' '):
                checker = False
        elif toRow > fromRow and toRow - fromRow > 1:
            for i in range(toRow - fromRow - 1):
                tempList.append(areaList[fromRow + i + 1][fromColumn])
            if len(tempList) != tempList.count(' '):
                checker = False
    if areaList[toRow][toColumn] != " " or areaList[fromRow][fromColumn] != player or \
            not ((fromRow != toRow and fromColumn == toColumn) or (fromRow == toRow and fromColumn != toColumn)) \
            or len(movement) != 5 or int(movement[0]) not in numbers or int(movement[3]) not in numbers or\
            movement[1] not in letters or movement[4] not in letters or not checker:
        checker = False

    return checker

def takeMoves(areaList, player):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    movement = (input(f"Enter Player {player}'s Movement (From To) Ex.(1C 2C):")).upper()
    while len(movement) != 5 or \
            int(movement[0]) not in numbers or int(movement[3]) not in numbers or\
                movement[1] not in letters or movement[4] not in letters:
        print("Incorrect Entry! Please Try Again.")
        movement = (input(f"Enter Player {player}'s Movement (From To) Ex.(1C 2C):")).upper()
    fromRow = numbers.index(int(movement[0]))
    fromColumn = letters.index(movement[1])
    toRow = numbers.index(int(movement[3]))
    toColumn = letters.index(movement[4])
    check = checkPath(areaList, movement, fromRow, fromColumn, toRow, toColumn, player)
    while not check:
        print("Incorrect Entry! Please Try Again.")
        movement = (input(f"Enter Player {player}'s Movement (From To) Ex.(1C 2C):")).upper()
        fromRow = numbers.index(int(movement[0]))
        fromColumn = letters.index(movement[1])
        toRow = numbers.index(int(movement[3]))
        toColumn = letters.index(movement[4])
        check = checkPath(areaList, movement, fromRow, fromColumn, toRow, toColumn, player)
    areaList[fromRow][fromColumn] = " "
    areaList[toRow][toColumn] = player
    return toRow, toColumn

def stoneEater(area, areaList, player1, player2, lastRow, lastColumn):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    stone = False
    lockedNo = None
    lockedLet = None
    if areaList[area - 1][area - 1] == player2 and areaList[area - 2][area - 1] == player1 \
            and areaList[area - 1][area - 2] == player1:
        areaList[area - 1][area - 1] = " "
        lockedNo, lockedLet = numbers[area - 1], letters[area - 1]
        stone = True
    elif areaList[area - 1][0] == player2 and areaList[area - 2][0] == player1 and areaList[area - 1][1] == player1:
        areaList[area - 1][0] = " "
        lockedNo, lockedLet = numbers[area - 1], letters[0]
        stone = True
    elif areaList[0][area - 1] == player2 and areaList[1][area - 1] == player1 and areaList[0][area - 2] == player1:
        areaList[0][area - 1] = " "
        lockedNo, lockedLet = numbers[0], letters[area - 1]
        stone = True
    elif areaList[0][0] == player2 and areaList[1][0] == player1 and areaList[0][1] == player1:
        areaList[0][0] = " "
        lockedNo, lockedLet = numbers[0], letters[0]
        stone = True

    if area - 2 > lastColumn > 1 and area - 2 > lastRow > 1:
        if areaList[lastRow][lastColumn - 2] == player1 and areaList[lastRow][lastColumn - 1] == player2 and \
                areaList[lastRow][lastColumn + 2] == player1 and areaList[lastRow][lastColumn + 1] == player2:
            areaList[lastRow][lastColumn - 1] = " "
            areaList[lastRow][lastColumn + 1] = " "
            lockedNo, lockedLet = (str(numbers[lastRow]) + letters[lastColumn - 1]), (
                    str(numbers[lastRow]) + letters[lastColumn + 1])
            stone = True
        if areaList[lastRow - 2][lastColumn] == player1 and areaList[lastRow - 1][lastColumn] == player2 and \
                areaList[lastRow + 2][lastColumn] == player1 and areaList[lastRow + 1][lastColumn] == player2:
            areaList[lastRow + 1][lastColumn] = " "
            areaList[lastRow - 1][lastColumn] = " "
            lockedNo, lockedLet = (str(numbers[lastRow - 1]) + letters[lastColumn]), (
                    str(numbers[lastRow + 1]) + letters[lastColumn])
            stone = True
        if areaList[lastRow][lastColumn - 2] == player1 and areaList[lastRow][lastColumn - 1] == player2:
            areaList[lastRow][lastColumn - 1] = " "
            lockedNo, lockedLet = numbers[lastRow], letters[lastColumn - 1]
            stone = True
        elif areaList[lastRow][lastColumn + 2] == player1 and areaList[lastRow][lastColumn + 1] == player2:
            areaList[lastRow][lastColumn + 1] = " "
            lockedNo, lockedLet = numbers[lastRow], letters[lastColumn + 1]
            stone = True
        elif areaList[lastRow - 2][lastColumn] == player1 and areaList[lastRow - 1][lastColumn] == player2:
            areaList[lastRow - 1][lastColumn] = " "
            lockedNo, lockedLet = numbers[lastRow - 1], letters[lastColumn]
            stone = True
        elif areaList[lastRow + 2][lastColumn] == player1 and areaList[lastRow + 1][lastColumn] == player2:
            areaList[lastRow + 1][lastColumn] = " "
            lockedNo, lockedLet = numbers[lastRow + 1], letters[lastColumn]
            stone = True
    elif lastRow < 2:
        if areaList[lastRow + 2][lastColumn] == player1 and areaList[lastRow + 1][lastColumn] == player2:
            areaList[lastRow + 1][lastColumn] = " "
            lockedNo, lockedLet = numbers[lastRow + 1], letters[lastColumn]
            stone = True
        elif area - 2 > lastColumn > 1:
            if areaList[lastRow][lastColumn - 2] == player1 and areaList[lastRow][lastColumn - 1] == player2 and \
                    areaList[lastRow][lastColumn + 2] == player1 and areaList[lastRow][lastColumn + 1] == player2:
                areaList[lastRow][lastColumn - 1] = " "
                areaList[lastRow][lastColumn + 1] = " "
                lockedNo, lockedLet = (str(numbers[lastRow]) + letters[lastColumn - 1]), (
                        str(numbers[lastRow]) + letters[lastColumn + 1])
                stone = True
            if areaList[lastRow][lastColumn + 2] == player1 and areaList[lastRow][lastColumn + 1] == player2:
                areaList[lastRow][lastColumn + 1] = " "
                lockedNo, lockedLet = numbers[lastRow], letters[lastColumn + 1]
                stone = True
            elif areaList[lastRow][lastColumn - 2] == player1 and areaList[lastRow][lastColumn - 1] == player2:
                areaList[lastRow][lastColumn - 1] = " "
                lockedNo, lockedLet = numbers[lastRow], letters[lastColumn - 1]
                stone = True
        elif lastColumn < 2 and areaList[lastRow][lastColumn + 2] == player1\
                and areaList[lastRow][lastColumn + 1] == player2:
            areaList[lastRow][lastColumn + 1] = " "
            lockedNo, lockedLet = numbers[lastRow], letters[lastColumn + 1]
            stone = True
        elif lastColumn > area - 3 and areaList[lastRow][lastColumn - 2] == player1\
                and areaList[lastRow][lastColumn - 1] == player2:
            areaList[lastRow][lastColumn - 1] = " "
            lockedNo, lockedLet = numbers[lastRow], letters[lastColumn - 1]
            stone = True
    elif lastRow > area - 3:
        if areaList[lastRow - 2][lastColumn] == player1 and areaList[lastRow - 1][lastColumn] == player2:
            areaList[lastRow - 1][lastColumn] = " "
            lockedNo, lockedLet = numbers[lastRow - 1], letters[lastColumn]
            stone = True
        elif area - 2 > lastColumn > 1:
            if areaList[lastRow][lastColumn + 2] == player1 and areaList[lastRow][lastColumn + 1] == player2 and \
                    areaList[lastRow][lastColumn - 2] == player1 and areaList[lastRow][lastColumn - 1] == player2:
                areaList[lastRow][lastColumn - 1] = " "
                areaList[lastRow][lastColumn + 1] = " "
                lockedNo, lockedLet = (str(numbers[lastRow]) + letters[lastColumn - 1]), (
                        str(numbers[lastRow]) + letters[lastColumn + 1])
                stone = True
            if areaList[lastRow][lastColumn + 2] == player1 and areaList[lastRow][lastColumn + 1] == player2:
                areaList[lastRow][lastColumn + 1] = " "
                lockedNo, lockedLet = numbers[lastRow], letters[lastColumn + 1]
                stone = True
            elif areaList[lastRow][lastColumn - 2] == player1 and areaList[lastRow][lastColumn - 1] == player2:
                areaList[lastRow][lastColumn - 1] = " "
                lockedNo, lockedLet = numbers[lastRow], letters[lastColumn - 1]
                stone = True
        elif lastColumn < 2 and areaList[lastRow][lastColumn + 2] == player1 \
                and areaList[lastRow][lastColumn + 1] == player2:
            areaList[lastRow][lastColumn + 1] = " "
            lockedNo, lockedLet = numbers[lastRow], letters[lastColumn + 1]
            stone = True
        elif lastColumn > area - 3 and areaList[lastRow][lastColumn - 2] == player1 \
                and areaList[lastRow][lastColumn - 1] == player2:
            areaList[lastRow][lastColumn - 1] = " "
            lockedNo, lockedLet = numbers[lastRow], letters[lastColumn - 1]
            stone = True
    elif area - 2 > lastRow > 1 and lastColumn < 2:
        if areaList[lastRow + 2][lastColumn] == player1 and areaList[lastRow + 1][lastColumn] == player2 and \
                areaList[lastRow - 2][lastColumn] == player1 and areaList[lastRow - 1][lastColumn] == player2:
            areaList[lastRow - 1][lastColumn] = " "
            areaList[lastRow + 1][lastColumn] = " "
            lockedNo, lockedLet = (str(numbers[lastRow - 1]) + letters[lastColumn]), (
                    str(numbers[lastRow + 1]) + letters[lastColumn])
            stone = True
        if areaList[lastRow - 2][lastColumn] == player1 and areaList[lastRow - 1][lastColumn] == player2:
            areaList[lastRow - 1][lastColumn] = " "
            lockedNo, lockedLet = numbers[lastRow - 1], letters[lastColumn]
            stone = True
        elif areaList[lastRow + 2][lastColumn] == player1 and areaList[lastRow + 1][lastColumn] == player2:
            areaList[lastRow + 1][lastColumn] = " "
            lockedNo, lockedLet = numbers[lastRow + 1], letters[lastColumn]
            stone = True
        elif areaList[lastRow][lastColumn + 2] == player1 and areaList[lastRow][lastColumn + 1] == player2:
            areaList[lastRow][lastColumn + 1] = " "
            lockedNo, lockedLet = numbers[lastRow], letters[lastColumn + 1]
            stone = True
    elif area - 2 > lastRow > 1 and lastColumn > area - 3:
        if areaList[lastRow + 2][lastColumn] == player1 and areaList[lastRow + 1][lastColumn] == player2 and \
                areaList[lastRow - 2][lastColumn] == player1 and areaList[lastRow - 1][lastColumn] == player2:
            areaList[lastRow - 1][lastColumn] = " "
            areaList[lastRow + 1][lastColumn] = " "
            lockedNo, lockedLet = (str(numbers[lastRow - 1]) + letters[lastColumn]), (
                    str(numbers[lastRow + 1]) + letters[lastColumn])
            stone = True
        if areaList[lastRow - 2][lastColumn] == player1 and areaList[lastRow - 1][lastColumn] == player2:
            areaList[lastRow - 1][lastColumn] = " "
            lockedNo, lockedLet = numbers[lastRow - 1], letters[lastColumn]
            stone = True
        elif areaList[lastRow + 2][lastColumn] == player1 and areaList[lastRow + 1][lastColumn] == player2:
            areaList[lastRow + 1][lastColumn] = " "
            lockedNo, lockedLet = numbers[lastRow + 1], letters[lastColumn]
            stone = True
        elif areaList[lastRow][lastColumn - 2] == player1 and areaList[lastRow][lastColumn - 1] == player2:
            areaList[lastRow][lastColumn - 1] = " "
            lockedNo, lockedLet = numbers[lastRow], letters[lastColumn - 1]
            stone = True
    if stone:
        return lockedNo, lockedLet
    else:
        return None

def finishChecker(areaList, player1, player2):
    player1Count = 0
    player2Count = 0
    for tempList in areaList:
        for item in tempList:
            if item == player1:
                player1Count += 1
            elif item == player2:
                player2Count += 1
    if player2Count < 2:
        print(f"Player 1({player1}) Won The Game!")
        return True
    if player1Count < 2:
        print(f"Player 2({player2}) Won The Game!")
        return True

if __name__ == '__main__':
    main()