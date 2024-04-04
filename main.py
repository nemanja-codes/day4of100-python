rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
list = [rock, paper, scissors]
import random

choice = input(
    "What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors. \n")

choice = int(choice)

if choice > 2 or choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(list[choice])
    print("\nComputer choice: \n")
    computer_choice = random.randint(0, 2)

    print(list[computer_choice])
    if choice == 0 and computer_choice == 2:
        print("You win!")
    elif choice == 2 and computer_choice == 0:
        print("You lose!")
    elif choice == computer_choice:
        print("It's a draw!")
    elif choice == 1 and computer_choice == 0:
        print("You win!")
    elif choice == 0 and computer_choice == 1:
        print("You lose!")
    elif choice == 2 and computer_choice == 1:
        print("You win!")
    elif choice == 1 and computer_choice == 2:
        print("You lose")
