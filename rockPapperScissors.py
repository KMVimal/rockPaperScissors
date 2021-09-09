import random

userWins = 0
computerWins = 0

options = ["rock", "paper", "scissors"]

while True:
    userInput = input("Type rock , paper, scissors or Q to quit: ").lower()

    if userInput == "q":
        break

    if userInput not in options:
        continue

    randomNumber = random.randint(0, 2)
    computerPick = options[randomNumber]
    print("Computer picked", computerPick + ".")

    if userInput == "rock" and computerPick == "scissors":
        userWins += 1
        print("You won!")
    elif userInput == "paper" and computerPick == "rock":
        userWins += 1
        print("You won!")
    elif userInput == "scissors" and computerPick == "paper":
        userWins += 1
        print("You won!")
    else:
        computerWins += 1
        print("Computer won")

print("You won ", userWins, "times.")
print("Computer won ", computerWins, "times.")
print("Thank you for playing!")
