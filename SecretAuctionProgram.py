logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

def bid_user():
    name=str(input("Enter Your name: "))
    value=int(input("Enter the bid value: $"))
    user_data[name]=value
    

user_data={}

loop = True

bid_user()

while loop:
    value=input("Is ther any one who will bid: (Type \"Yes\" or \"No\")").lower()
    if value=="yes":
        print("\033c", end='')
        name=str(input("Enter Your name: "))
        value=int(input("Enter the bid value: $"))
        user_data[name]=value
        #print("\033c", end='')
    
    else:
        loop=False
print("The entries are ",user_data)

highest_bid=0
winner=""
for amout in user_data:
    if user_data[amout]>highest_bid:
        highest_bid=user_data[amout]
        winner=amout
print(f"The winner is {winner} with the highest bid of ${highest_bid}")

# max_bid=max(bid_amount)
# print(max_bid)

