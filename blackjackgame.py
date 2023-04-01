logo = """
                                                                                                                       
                                                                           ,---._                                      
    ,---,.    ,--,                                   ,-.                 .-- -.' \                                ,-.  
  ,'  .'  \ ,--.'|                               ,--/ /|                 |    |   :                           ,--/ /|  
,---.' .' | |  | :                             ,--. :/ |                 :    ;   |                         ,--. :/ |  
|   |  |: | :  : '                             :  : ' /                  :        |                         :  : ' /   
:   :  :  / |  ' |       ,--.--.       ,---.   |  '  /                   |    :   :   ,--.--.       ,---.   |  '  /    
:   |    ;  '  | |      /       \     /     \  '  |  :                   :           /       \     /     \  '  |  :    
|   :     \ |  | :     .--.  .-. |   /    / '  |  |   \                  |    ;   | .--.  .-. |   /    / '  |  |   \   
|   |   . | '  : |__    \__\/: . .  .    ' /   '  : |. \             ___ l           \__\/: . .  .    ' /   '  : |. \  
'   :  '; | |  | '.'|   ," .--.; |  '   ; :__  |  | ' \ \          /    /\    J   :  ," .--.; |  '   ; :__  |  | ' \ \ 
|   |  | ;  ;  :    ;  /  /  ,.  |  '   | '.'| '  : |--'          /  ../  `..-    , /  /  ,.  |  '   | '.'| '  : |--'  
|   :   /   |  ,   /  ;  :   .'   \ |   :    : ;  |,'             \    \         ; ;  :   .'   \ |   :    : ;  |,'     
|   | ,'     ---`-'   |  ,     .-./  \   \  /  '--'                \    \      ,'  |  ,     .-./  \   \  /  '--'       
`----'                 `--`---'       `----'                        "---....--'     `--`---'       `----'              
                                                                                                                       
"""
import random
import os




cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

human_cards = []  # variable that will store the list of selected cards form the user.
computer_cards = []  # variable that wll store the list of selected cards form the computer.


def human_card_selection():  # function that will pick a card human
    if cards[random.randint(0, len(cards) - 1)] == 11:
        option_card = int(input("Which value of Ace card you want to use 1 or 11 : "))
        human_cards.append(option_card)
    else:
        human_cards.append(cards[random.randint(0, len(cards) - 1)])


def computer_card_selection():  # fuction that will pick the card for computer
    computer_cards.append(cards[random.randint(0, len(cards) - 1)])


def computer_run():  # function that will run until the sum of card is <17 for computer cards.
    while sum(computer_cards) < 17:
        computer_card_selection()

def card_number_printer():      #This function will print the current values of card and theier sum.
    print(f" Your cards: {human_cards}, current score: {sum(human_cards)}")
    print(f" Computer cards: {computer_cards}, current score: {sum(computer_cards)}")

def blackjack_decision_maker():     #This functio will print the final winner
    if (sum(human_cards) < sum(computer_cards)) and (sum(human_cards) <= 21) and (sum(computer_cards) <= 21):
        #card_number_printer()
        print("Computer Wins")
    elif (sum(human_cards) > sum(computer_cards)) and (sum(human_cards) <= 21) and (sum(computer_cards) <= 21):
        #card_number_printer()
        print("You won")
    elif sum(human_cards) > 21 > sum(computer_cards):
        #card_number_printer()
        print("Computer Wins")
    elif sum(computer_cards) > 21 > sum(human_cards):
        #card_number_printer()
        print("You Wins")
    elif sum(computer_cards) == sum(human_cards):
        #card_number_printer()
        print("Tie")
user_choice1_to_play = input("Do you want to play: Type \'y\' to play and \'n\' to exit. ").lower()

if user_choice1_to_play == 'y':
    os.system('cls')
    print(logo)
    human_card_selection()
    human_card_selection()
    computer_card_selection()
    card_number_printer()

    play_continue = True

    while play_continue:
        user_choice2_to_play = input("Do you want to take new card: Type \'y\' to play and \'n\' to pass to computer. ").lower()
        if user_choice2_to_play == 'y':
            human_card_selection()
            if sum(human_cards) > 21:
                play_continue = False
        elif user_choice2_to_play == 'n':
            computer_run()
            play_continue = False
        card_number_printer()

else:
    print("You don\'t opted to play.")

blackjack_decision_maker()
