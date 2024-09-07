import random
import sys
from enum import Enum
print("Play...Rock! Paper!! Scissors!!!")
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

while True:
    player = int(input("Enter...\n"
                       "1 for Rock.\n"
                       "2 for Paper.\n"
                       "3 for Scissors.\n:"))
    if player > 3 or player < 1:
        sys.exit("You must enter 1,2 or 3 only...")
    computer = int(random.choice("123"))
    print("\nYour choise is", str(RPS(player)).replace("RPS.", ""), ".\n"
          "Python choise is", str(RPS(computer)).replace("RPS.", ""), ".\n")
    if player == 1 and computer == 3:
        print("✨🎉✨You win!")
    elif player == 2 and computer == 1:
        print("✨🎉✨You win!")
    elif player == 2 and computer == 2:
        print("✨🎉✨You win!")
    elif player == computer:
        print("😮Tie Game!")
    else:
        print("✨🎉✨Python win!")
    playagain = input("\nDo you want to play again?\n"
                      "Y for Yes.\nQ for Quit.\nEnter...")
    if playagain.lower() == 'y':
        continue
    else:
        print('\n✨✨✨✨✨✨\n'
              'Thank you for playing!!!\n')
        break

sys.exit("Bye👋...")
