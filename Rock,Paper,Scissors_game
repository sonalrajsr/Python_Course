import random
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
Choose_user=int(input("What will you choose. Type 0 for Rock, 1 for Paper, 2 for Seasors"))

if Choose_user==0:
    print(rock)
    computer_choose=random.randint(0,2)
    if computer_choose==0:
        print(f"Computer choose {computer_choose}")
        print(rock)
        print("Match draw")
    elif computer_choose==1:
        print(f"Computer choose {computer_choose}")
        print(paper)
        print("You Lose")
    elif computer_choose:
        print(f"Computer choose {computer_choose}")
        print(scissors)
        print("You Win")
elif Choose_user==1:
    print(paper)
    computer_choose=random.randint(0,2)
    if computer_choose==0:
        print(f"Computer choose {computer_choose}")
        print(rock)
        print("You win")
    elif computer_choose==1:
        print(f"Computer choose {computer_choose}")
        print(paper)
        print("Match Draw")
    elif computer_choose:
        print(f"Computer choose {computer_choose}")
        print(scissors)
        print("You Lose")
elif Choose_user==2:
    print(scissors)
    computer_choose=random.randint(0,2)
    if computer_choose==0:
        print(f"Computer choose {computer_choose}")
        print(rock)
        print("you win")
    elif computer_choose==1:
        print(f"Computer choose {computer_choose}")
        print(paper)
        print("You Lose")
    elif computer_choose:
        print(f"Computer choose {computer_choose}")
        print(scissors)
        print("You Win")
else:
    print("Invalid Input")
