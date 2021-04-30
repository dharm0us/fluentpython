import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

f = FrenchDeck()
print(len(f))
import random
print(random.choice(f)) # this also needs __len__
print(f.ranks)
print(f.suits)
print(f[0]) # first card
print(f[-1]) # last card

# even though we haven't implemented __contains__, we can use the in operator due to __getitem__, however a sequential scan would happen in this case
print(Card('Q', 'hearts') in f)
# it's also iterable due to __getitem__
distinct_ranks = {c.rank for c in f}
print(distinct_ranks)
#reversed
distinct_suits = {c.suit for c in reversed(f)} #reversed needs __len__
print(distinct_suits)

# how to sort
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for c in sorted(f, key=spades_high):
  print(c)


  # __repr__ vs __str__ => str is for user friendly string, repr should print in a way that it's easy to recreate the object.