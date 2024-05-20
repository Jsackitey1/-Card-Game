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

#for card in deck:
#    print(card)

#deal out a hand of cards
hand = []
number_of_cards_per_hand = 5

for i in range(number_of_cards_per_hand):
    card = deck.pop(0)
    hand.append(card)

print(f"number of cards in hand: {len(hand)}")
print(f"number of cards left in deck: {len(deck)}")

print()
print("hand of cards:")
for card in hand:
    print(f"\t{card}")
    






               
               
