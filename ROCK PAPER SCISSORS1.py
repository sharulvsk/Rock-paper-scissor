import random
options = ("rock","paper","scissors")
running = True
while running:
   player = None
   computer = random.choice(options)
   while player not in options:
      player = input("Enter a choice(rock,paper,scissors):") 
   print(f"player:{player}")
   print(f"computer:{computer}")
   if player==computer:
      print("It's a tie!")
   elif player=="rock" and computer=="scissors":
      print("You win<3")
   elif player=="paper" and computer=="rock":
      print("You win<3")
   elif player=="scissors" and computer=="paper":
      print("You win<3")
   else:
      print("You lose!")  
   if not input("play again?(y/n):").lower()=="y":
      running = False
print("Thanks for playing<3")