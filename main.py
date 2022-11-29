from random import randint

choice = ["rock", "paper", "scissor"]

print("The one scoring 5 points first will won")

player_point = comp_point = 0

while (comp_point < 5) or (player_point < 5):
    player_choice = input("\nEnter your choice: rock , paper or scissor")
    computer = choice[randint(0, 2)]
    if player_choice not in choice:
        print("Invalid input")
        continue
    elif computer == player_choice:
        print("\nTie")
    elif computer == "rock":
        if player_choice == "scissor":
            print("\ncomputer scored a point")
            comp_point = comp_point + 1
        else:
            print("\nyou scored a point")
            player_point = player_point + 1
    elif computer == "paper":
        if player_choice == "rock":
            print("\ncomputer scored a point")
            comp_point = comp_point + 1
        else:
            print("\nyou scored a point")
            player_point = player_point + 1
    else:
        if player_choice == "paper":
            print("\ncomputer scored a point")
            comp_point = comp_point + 1
        else:
            print("\nyou scored a point")
            player_point = player_point + 1

if player_point == 5:
    print("Congratulations you won!")

else:
    print("Oops computer won!")
