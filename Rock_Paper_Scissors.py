import random
Scissors=(''' __      __
( _\    /_ )
 \ _\  /_ / 
  \ _\/_ /_ _
  |_____/_/ /|
  (  (_)__)J-)
  (  /`.,   /
   \/  ;   /
    | === |''')
Rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
Paper=("""
      _.-._
      | | | |_
      | | | | |
      | | | | |
    _ |     ` |
    \`\       |
     \        |
      \      /
       |    |
       |    |
""")
game_images =[Rock, Paper , Scissors]

player1 = int(input("What do you choose?Type 0 for Rock , 1 for Paper or 2 for Scissors.\n"))
print(game_images[player1])

computer_choice = random.randint(0,2)
print(f"Computer chose {computer_choice}")
print(game_images[computer_choice])

if(player1 == 0 and computer_choice ==2):
    print("You Win!")
elif(computer_choice > player1):
    print("Computer Wins!")
elif(computer_choice==player1):
    print("Tie!")
else:
    print("You typed an invalid number, you lose!")
