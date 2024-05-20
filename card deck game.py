# -*- coding: utf-8 -*-
"""
Module to handle the functionality needed to play a game of cards with a standard deck.

@author:Sackitey Joseph
"""


#Define constant variables
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
card_values = (2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace")


#Define functions

def build_deck():
    """
    Create the deck of cards based on the suits and values    

    Returns
    -------
    deck : list
        list containing the initial cards


    """
    deck = []

    for suit in suits:
        for value in card_values:
            card = [suit, value]
            deck.append(card)

    return deck


def get_card_rank(card):
    """
    Return the integer rank of the card    

    Parameters
    ----------
    card : list
        list containing the suit / value of the card

    Returns
    -------
    rank : numeric representation of the card

    """
    rank = 0
    value = card[1]
    
    if value in range(2, 11):
        rank = int(value)
    elif value in ["Jack", "Queen", "King"]:
        rank = 10
    elif value == "Ace":
        rank = 11        
    
    return rank

def print_deck(deck):
    """
    Test method to print out all cards in the deck   

    Parameters
    ----------
    deck : list
        list of cards to print

    Returns
    -------
    None.

    """
    for card in deck:
        print(f"{card[1]} of {card[0]} - rank: {get_card_rank(card)}")


def shuffle_deck(deck):
    """
    Shuffle the deck of cards using the random module

    Parameters
    ----------
    deck : list
        the list of cards to randomize

    Returns
    -------
    deck : list
        the randomzied list of cards


    """
    return deck

#
def deal(deck, number_of_players = 2, number_of_cards = 2):
    """
    Deal the cards from the deck based on the number of players and the number of cards in the hand   

    Parameters
    ----------
    deck : the list of cards to deal from
    number_of_players : int, optional
        Number of hands of cards to deal. The default is 2.
    number_of_cards : int, optional
        The number of cards to deal to each player. The default is 2.

    Returns
    -------
    player_hands : int
        List of players and the cards in each hand

    """
    player_hands = []
    
    return player_hands

