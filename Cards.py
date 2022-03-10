class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
        # High value is for ACE cards only.
        self.high_value = 0
        self.face_value = ""
    
    def __repr__(self):
        if self.get_face_value() == "":
            return str(self.get_value()) + " of " + self.get_suit()
        else:
            return self.get_face_value() + " of " + self.get_suit()        

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def get_face_value(self):
        return self.face_value

    def set_face_value(self, face_value):
        self.face_value = face_value

    def set_high_value(self, high_value):
        self.high_value = high_value