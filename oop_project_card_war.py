import random

SUITS = 'S D H C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

#-----------------------------------------------------------------------------------
class Deck:

    def __init__(self):
        self.deck = [(a,b) for a in SUITS for b in RANKS]
    
    def showDeck(self):
        print(self.deck)

    def shuffleDeck(self):
        random.shuffle(self.deck)

#-----------------------------------------------------------------------------------
class Cards():

    def __init__(self, deck):
        self.cards = [deck[:26],deck[26:]]

#-----------------------------------------------------------------------------------
class Player():

    def __init__(self, cards):
        self.cards = cards

    def getLen(self):
        if len(self.cards)>0:
             True
        else: 
            False

    def getHand(self):
        return self.cards[:1]
    
    def removeHand(self):
        self.cards = self.cards[1:]

#---------------------------------THE GAME-------------------------------------------------
deck = Deck()
cards = Cards(deck.deck)

cards = cards.cards

comp = Player(cards[0])
player = input("Enter the Name of Player: ")
score = {'comp': 0, player: 0}
player = Player(cards[1])

while len(comp.cards) and len(player.cards) :

    print(comp)

    if (player.cards[0][1]) > (player.cards[0][1]):
        score[player]+=1
    else:
        score['comp']+=1

    comp.removeHand()
    player.removeHand()

print(score)
