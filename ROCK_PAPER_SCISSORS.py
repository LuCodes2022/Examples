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


import random

options = [rock, paper, scissors]

player_number = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
player_choice = options[int(player_number)]
print(f"You chose: {player_choice}")
number_computer = random.randint(0, 2)
choice_computer = options[int(number_computer)]
print(f"The computer chose: {choice_computer}")


if player_number == "0":
  if number_computer == 0:
    print("It is a tie")
  elif number_computer == 1:
    print("You lose, the computer won..")
  else:
    print("You win!")
elif player_number == "1":
  if number_computer == 0:
    print("You win!")
  elif number_computer == 1:
    print("It is a tie!")
  else:
    print("You lose, the computer wins")
else:
  if number_computer == 0:
    print("You lose, the computer wins")
  elif number_computer == 1:
    print("You win!")
  else:
    print("It is a tie!")