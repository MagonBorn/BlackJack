class Player:
    def __init__(self, name):
        self.name = name
        self.player_hand = []
        self.player_score = 0
    
    def __repr__(self):
        return "your hand consists of the " + " ".join(str(card) + "," for card in self.player_hand) + " for a total of: " + str(self.get_score())

    def get_score(self):
        return self.player_score
    