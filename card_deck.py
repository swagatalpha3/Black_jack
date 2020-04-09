import random


class Deck():
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubes')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    current_deck = []

    def __init__(self):
        if len(Deck.current_deck) == 0:
            for suit in Deck.suits:
                for rank in Deck.ranks:
                    card_name = rank + ' of ' + suit
                    Deck.current_deck.append(card_name)

    def suffle(self):
        Deck.current_deck = random.sample(Deck.current_deck, k=len(Deck.current_deck))[:]


class Card(Deck):
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
              'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 1}

    def __init__(self):
        Deck.__init__(self)
        self.player1 = []
        self.player2 = []

    def __str__(self):
        return Deck.current_deck[0]

    def pull_card(self, number_of_cards, player):
        if player == 1:
            for num in range(number_of_cards):
                self.player1.append(Deck.current_deck[num])
        else:
            for num in range(number_of_cards):
                self.player2.append(Deck.current_deck[num])
        for num in range(number_of_cards):
            Deck.current_deck.pop(0)

    def total_value(self, player):
        if player == 1:
            total = 0
            for number in range(len(self.player1)):
                total += Card.values[self.player1[number].split(' ')[0]]
            return total
        else:
            total = 0
            for number in range(len(self.player2)):
                total += Card.values[self.player2[number].split(' ')[0]]
            return total


if __name__ == '__main__':
    deck1 = Card()
    # print(deck1.current_deck)
    # # print(deck1)
    deck2 = Card()
    # print(deck2.current_deck)
    deck2.suffle()
    # print(deck1.current_deck)
    # print(deck2.current_deck)
    # print(deck1)
    deck2.pull_card(3, 2)
    print(deck2.player2)
    print(deck2.total_value(2))
    deck2.pull_card(3, 1)
    print(deck2.player1)
    print(deck2.total_value(1))
    # print(random.sample(deck2.current_deck, k=52))
    # # print(len(deck1.current_deck))
