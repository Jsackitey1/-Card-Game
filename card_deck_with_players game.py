# -*- coding: utf-8 -*-
"""
Use lists and loops to build functionality for a deck of cards.

@author: Sackitey Joseph
"""
import random

#use a tuple to create a fixed list of values for the suits and values
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
card_values = (2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A")

#create the deck list variable
#deck = [0] * (len(suits) * len(card_values))
deck = [] 


print("Build the deck of cards")
#fill the deck with a card of each suit
#i = 0
for suit in suits:
    for value in card_values:
        card = f"{value} of {suit}"
        deck.append(card)
        #deck[i] = card
        #i+=1

#print the initial deck of cards
#for card in deck:
#    print(card)

print()
print("...Shuffling...")
print()

#shuffle the deck of cards
random.shuffle(deck)

#add the position of the card in the deck for test
for i in range(len(deck)):
    deck[i] = f"{i} - {deck[i]}"

#print the shuffled deck
for card in deck:
    print(card)

#variables to set the number of players (hands) and number of cards in each hand
number_of_hands = 3
number_of_cards_per_hand = 5

#create an empty hand for each player
player_hands = [[] for i in range(number_of_hands)]

#below for loop does the same as the code in line 50
#for i in range(number_of_hands):
#    player_hands[i] = hand[]

#loop through the number of cards per hand and deal it to each player
#player 1 will get card 0, player 2 will get card 1, etc
for card_index in range(number_of_cards_per_hand):
    for hand in player_hands:
        hand.append(deck.pop(0))
    

#Deal all cards to player 1, then all cards to player 2, and so on
#for hand_index in range(number_of_hands):
#    hand = []
#    for card_index in range(number_of_cards_per_hand):
#        card = deck.pop(0)
#        hand.append(card)
#    player_hands.append(hand)
    
print()

for player in player_hands:
    for card in player:
        print(f"\t{card}")
    print()
    

    






               
               
