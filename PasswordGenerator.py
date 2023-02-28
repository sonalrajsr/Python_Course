import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
no_letters= int(input("How many letters would you like in your password?\n")) 
no_symbols = int(input(f"How many symbols would you like?\n"))
no_numbers = int(input(f"How many numbers would you like?\n"))

# random_letter=random.randint(0,25)
# random_numbers=random.randint(0,len(numbers)-1)
# random_symbols=random.randint(0,len(symbols)-1)
letter_pass=[]

for i in range(0,no_letters):
    random_letter=random.randint(0,25)
    letter_pass.append(letters[random_letter])

for i in range(0,no_symbols):
    random_symbols=random.randint(0,len(symbols)-1)
    letter_pass.append(symbols[random_symbols])

for i in range(0,no_numbers):
    random_numbers=random.randint(0,len(numbers)-1)
    letter_pass.append(numbers[random_numbers])
#print(letter_pass)
random.shuffle(letter_pass)
#print(letter_pass)

password=""
for i in range(0,len(letter_pass)):
    password=password+letter_pass[i]

print(password)

