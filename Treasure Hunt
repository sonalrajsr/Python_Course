print('''
     .--.   |V|
     /    \ _| /
     q .. p \ /
      \--/  //
     __||__//
    /.    _/
   // \  /
  //   ||
  \\  /  \
   )\|    |
  / || || |
  |/\| || |
     | || |
     \ || /
   __/ || \__
  \____/\____/


''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

path1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if path1 == "left":
  path2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if path2 == "wait":
    path3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if path3 == "red":
      print("It's a room full of fire. Game Over.")
    elif path3 == "yellow":
      print("You found the treasure! You Win!")
    elif path3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")
