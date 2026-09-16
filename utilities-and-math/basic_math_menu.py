def getNumber(lowerLimit, upperLimit):
    number = int(input("Enter Number:"))
    while number < lowerLimit or number > upperLimit:
        number = int(input("Incorrect Data Entry, Please Enter Again:"))
    return number


def drawRectangle(verticalSide, horizontalSide):
    for i in range(verticalSide):
        for j in range(horizontalSide):
            print('*', end=' ')
        print('')


def calculateRectangleInfo(side1, side2):
    return side1 * side2, 2 * (side1 + side2), side1 == side2  # if true it is square


def factorial(number):
    product = 1
    for multiplier in range(number, 1, -1):
        product = product * multiplier
    return product


def combination(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


def showMenu():
    print("1.Draw Rectangle")
    print("2.Calculate Info Of Rectangle")
    print("3.Calculate Factorial")
    print("4.Calculate Combination [C(n,k)]")
    print("0.Exit")


def main():
    exit = 'n'
    while exit == 'N' or exit == 'n':
        showMenu()
        selection = getNumber(0, 4)
        if selection == 1:
            print("Enter The Vertical Side Length Of The Rectangle [1,20]:", end='')
            verticalSide = getNumber(1, 20)
            print("Enter The Horizontal Side Length Of The Rectangle [1,20]:", end='')
            horizontalSide = getNumber(1, 75)
            drawRectangle(verticalSide, horizontalSide)
        elif selection == 2:
            print("Enter The Length Of One Side Of The Rectangle[1,1000]:", end='')
            side1 = getNumber(1, 1000)
            print("Enter The Length Of One Side Of The Rectangle[1,1000]:", end='')
            side2 = getNumber(1, 1000)
            area, perimeter, square = calculateRectangleInfo(side1, side2)
            if square:
                print("This Rectangle Is A Square.")

        elif selection == 3:
            print("Enter The Number That You Want To Calculate Factorial[0,10]:")
            number = getNumber(0, 10)
            print(f"The Result Is {number}!={factorial(number)}")

        elif selection == 4:
            print("Enter The Number n For The Combination C(n,k) [1,10]:")
            n = getNumber(1, 10)
            print("Enter The Number k For The Combination C(n,k) [1,{n}]:")
            k = getNumber(1, n)
            print(f"C({n},{k})={combination(n, k)}")

        else:
            exit = input("Are You Sure You Want To Exit (y,Y,n,N) ?:")
            while exit not in ['y', 'Y', 'n', 'N']:
                exit = input("Incorrect Data Entry Please Try Again:")


main()
