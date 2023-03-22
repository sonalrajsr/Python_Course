def game(n):
    life = n
    for i in range(0, n+1):
        guess=int(input("Enter the guess number: "))
        if guess > number:
            print(f"High, {guess} is higher than the actual number:")
            life -= 1
        elif guess < number:
            print(f"Low, {guess} is lower than the actual number:")
            life -= 1
        elif number == guess:
            print("Congratulation you won, You guessed the correct number ", guess)
            break
        if life == 0:
            print("You live is over, You loose")
            print("The correct value is ", number)
        print("Your rest life is ", life)
        
import random

logo = '''  ________                                __  .__              _______               ___.                  
 /  _____/ __ __   ____   ______ ______ _/  |_|  |__   ____    \      \  __ __  _____\_ |__   ___________  
/   \  ___|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \ 
\    \_\  \  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ 
 \______  /____/  \___  >____  >____  >  |__| |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|    
        \/            \/     \/     \/             \/     \/          \/            \/    \/     \/         
        '''

number = random.randint(1, 100)
print(number)
print(logo)

level = input("Choose the level you want to play: Easy or Hard ").lower()

if level == "easy":
    game(10)
else:
    game(5)
