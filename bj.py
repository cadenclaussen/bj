import random

class Card: 

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.visibility = False

    def __str__(self):

        value2 = self.value
        if self.value == "J":
            value2 = "Jack"
        elif self.value == "Q":
            value2 = "Queen"
        elif self.value == "K":
            value2 = "King"
        elif self.value == "A":
            value2 = "Ace"


        suit2 = self.suit
        if self.suit == "S":
            suit2 = "Spades"
        elif self.suit == "C":
            suit2 = "Clubs"
        elif self.suit == "D":
            suit2 = "Diamonds"
        elif self.suit == "H":
            suit2 = "Hearts"
       
        return str(value2) + " of " + suit2 


class Deck:

    def __init__(self):
        self.cards = []
        for suit in [ "H", "D", "S", "C" ]:
            for value in [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K" ]:
                card = Card(value, suit)
                self.cards.append(card)
             
    def shuffle(self):
        shuffledCards = []
        for _ in range(52):
            card = random.choice(self.cards)
            self.cards.remove(card)
            shuffledCards.append(card)
        self.cards = shuffledCards

    def __str__(self):
        s = ""
        for card in self.cards:
            s2 = card.__str__()
            s = s + "\n" + s2
        return s


class Player:
    def __init__(self):
        pass
    def __str__(self):
        pass

class Dealer:
    def __init__(self):
        pass
    def __str__(self):
        pass


deck = Deck()
deck.shuffle()
print(deck)