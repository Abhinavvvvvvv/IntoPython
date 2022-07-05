import random

userScore = 0
computerScore = 0

options = ["rock", "paper", "scissors"]

while True:
    userInput = input("Type Rock/Paper/Scissors or Q to quit:").lower()
    if userInput == "q":
        break

    if userInput not in options:
        continue
    
    randomNum = random.randint(0, 2)
    # rock: 0, paper: 1, scissors:2
    pickComputer = options[randomNum]
    print("Computer picked", pickComputer + ".")

    if userInput == "rock" and pickComputer == "scissors":
        print("WINNER WINNER!!!!")
        userScore += 1

    elif userInput == "paper" and pickComputer == "rock":
        print("WINNER WINNER!!!!")
        userScore += 1 

    elif userInput == "scissors" and pickComputer == "paper":
        print("WINNER WINNER!!!!")
        userScore += 1

    else:
        print("LOSERRRRRRRRRRR!")
        computerScore += 1

print("You won", userScore, " times.") 
print("Computer won", computerScore, " times.") 
print("Doei!")