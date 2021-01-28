from __future__ import annotations
from typing import TYPE_CHECKING
from hand import Hand

if TYPE_CHECKING:
    from deck import Deck


class Player:
    def __init__(self):
        self.hand: Hand = Hand([])
        self.chip = 500
    
    def draw_card(self, deck: Deck):
        self.hand.cards.append(deck.pick())