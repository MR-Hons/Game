#Roulette Game
#Made by Matthew R. Hons

import random

money = 100

#test of Roulette.
def roulette(choice, bet):
    #the wheel as a list.
    wheel = ["0", '28', '9', '26', '30', '11', '7', '20', '32', '17', '5', '22', '34', '15', '3', '24', '36', '13', '1', '00', '27', '10', '25', '29', '12', '8', '19', '31', '18', '6', '21', '33', '16', '4', '23', '35', '14', '2']
    #the role of the ball via random choice. 
    role = random.choice(wheel)
    #function to show color of the number on the wheel. 
    def color(num):
        if num == "0" or num == "00":
            return"Green"
        num = int(num)
        if num in range(1,11) or num in range(19,29):
            if num % 2 == 0:
                return "Black"
            if num % 2 != 0:
                return "Red"
        if num in range(11,19) or num in range(29,37):
            if num % 2 == 0:
                return "Red"
            if num % 2 != 0:
                return "Black"
    #"Odd/Even" = bet o/e. pays 1:1
    if choice == "Odd" or choice == "Even":
        if choice == "Odd":
            if int(role) % 2 != 0:
                print("You bet $" + str(bet) + " on " + str(choice) + " at the Roulette wheel. The ball landed on " + str(role) + " " + str(color(role)) + \
                ". You won! You now have $" + str(money+bet))
                return bet
            if int(role) % 2 == 0:
                print("You bet $" + str(bet) + " on " + str(choice) + " at the Roulette wheel. The ball landed on " + str(role) + " " + str(color(role)) + \
                ". You lost! You now have $" + str(money-bet))
                return -bet
        if choice == "Even":
            if int(role) % 2 == 0:
                print("You bet $" + str(bet) + " on " + str(choice) + " at the Roulette wheel. The ball landed on " + str(role) + " " + str(color(role)) + \
                ". You won! You now have $" + str(money+bet))
                return bet
            if int(role) % 2 != 0:
                print("You bet $" + str(bet) + " on " + str(choice) + " at the Roulette wheel. The ball landed on " + str(role) + " " + str(color(role)) + \
                ". You lost! You now have $" + str(money-bet))
                return -bet
    #"Red/Black" = lands red or black. pays 1:1
    if choice == "Red" or choice == "Black":
        if choice == "Red":
            if color(role) == "Red":
                print("You bet $" + str(bet) + " on " + str(choice) + " at the Roulette wheel. The ball landed on " + str(role) + " " + str(color(role)) + \
                    ". You won! You now have $" + str(money+bet))
                return bet
            if color(role) == "Black" or color(role) == "Green":
                print("You bet $" + str(bet) + " on " + str(choice) + " at the Roulette wheel. The ball landed on " + str(role) + " " + str(color(role)) + \
                    ". You lost! You now have $" + str(money-bet))
                return -bet 
        if choice == "Black":
            if color(role) == "Black":
                print("You bet $" + str(bet) + " on " + str(choice) + " at the Roulette wheel. The ball landed on " + str(role) + " " + str(color(role)) + \
                    ". You won! You now have $" + str(money+bet))
                return bet
            if color(role) == "Red" or color(role) == "Green":
                print("You bet $" + str(bet) + " on " + str(choice) + " at the Roulette wheel. The ball landed on " + str(role) + " " + str(color(role)) + \
                    ". You lost! You now have $" + str(money-bet))
                return -bet
    #"strait up" = any single muber on the board. pays 35:1
    if choice in wheel:
        if choice == role:
            print("You bet $" + str(bet) + " on " + str(choice) + " at the Roulette wheel. The ball landed on " + str(role) + " " + str(color(role)) + \
                ". You won! You now have $" + str(money+(35*bet)))
            return bet*35
        if choice != role:
            print("You bet $" + str(bet) + " on " + str(choice) + " at the Roulette wheel. The ball landed on " + str(role) + " " + str(color(role)) + \
                ". You lost! You now have $" + str(money-bet))
            return -bet
    #"row" = 0,00. pays 17:1
    if choice == "Row":
        if role == "0" or role == "00":
            print("You bet $" + str(bet) + " on " + str(choice) + " at the Roulette wheel. The ball landed on " + str(role) + " " + str(color(role)) + \
                ". You won! You now have $" + str(money+(17*bet)))
            return bet*17
        else:
            print("You bet $" + str(bet) + " on " + str(choice) + " at the Roulette wheel. The ball landed on " + str(role) + " " + str(color(role)) + \
                ". You lost! You now have $" + str(money-bet))
            return -bet
    else:
        print("Your bet is not supported.")
        return 0
    

#Call test functions here.
money += roulette("Row", 10)
money += roulette("Row", 10)
money += roulette("Row", 10)
money += roulette("Row", 10)
money += roulette("Row", 10)
money += roulette("Row", 10)
money += roulette("Row", 10)
money += roulette("Row", 10)
money += roulette("Row", 10)
money += roulette("Row", 10)
money += roulette("Row", 10)
money += roulette("Row", 10)
money += roulette("Row", 10)
money += roulette("Row", 10)
money += roulette("Row", 10)
money += roulette("Row", 10)
money += roulette("Row", 10)
money += roulette("Row", 10)
money += roulette("Row", 10)
money += roulette("Row", 10)
money += roulette("Row", 10)
money += roulette("Row", 10)
money += roulette("Row", 10)
money += roulette("Row", 10)
money += roulette("Row", 10)
money += roulette("Row", 10)

