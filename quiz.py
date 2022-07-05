print("Get ready to f*** your brain!")

playing = input("Will you give your precious time to this? ")
if playing.lower() != "yes":
    quit()

print("Let's give this shit a shot 😉")
score = 0

# Questions
answer = input("How many stripes are there on the US flag? ")
if answer == "13":
    print("Bravo!!!!!")
    score += 20
else:
    print("Incorrect! Better luck next time🙂")

answer = input("What's the capital of Canada? ")
if answer.lower() == "ottawa":
    print("Correct!!!")
    score += 20
else:
    print("Incorrect! Better luck next time🙂")

answer = input("What is the slang name for New York City, used by locals? ")
if answer.lower() == "gotham":
    print("Slayer!!!")
    score += 20
else:
    print("Incorrect! Better luck next time🙂")

answer = input("Who invented the iconic Little Black Dress?  ")
if answer.lower() == "coco chanel":
    print("We bow to you, King!!")
    score += 20
else:
    print("Incorrect! Better luck next time🙂")

answer = input("What city do The Beatles come from? ")
if answer.lower() == "liverpool":
    print("YOU ARE A G.O.A.T. !!😎")
    score += 20
else:
    print("Incorrect! Better luck next time🙂")



print("Score: " + str(score))
print("You got " + str(((score/20)/5) * 100) + "%")