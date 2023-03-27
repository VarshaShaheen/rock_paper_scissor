from random import randint

choice = ["stone", "paper", "scissor"]
max_score = 5
user_score = 0
comp_score = 0

while user_score != max_score and comp_score != max_score:
    computer = randint(0, 2)
    print("Enter the choice 0 for rock 1 for paper and 2 for scissor:")
    user = int(input())
    print(choice[computer])
    if user == (computer + 1) % 3:
        user_score = user_score + 1
    else:
        comp_score = comp_score + 1

if user_score == max_score:
    print("Congratulations you won!")
else:
    print("Computer won!")
