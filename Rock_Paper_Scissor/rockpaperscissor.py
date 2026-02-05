# HERE WE ARE GOING TO CRATE THE GAME ROCK PAPER SCISSOR
import random

select=["rock","paper","scissor"]
computer= random.choice(select)
user_input=input("enter your choise: ").lower().strip()
print("computer selection is :",computer)
if user_input=="rock" and computer=="scissor":
    print("you wins")
elif user_input=="scissor" and computer=="rock":
    print("computer wins")
elif user_input=="paper" and computer=="rock":
    print("you wins")
elif user_input=="scissor" and computer=="paper":
    print("you wins ")
elif user_input=="paper" and computer=="scissor":
    print("computer wins")
elif user_input=="rock" and computer=="paper":
    print("computer wins")
elif user_input==computer:
    print("match draw")
else:
    print("enter in between rock,paper,scissor")
