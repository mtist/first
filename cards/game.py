from cards import *
from player import *
from cleaner import *

player1 = Player(input('Первый игрок, введите имя: '))
player2 = Player(input('Второй игрок, введите имя: '))
cards = Cards()

player1.deck = cards.deck[:len(cards.deck)//2]
player2.deck = cards.deck[len(cards.deck)//2:]

while True:
    clear()
    print()
    print('''            {0}|{1}'''.format(player1.name.center(11), player2.name.center(11)))
    Cards.turn(player1, player1, player2)
    print('''           -------------------------
    Счёт:  |    {0}    |    {1}    |
           -------------------------'''.format((' ' + str(player1.count) if len(str(player1.count)) == 2 else ' ' + str(player1.count) + ' '), 
            (' ' + str(player2.count) if len(str(player2.count)) == 2 else ' ' + str(player2.count) + ' ')))
    input()
    if not player1.deck or not player2.deck:
        break