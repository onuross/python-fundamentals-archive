def main():
    fileName = languageSelect()
    word = wordChooser(fileName)
    letterInput(word)


def languageSelect():
    import random
    language = input("Enter The Word Language (turkish, english, random):")
    while language not in ["random", "english", "turkish"]:
        print("Incorrect Entry! Please Enter Again.")
        language = input("Enter The Word Language (english, turkish, random)")
    if language == "random":
        number = random.randint(0,2)
        if number == 1:
            return "turkish"
        elif number == 0:

            return "english"
    elif language == "english":
        return "english"
    else:
        return "turkish"


def wordChooser(fileName):
    import random
    if fileName == "turkish":
        file = open("worldsListTurkish.txt","r")
    else:
        file = open("wordsListEnglish.txt","r")
    tempList = file.readlines()
    length = len(tempList)
    number = random.randint(0,length-1)
    word = tempList[number]
    return word.rstrip()


def letterInput(word):
    length = len(word)
    letterShowList = ["-" for _ in range(length)]
    letterList = [item for item in word]
    letterShow = ""
    for element in letterShowList:
        letterShow += element
    print(letterShow)
    wrongCounter = 0
    cont = True
    while wrongCounter != length and cont and letterShowList.count("-") != 0:
        letter = input("Enter a Letter:")
        while len(letter) != 1 or letter.isalpha() == False:
            print("Incorrect Entry! Please Enter Again.")
            letter = input("Enter a Letter:")

        if letterShow == word:
            print("You Win!")
            print(f"The Word Is {word}")
            print("Game Ended!")
            cont = False

        if letter not in word:
            wrongCounter += 1
            if length == wrongCounter:
                cont = False
                print("You Lose!")
                print(f"The Word Was {word.capitalize()}")
                print("Game Ended!")
            else:
                print(f"Wrong! You Have {length-wrongCounter} More Tries!")
                print(letterShow)
        else:
            indices = findIndices(letterList,letter)
            for ix in indices:
                letterShowList[ix] = letter
            letterShow = ""
            for element in letterShowList:
                letterShow += element
            if letterShowList.count("-") != 0:
                print(f"Correct! You Have {length - wrongCounter} More Tries!")
                print(letterShow)

        if letterShowList.count("-") == 0:
            print("You Win!")
            print(f"The Word Is {word}")
            print("Game Ended!")
            cont = False

    if cont:
        print("You Lose!")
        print(f"The Word Was {word.capitalize()}")
        print("Game Ended!")



def findIndices(checkList, itemFind):
    indices = []
    for idx, value in enumerate(checkList):
        if value == itemFind:
            indices.append(idx)
    return indices


main()
