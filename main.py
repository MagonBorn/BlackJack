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
        if suit_of_cards[i-1].get_value() == 1:
            suit_of_cards[i-1].set_face_value("Ace")
            suit_of_cards[i-1].set_high_value(11)
        if suit_of_cards[i-1].get_value() == 11:
            suit_of_cards[i-1].set_face_value("Jack")
        if suit_of_cards[i-1].get_value() == 12:
            suit_of_cards[i-1].set_face_value("Queen")
        if suit_of_cards[i-1].get_value() == 13:
            suit_of_cards[i-1].set_face_value("King")
    for card in suit_of_cards:
        deck_of_cards.append(card)

# Deals a set of cards to the player
def deal_cards(player):
    for card in range(2):
        player.player_hand += [deck_of_cards[random.randint(0, len(deck_of_cards) -1)]]
        deck_of_cards.remove(player.player_hand[card])
    for card in player.player_hand:
        player.player_score += card.value

def dealers_cards():
    dealers_hand = [deck_of_cards[random.randint(0, len(deck_of_cards) -1)]]
    deck_of_cards.remove(dealers_hand[0])
    return dealers_hand

# Beginning of the game
print("Let's play some BlackJack\n")
print("Rules: You play against the dealer to try and create a hand with a value as close to 21 as possible without going over (bust).")

# Create a single deck of 52 playing cards
create_deck()

# Ask the player their name and store the Player object as player_one
player_one = Player.Player(input("What is your name\n"))

# Deals a card to the dealer and a set of 2 cards to the player
dealers_hand = dealers_cards()
deal_cards(player_one)

# Output players hand and dealers hand
print("\n" + player_one.name + ", " + str(player_one))
print("The dealers hand consists of the " + str(dealers_hand[0]))