import random

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissors"]

while user_wins < 3 and computer_wins < 3:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q" or user_input == "quit":
        break
    elif user_input not in options:
        continue
    random_num = random.randint(0,2)
    computer_pick = options[random_num]
    print(f"you picked: {user_input}, while computer picked: {computer_pick}") 
    if user_input == "rock" and computer_pick == "scissors":
        print("You Won..!!")
        user_wins += 1
        print(f"score is: {user_wins}, while your  opponent has: {computer_wins}")
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won..!!")
        user_wins += 1
        print(f"score is: {user_wins}, while your  opponent has: {computer_wins}")
    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won..!!")
        user_wins += 1
        print(f"score is: {user_wins}, while your  opponent has: {computer_wins}")
    elif user_input == computer_pick:
        print("It is a Tie")
        print(f"score is: {user_wins}, while your  opponent has: {computer_wins}")
    else:
        print("You Lost")
        computer_wins += 1
        print(f"score is: {user_wins}, while your  opponent has: {computer_wins}")
        continue

print(f"The Final score is: {user_wins}, while your  opponent has: {computer_wins}")
print("Goodbye")