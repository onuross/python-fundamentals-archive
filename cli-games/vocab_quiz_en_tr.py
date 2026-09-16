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
    english = open("wordsEnglish.txt", "r")
    englishWords = english.readlines()
    turkish = open("wordsTurkish.txt", "r")
    turkishWords = turkish.readlines()
    lenFile = len(englishWords)
    line = random.randint(0, lenFile + 1)
    wordEnglish = englishWords[line]
    wordEnglish = wordEnglish.rstrip()
    wordTurkish = turkishWords[line]
    wordTurkish = wordTurkish.rstrip()
    turkishWord = input(wordEnglish+ " : ")
    if turkishWord.lower() != wordTurkish.lower():
        print(f"Wrong Entry, The Word In Turkish Is ( {wordTurkish} )")
    else:
        print("Correct!")
    return turkishWord


def gameReverse():
    import random
    english = open("wordsEnglish.txt", "r")
    englishWords = english.readlines()
    turkish = open("wordsTurkish.txt", "r")
    turkishWords = turkish.readlines()
    lenFile = len(englishWords)
    line = random.randint(0,lenFile+1)
    wordEnglish = englishWords[line]
    wordEnglish = wordEnglish.rstrip()
    wordTurkish = turkishWords[line]
    wordTurkish = wordTurkish.rstrip()
    englishWord = input(wordTurkish + " : ")
    if englishWord.lower() != wordEnglish.lower():
        print(f"Wrong Entry, The Word In English Is ( {wordEnglish} )")
    else:
        print("Correct!")
    return englishWord


def gameRandom():
    import random
    gameChoose = random.randint(0,2)
    if gameChoose == 1:
        word = game()
    else:
        word = gameReverse()
    return word


def wordAdd():
    english = open("wordsEnglish.txt", "a")
    english2 = open("wordsEnglish.txt","r")
    englishList = english2.readlines()
    turkish = open("wordsTurkish.txt", "a")
    cont = "y"
    while cont in ["y", "Y"]:
        wordEnglish = input("Enter The Word In English:")
        wordTurkish = input("Enter The Word In Turkish:")
        while not (wordEnglish.isalpha() or wordTurkish.isalpha()):
            print("Incorrect Entry, Please Enter The Words In Alphabetic Characters")
            wordEnglish = input("Enter The Word In English:")
            wordTurkish = input("Enter The Word In Turkish:")
        if wordEnglish in englishList:
            print("The Word That You Are Trying To Enter Is Already in The List")
            cont = input("Do You Want To Add More Words (y/n):")
        else:
            english.write(wordEnglish + "\n")
            turkish.write(wordTurkish + "\n")
            cont = input("Do You Want To Add More Words (y/n):")


def menuPrinter():
    print("1.Play Game Turkish->English")
    print("2.Play Game English->Turkish")
    print("3.Play Randomly")
    print("4.Add More Words")
    print("5.Quit The Game")
    choose = int(input("Please Enter The Menu Number That You Want To Choose:"))
    while choose not in [1,2,3,4,5]:
        choose = int(input("Please Enter The Menu Number That You Want To Choose:"))
    return choose


if __name__ == '__main__':
    main()