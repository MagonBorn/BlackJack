import Cards
import Player
import random

# initialise variables
deck_of_cards = []

# Method to create a single deck of 52 cards
def create_deck():
    create_suit("Spades")
    create_suit("Hearts")
    create_suit("Clubs")
    create_suit("Diamonds")

# Helper method to create each individual suit of cards
def create_suit(suit):
    suit_of_cards = []
    for i in range(1, 14):
        suit_of_cards.append(Cards.Card(i, suit))
        if suit_of_cards[i-1].get_number() == 1:
            suit_of_cards[i-1].set_face_value("Ace")
        if suit_of_cards[i-1].get_number() == 11:
            suit_of_cards[i-1].set_face_value("Jack")
        if suit_of_cards[i-1].get_number() == 12:
            suit_of_cards[i-1].set_face_value("Queen")
        if suit_of_cards[i-1].get_number() == 13:
            suit_of_cards[i-1].set_face_value("King")
    for card in suit_of_cards:
        deck_of_cards.append(card)

# Deals a set of cards to the player
def deal_cards(player):
    for card in range(2):
        player.player_hand += [deck_of_cards[random.randint(0, len(deck_of_cards) -1)]]
        deck_of_cards.remove(player.player_hand[card])
    for card in player.player_hand:
        player.player_score += card.number

# Beginning of the game
print("Let's play some BlackJack")

# Create a single deck of 52 playing cards
create_deck()

# Ask the player their name and store the Player object as player_one
player_one = Player.Player(input("What is your name\n"))

# Deal a set of 2 cards to player one
deal_cards(player_one)

print(player_one)