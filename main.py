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
            suit_of_cards[i-1].set_value(10)
        if suit_of_cards[i-1].get_value() == 12:
            suit_of_cards[i-1].set_face_value("Queen")
            suit_of_cards[i-1].set_value(10)
        if suit_of_cards[i-1].get_value() == 13:
            suit_of_cards[i-1].set_face_value("King")
            suit_of_cards[i-1].set_value(10)
    for card in suit_of_cards:
        deck_of_cards.append(card)

# Deals a set of cards to the player
def deal_cards(player):
    for card in range(2):
        player.player_hand += [deck_of_cards[random.randint(0, len(deck_of_cards) -1)]]
        deck_of_cards.remove(player.player_hand[card])
    calculate_player_score(player)

# calculates a players score
def calculate_player_score(player):
    player.player_score = 0
    for card in player.player_hand:
        player.player_score += card.value

# Deals a card to the dealer
def dealers_cards():
    dealers_hand = [deck_of_cards[random.randint(0, len(deck_of_cards) -1)]]
    deck_of_cards.remove(dealers_hand[0])
    return dealers_hand

# Determins the dealers score
def calculate_dealers_score():
    dealers_score = 0
    for card in dealers_hand:
        dealers_score += card.get_value()
    return dealers_score

# Checks the players score to see if it equals 21
def check_blackjack(player):
    if player.player_score == 21:
        return "BLACKJACK"

# Loop to control the players decision to hit or stand
def player_turn(player):
    while player.player_score < 21:
        decision = input("What would you like to do? \'hit\' or \'stand\'\n")
        if decision == "hit":
            player.player_hand += [deck_of_cards[random.randint(0, len(deck_of_cards) -1)]]
            deck_of_cards.remove(player.player_hand[-1])
            calculate_player_score(player)
            print("\n" + player_one.name + ", " + str(player_one))
            continue
        elif decision == "stand":
            calculate_player_score(player)
            print("\n" + player_one.name + ", " + str(player_one))
            dealers_turn(player)
            break
    if player.player_score == 21:
        print("blackjack")
        dealers_turn(player)
    if player.player_score > 21:
        print("BUST")

# Loop control to control dealers turn
def dealers_turn(player):
    while calculate_dealers_score() <= player.player_score and calculate_dealers_score() < 17:
        new_card = deck_of_cards[random.randint(0, len(deck_of_cards) -1)]
        dealers_hand.append(new_card)
    if calculate_dealers_score() == player.player_score and calculate_dealers_score() >= 17:
        print_dealers_hand()
        print("Its a tie")
    elif calculate_dealers_score() > player.player_score and calculate_dealers_score() <= 21:
        print_dealers_hand()
        print("Dealers Wins")
    elif calculate_dealers_score() > 21:
        print_dealers_hand()
        print("Dealers goes bust, Player wins")
    else:
        print(calculate_dealers_score())

def print_dealers_hand():
    print("The dealers hand consists of the " + str(dealers_hand).strip("[]") + " for a total of: " + str(calculate_dealers_score()))

# Beginning of the game
print("Let's play some BlackJack\n")
print("""Rules: You play against the dealer to try and create a hand with a value as close to 21 as possible without going over (bust).

commands to use during play:
hit: Take another card
stand: End your turn\n""")

# Create a single deck of 52 playing cards
create_deck()

# Ask the player their name and store the Player object as player_one
player_one = Player.Player(input("What is your name\n"))

# Deals a card to the dealer and a set of 2 cards to the player
dealers_hand = dealers_cards()
deal_cards(player_one)

# Output players hand and dealers hand
print("\n" + player_one.name + ", " + str(player_one))
print("The dealers hand consists of the " + str(dealers_hand[0]) + " for a total of: " + str(calculate_dealers_score()))

# Check to see it the player has blackjack
check_blackjack(player_one)

# The player takes their turn and decides to hit or stand
player_turn(player_one)