# rock, paper, scissor

import random
import sys
from enum import Enum

# this is how we define enum
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# print(RPS(1))
# print(RPS(1).name)
# print(RPS.ROCK.name)
# print(RPS.ROCK.value)

print("GAME".center(25, "="))

player_choice = input("Enter ... \n1. Rock 🪨\n2. Paper 📄\n3. Scissors ✂️\n\n")
player = int(player_choice)

if player < 1 or player > 3:
    sys.exit("Choose between 1 and 3")

computer_choice = random.choice(["1", "2", "3"])
computer = int(computer_choice)

print("You chose " + str(RPS(player).name) + " and Computer chose " + str(RPS(computer).name))

if player == computer:
    print("😳 Tie!")
elif player == 1 and computer == 3:
    print("🎉 You won!")
elif player == 2 and computer == 1:
    print("🎉 You won!")
elif player == 3 and computer == 2:
    print("🎉 You won!")
else:
    print("😭 Computer won!")
