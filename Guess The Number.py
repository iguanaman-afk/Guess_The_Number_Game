import random

myName = input("Hello, What is your name?")
numberFound = False

number = random.randint(1, 20)
trys = 0

while (numberFound != True) and (trys < 5):
    guess = int(input("well, " + myName + " I am thinking of a number between 1 and 20."))
    if guess == number:
        print("Yes " + myName + ", that's right!")
        numberFound = True
    else:
        print("No " + myName + ", that's not right. Try again.")
        trys += 1
        if guess < number:
            print("Your guess is too low.")
        if guess > number:
            print("Your guess is too high.")
    if (trys == 5) and numberFound == False:
        print("Sorry " + myName + ", your dumb as shit, you lost motherfucker!")