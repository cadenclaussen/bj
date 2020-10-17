import random

class Card: 

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.visibility = False

    def __str__(self):
        return self.suit + " " + str(self.value) + " " + str(self.visibility)


class Deck:

    def __init__(self):
        self.cards = []
        for suit in [ "hearts", "spades", "daimonds", "clubs" ]:
            for value in [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K" ]:
                card = Card(value, suit)
                self.cards.append(card)

    def shuffle(self ):
        pass

    def __str__(self):
        s = ""
        for card in self.cards:
            s2 = card.__str__()
            s = s + "\n" + s2
        return s


deck = Deck()
deck.shuffle()
print(deck)