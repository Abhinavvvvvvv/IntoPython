import random

topRange = input("Type a number: ")

if topRange.isdigit():
    topRange = int(topRange)

    if topRange <= 0:
        print("Please type a number larger than 0.")
        quit()

else:
    print("Please type a number.")
    quit()


randomNumber = random.randint(0, topRange)
guesses = 0

while True:
    guesses += 1
    
    guessUser = input("Make a guess: ")
    if guessUser.isdigit():
        guessUser = int(guessUser)
    else:
        print("Please type a number next time.")
        continue

    if guessUser == randomNumber:
        print("GOTCHA!!!!")
        break
    elif guessUser > randomNumber:
        print("Go down!")
    else:
        print("Go up!")

print("You got it in", guesses, "guesses")
