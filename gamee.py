import random

user_choice = input("Enter your choice (rock,paper,scissor): ")
possibility = ["rock", "paper", "scissor"]
computer_choice = random.choice(possibility)
print(f"\n your choice:{user_choice} computer choice:{computer_choice}\n")


if user_choice == computer_choice:
    print(f"both selected {user_choice},it's ties")
elif user_choice == "rock":
    if computer_choice  == "scissor":
        print(" rock smashes scissor! you win")
    else:
        print("paper cover rock ! you lose")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("paper cover rock! you win")
    else:
        print("scissor cut paper! you lose")
elif user_choice == "scissor":
    if computer_choice == "paper":
        print("scissor cut paper! you win")
    else:
        print("rock smashes scissor! you lose")
