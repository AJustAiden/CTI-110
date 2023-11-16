#Aiden Allison
#11/16/23
#Using if else staments, loops , funcations and random numbers
import random

def Adding():
    num_1 = random.randint(0,10)
    num_2 = random.randint(0,10)
    Sum = num_1 + num_2 
    Answer = int(input(f"What is the sum of {num_1} + {num_2}: "))
    guessCount = 1
    while Answer != Sum:
        if Answer > Sum:
            print("your guess was too high: ")
            Answer = int(input(f"What is the sum of {num_1} + {num_2}: "))
            guessCount += 1
        elif Answer < Sum:
            print("your guess was too low: ")
            Answer = int(input(f"What is the sum of {num_1} + {num_2}: "))
            guessCount += 1
    print("good job you got it right!!")
    print(f"you guessed {guessCount} times")

def Minus():
    num_1 = random.randint(0,10)
    num_2 = random.randint(0,10)
    Sum = num_1 - num_2
    Answer = int(input(f"What is the sum of {num_1} - {num_2}: "))
    guessCount = 1
    while Answer != Sum:
        if Answer > Sum:
            print("your guess was too high: ")
            Answer = int(input(f"What is the sum of {num_1} - {num_2}: "))
            guessCount += 1
        elif Answer < Sum:
            print("your guess was too low: ")
            Answer = int(input(f"What is the sum of {num_1} - {num_2}: "))
            guessCount += 1
    print("good job you got it right!!")
    print(f"you guessed {guessCount} times")
def guessing():
    
    
def menu():
    print("MAIN MENU")
    print("-------------------------------")
    print("1.Adding Random numbers")
    print("2.Subtracting Random Numbers")
    print("3.Exit")
def Exit():
    ("program over")
#mainfunction that runs program
def main():
    menu()
    menuNum = int(input("Please choose one of the menu options: "))

    if menuNum == 1:
        Adding()
    elif menuNum == 2:
        Minus()
    elif menuNum == 3:
        Exit()
    else:
         print("error wrong number")
         menu()
#Call the mainfunction
if __name__ == "__main__":
    main()
