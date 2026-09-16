def main():
    choose = menuPrinter()
    if choose == 5:
        quit()
    elif choose == 4:
        wordAdd()
    elif choose == 3:
        word = gameRandom()
        while word != " ":
            word = gameRandom()
    elif choose == 2:
        word = game()
        while word != " " and choose != 3:
            game()
    else:
        word = gameReverse()
        while word != " " and choose != 3:
            gameReverse()


def game():
    import random
    german = open("germanWords.txt", "r")
    germanWords = german.readlines()
    turkish = open("turkishWords.txt", "r")
    turkishWords = turkish.readlines()
    lenFile = len(germanWords)
    line = random.randint(0, lenFile + 1)
    wordGerman = germanWords[line]
    wordGerman = wordGerman.rstrip()
    wordTurkish = turkishWords[line]
    wordTurkish = wordTurkish.rstrip()
    turkishWord = input(wordGerman+ " : ")
    if turkishWord.lower() != wordTurkish.lower():
        print(f"Wrong Entry, The Word In Turkish Is ( {wordTurkish} )")
    else:
        print("Correct!")
    return turkishWord


def gameReverse():
    import random
    german = open("germanWords.txt", "r")
    germanWords = german.readlines()
    turkish = open("turkishWords.txt", "r")
    turkishWords = turkish.readlines()
    lenFile = len(germanWords)
    line = random.randint(0,lenFile+1)
    wordGerman = germanWords[line]
    wordGerman = wordGerman.rstrip()
    wordTurkish = turkishWords[line]
    wordTurkish = wordTurkish.rstrip()
    germanWord = input(wordTurkish + " : ")
    if germanWord.lower() != wordGerman.lower():
        print(f"Wrong Entry, The Word In Deutsch Is ( {wordGerman} )")
    else:
        print("Correct!")
    return germanWord


def gameRandom():
    import random
    gameChoose = random.randint(0,2)
    if gameChoose == 1:
        word = game()
    else:
        word = gameReverse()
    return word


def wordAdd():
    german = open("germanWords.txt", "a")
    german2 = open("germanWords.txt","r")
    germanList = german2.readlines()
    turkish = open("turkishWords.txt", "a")
    cont = "y"
    while cont in ["y", "Y"]:
        wordGerman = input("Enter The Word In Deutsch:")
        wordTurkish = input("Enter The Word In Turkish:")
        while not (wordGerman.isalpha() or wordTurkish.isalpha()):
            print("Incorrect Entry, Please Enter The Words In Alphabetic Characters")
            wordGerman = input("Enter The Word In Deutsch:")
            wordTurkish = input("Enter The Word In Turkish:")
        if wordGerman in germanList:
            print("The Word That You Are Trying To Enter Is Already in The List")
            cont = input("Do You Want To Add Another Words (y/n):")
        else:
            german.write(wordGerman + "\n")
            turkish.write(wordTurkish + "\n")
            cont = input("Do You Want To Add More Words (y/n):")


def menuPrinter():
    print("1.Play Game Turkish->Deutsch")
    print("2.Play Game Deutsch->Turkish")
    print("3.Play Randomly")
    print("4.Add More Words")
    print("5.Quit The Game")
    choose = int(input("Please Enter The Menu Number That You Want To Choose:"))
    while choose not in [1,2,3,4,5]:
        choose = int(input("Please Enter The Menu Number That You Want To Choose:"))
    return choose


if __name__ == '__main__':
    main()