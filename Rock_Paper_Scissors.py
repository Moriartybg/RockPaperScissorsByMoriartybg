import random
rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_score = 0
computer_score = 0
draw = 0

for _ in range(10):

    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid Input. Try again...")

    computer_move = random.randint(1, 3)

    if computer_move == 1:
        computer_move = rock

    elif computer_move == 2:
        computer_move = paper

    else:
        computer_move = scissors

    print(f"The computer chose {computer_move}.")

    if player_move == rock and computer_move == scissors or \
        player_move == scissors and computer_move == paper or \
        player_move == paper and computer_move == rock:
        print("You win!")
        player_score += 1
    elif player_move == computer_move:
        print(f"Draw!")
        draw += 1
    else:
        print("You lose!")
        computer_score += 1
print()
print()

if player_score > computer_score:
    print("YOU ARE THE WINNER!!!")

elif player_score == computer_score:
    print("NO WINNER THIS TIME!")

else:
    print("YOU ARE LOSE!")


print()
print()
print(f"Yur score is:{player_score}")
print(f"Computer score is:{computer_score}")
print(f"Draw:{draw}")
