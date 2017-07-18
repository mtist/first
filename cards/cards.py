import random


class Cards():

    def __init__(self):
        self.suits = ["♥","♦","♠","♣"]
        self.nums = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.deck = [(num,suit) for suit in self.suits for num in self.nums]
        random.shuffle(self.deck)


    def get_cards(self, player):
        while True:
            yield player.deck.pop()


    def turn(self, player1, player2):
        k = 0
        for self.card1, self.card2 in zip(Cards.get_cards(player1, player1),Cards.get_cards(player2, player2)):
            # print(self.card1, self.card2)
            print('''           -------------------------
    Карта: |    {0}    |    {1}    |
           -------------------------'''.format((''.join(self.card1) if len(self.card1[0]) != 1 else ' '.join(self.card1)),
            (''.join(self.card2) if len(self.card2[0]) != 1 else ' '.join(self.card2))))

            if self.card1[0] < self.card2[0]:
                k += 2
                player2.count += k
                break

            elif self.card2[0] < self.card1[0]:
                k += 2
                player1.count += k
                break

            elif self.card1[0] == self.card2[0]:
                break
