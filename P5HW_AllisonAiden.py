# Aiden Allison
# 11/16/23
# Using if else statements, loops , functions and random numbers
import random


def Adding():
    num_1 = random.randint(0, 10)
    num_2 = random.randint(0, 10)
    global Sum
    Sum = num_1 + num_2


def Minus():
    num_1 = random.randint(0, 10)
    num_2 = random.randint(0, 10)
    global Sum
    Sum = num_1 - num_2


def guessing():
    guessCount = 1
    Answer = int(input(f"What is your guess? "))
    while Answer != Sum:
        if Answer > Sum:
            print("your guess was too high: ")
            Answer = int(input(f"What is your guess? "))
            guessCount += 1
        elif Answer < Sum:
            print("your guess was too low: ")
            Answer = int(input(f"What is your guess? "))
            guessCount += 1
    print("good job you got it right!!")
    print(f"you guessed {guessCount} times")

def menu():
    print("MAIN MENU")
    print("-------------------------------")
    print("1.Adding Random numbers")
    print("2.Subtracting Random Numbers")
    print("3.Exit")
    global menuNum
    menuNum = int(input("Please choose one of the menu options: "))

def Exit():
    ("program over")


# mainfunction that runs program
def main():
    menu()

    if menuNum == 1:
        Adding()
        print(Sum)
        guessing()
    elif menuNum == 2:
        Minus()
        print(Sum)
        guessing()
    elif menuNum == 3:
        Exit()
    else:
        print("error none usable number")
        menu()
    exit()
# Call the main function
if __name__ == "__main__":
    main()
