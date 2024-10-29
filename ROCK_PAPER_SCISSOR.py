import random
random_number= random.randint(0,2)
print("<-----------WELCOME TO ROCK, PAPER and SCISSOR GAME---------->")
player=int(input("Choose a number betweer 0-3 where\n 0 = ROCK\n 1 = PAPER\n 2 = SCISSOR\n"))


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


list=[rock,paper,scissors]


if random_number==0 and player==0:
    print(list[player])
    print(list[random_number])
    print("BOTH COMPUTER AND YOU CHOOSES ROCK :")
    print("---DRAW---")


elif random_number==1 and player==1:
    print(list[player])
    print(list[random_number])
    print("BOTH COMPUTER AND YOU CHOOSES PAPER :")
    print("---DRAW---")
    
    
elif random_number==2 and player==2:
    print(list[player])
    print(list[random_number])
    print("BOTH COMPUTER AND YOU CHOOSES SCISSOR :")
    print("---DRAW---")
    
    
elif random_number==1 and player==0:
    print(list[player])
    print(list[random_number])
    print("YOU CHOOSES ROCK ------AND---- COMPUTER CHOOSES PAPER  :")
    print("---YOU LOOSE---")    
    
    
elif random_number==0 and player==1:
    print(list[player])
    print(list[random_number])
    print("YOU CHOOSES PAPER ------AND---- COMPUTER CHOOSES ROCK  :")
    print("---YOU WIN---")    
    
    
elif random_number==2 and player==0:
    print(list[player])
    print(list[random_number])
    print("YOU CHOOSES ROCK ------AND---- COMPUTER CHOOSES SCISSOR  :")
    print("---YOU WIN---")    
    
    
elif random_number==0 and player==2:
    print(list[player])
    print(list[random_number])
    print("YOU CHOOSES SCISSOR ------AND---- COMPUTER CHOOSES ROCK  :")
    print("---YOU LOOSE---")    
    
                    
elif random_number==2 and player==1:
    print(list[player])
    print(list[random_number])
    print("YOU CHOOSES PAPER ------AND---- COMPUTER CHOOSES SCISSOR  :")
    print("---YOU LOOSE---")    
    
    
elif random_number==1 and player==2:
    print(list[player])
    print(list[random_number])
    print("YOU CHOOSES SCISSOR ------AND---- COMPUTER CHOOSES PAPER  :")
    print("---YOU WIN---")    
    
    
else:
    print("YOU ARE CHOOSING AN INVALID NUMBER")    
    
    
