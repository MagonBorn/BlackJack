class Card:
    def __init__(self, number, suit):
        self.suit = suit
        self.number = number
        self.face_value = ""
    
    def __repr__(self):
        if self.get_face_value() == "":
            return str(self.get_number()) + " of " + self.get_suit()
        else:
            return self.get_face_value() + " of " + self.get_suit()        

    def get_number(self):
        return self.number

    def get_suit(self):
        return self.suit

    def get_face_value(self):
        return self.face_value

    def set_face_value(self, face_value):
        self.face_value = face_value