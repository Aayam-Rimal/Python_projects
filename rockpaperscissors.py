# game of rock paper scissors using random module
import random
import os
import json

FILENAME="scores.json"

if os.path.exists(FILENAME):
      with open(FILENAME,'r') as f:
            data=json.load(f)
else:
      data={"you":0, "computer":0}


options=['rock','paper','scissors']

you=data['you']
computer=data['computer']

while True:
    try:
        for i in range(1,6):
        
            user_choice=input("enter your choice rock/paper/scissors: ")
            if user_choice in options:
                computer_choice= random.choice(options)
                print(computer_choice)
            

                if (user_choice=='rock' and computer_choice=='paper') or ( user_choice=='paper' and computer_choice=='scissors') or (user_choice=='scissors' and computer_choice=='rock'):
                    print("computer wins!")
                    computer+=1
                elif user_choice==computer_choice:
                    print("draw!")
                else:
                    print("you win!!")
                    you+=1
            else:
                  print("sorry invalid input!!")
        with open(FILENAME, 'w') as f:
              json.dump({"you":you, "computer":computer},f, indent=4)


        if computer>you:
                print("computer won with score:",computer)
        elif you>computer:
                print("you won with score:", you)
        else:
                print("draw")
        print(f"you:{you}, computer={computer}")

        choice=input("do you want to continue?(y/n): ")
        if choice=='y':
                continue
        elif choice=='n':
                break
    except ValueError:
        print("invalid input!! try again: ")
        continue        




                