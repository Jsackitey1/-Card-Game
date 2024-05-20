# Card Deck Management System

## Overview

This project is a Card Deck Management System developed in Python to facilitate the creation, shuffling, and dealing of a standard deck of cards. It serves as a practical tool for various card games and was created to enhance my coding skills and familiarize myself with the Python programming language.

## Features

### Deck Building
- **Build Deck**: Utilizes tuples to create a fixed list of suits and card values, then constructs the deck by combining each suit with each card value.

### Shuffling
- **Shuffle Deck**: Randomly shuffles the deck using the `random.shuffle` function to ensure a fair distribution of cards.

### Dealing
- **Deal Cards**: Distributes cards to players by creating empty hands for each player and dealing the specified number of cards in a round-robin fashion.

### Card Ranking
- **Get Card Rank**: Assigns a numeric rank to each card based on its value, which is essential for game logic involving comparisons.

### Interactive Output
- **Print Deck**: Provides a method to print all cards in the deck along with their ranks.
- **User Interaction**: Displays the deck before and after shuffling, and shows the hands dealt to each player.

## Project Structure

- **Main Program**: Initializes the deck, shuffles it, and deals cards to players.
- **Deck Functions**: Functions to build, shuffle, and print the deck.
- **Game Logic**: Functions to rank cards and deal them to players.

## How to Run

1. **Set Up Environment**: Ensure Python is installed on your system.
2. **Run the Program**: Execute the Python script to see the deck being built, shuffled, and dealt.
   ```
   python card_deck_management.py
   ```

## Example Usage

1. **Build Deck**: The program automatically builds a deck of cards combining suits and values.
2. **Shuffle Deck**: The deck is shuffled using the `random.shuffle` method.
3. **Deal Cards**: Cards are dealt to a specified number of players, with each player receiving a specified number of cards.
4. **Print Results**: The initial and shuffled deck are printed, followed by the hands dealt to each player.

## Conclusion

This Card Deck Management System is designed to provide a seamless experience for managing and handling card decks, making it suitable for various card games. The project was developed to improve my coding skills and to become proficient in the Python programming language.
