import random

money = 100

# function for Card Draw game. 
def card_draw(bet):
    #makes list for a deck of cards.
    hearts = list(range(1,14))
    diamonds = list(range(1,14))
    spades = list(range(1,14))
    clubs = list(range(1,14))
    deck = hearts + diamonds + spades + clubs
    #choses card for player and house.
    player = random.choice(deck)
    house = random.choice(deck)
    #tells the user what happened and returns bet win/loss.
    if player == house:
        print("You bet $" + str(bet) + " on a game of Card Draw. You drew a " + str(player) + " and the house drew a " + str(house) + ". You tied the house! You still have $" + str(money) + ".")
        return 0
    if player > house:
        print("You bet $" + str(bet) + " on a game of Card Draw. You drew a " + str(player) + " and the house drew a " + str(house) + ". You beat the house! You now have $" + str(money+bet) + ".")
        return bet
    if player < house:
        print("You bet $" + str(bet) + " on a game of Card Draw. You drew a " + str(player) + " and the house drew a " + str(house) + ". You lost to the house! You now have $" + str(money-bet) + ".")
        return -bet


money += card_draw(10)
money += card_draw(10)
money += card_draw(10)
money += card_draw(10)
money += card_draw(10)
money += card_draw(10)
money += card_draw(10)
money += card_draw(10)
money += card_draw(10)
money += card_draw(10)
money += card_draw(10)
money += card_draw(10)
money += card_draw(10)
money += card_draw(10)
money += card_draw(10)
money += card_draw(10)
money += card_draw(10)
money += card_draw(10)
money += card_draw(10)
money += card_draw(10)
money += card_draw(10)
money += card_draw(10)
money += card_draw(10)
money += card_draw(10)
money += card_draw(10)
money += card_draw(10)
money += card_draw(10)
