name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to and end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ").lower()

    if answer == "swim":
        print("You swam across and were eaten by a shark")
    elif answer == "walk":
        print()
    else:
        print("Invalid choice. You lose!")

elif answer == "right":
    print()

else:
    print("Invalid choice. You lose!")