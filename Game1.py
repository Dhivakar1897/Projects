print("Play... Rock! Paper!! Scissor!!!\n")
import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK=1
    PAPER=2
    SCISSORS=3

player=int(input("Enter...\n"
                 "1 for Rock.\n"
                 "2 for Paper.\n"
                 "3 for Scissors.\n:"))
if player<1 or player>3:
    sys.exit("You must enter 1,2 or 3.")

computer=int(random.choice("123"))
print("\nYour choice",str(RPS(player)).replace("RPS.","")+".")
print("Python choice",str(RPS(computer)).replace("RPS.","")+".\n")
if player==1 and computer==3:
    print("🎉✨ You win!")
elif player==2 and computer==1:
    print("🎉✨ You win!")
elif player ==3 and computer ==2:
    print("🎉✨ You win!")
elif player ==computer:
    print("😮Tie Game!")
else:
    print("🎉✨ Python win!")