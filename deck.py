from card import Card
import random
from typing import List


class Deck:
    def __init__(self):
        self._cards:List[Card] = [Card(rank + suit) for rank in Card.RANKS_STR for suit in Card.SUITS]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self._cards)

    def pick(self):
        return self._cards.pop()

    @property
    def cards(self):
        return self._cards

    def __len__(self):
        return len(self._cards)


class SixDeck(Deck):
    def __init__(self):
        self._cards:List[Card] = [Card(rank + suit) for rank in Card.RANKS_STR for suit in Card.SUITS for i in range(6)]
        self.shuffle()