import Cards
import random

deck_of_cards = []

# Method to create a single deck of cards
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
    deck_of_cards.append(suit_of_cards)


create_deck()

index1 = random.randint(0, len(deck_of_cards)-1)
index2 = random.randint(0, len(deck_of_cards[0])-1)
print(deck_of_cards[index1][index2])