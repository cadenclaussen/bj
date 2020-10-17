import random
from tkinter import *
from PIL import Image as PI
from PIL import ImageTk


class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.visibility = False
        image = PI.open("cards/" + value + suit + ".png")
        self.image = ImageTk.PhotoImage(image)

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
            for value in [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A" ]:
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


def main():
    root = Tk()
    root.title("Black Jack")
    root.geometry("760x760")

    window = LabelFrame(root, padx=1, pady=1, bg="grey")
    window.pack()

    header = LabelFrame(window, padx=10, pady=10)
    header.grid(row=0, column=0, columnspan=2, sticky=W+E)
    label = Label(header, text="Header Frame")
    label.pack()

    players = LabelFrame(window, padx=10, pady=10, width=30)
    players.grid(row=1, column=0, sticky=N+S)
    label = Label(players, text="Players Frame")
    label.pack()

    board = LabelFrame(window, padx=20, pady=20)
    board.grid(row=1, column=1)

    footer = LabelFrame(window, padx=20, pady=20)
    footer.grid(row=2, column=0, columnspan=2, sticky=W+E)
    label = Label(footer, text="Footer Frame")
    label.pack()

    deck = Deck()
    deck.shuffle()
    print(deck)


    # for row in range(19):
    #     for column in range(19):
    #         image = getImage(row, column)
    #         label = Label(board, image=image, width=27, height=27, padx=0, pady=0)
    #         label.grid(row=row, column=column, padx=0, pady=0)
    #         label.bind("<Enter>", enter)
    #         label.bind("<Leave>", leave)
    #         label.bind("<Button-1>", playBead)

    root.mainloop()



main()
