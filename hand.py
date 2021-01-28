from card import Card
from typing import List


class Hand:
    def __init__(self, cards: List[Card]):
        self.cards: List[Card] = cards

    def return_sum(self):
        return sum([card.value for card in self.cards])

    def return_sum_list(self):

        sum_list = [self.return_sum()]
        if "A" in [card.rank for card in self.cards]:
            num_A = [card.rank for card in self.cards].count("A")

            for i in range(num_A):
                sum_list.append(sum_list[-1] + 10)

        return sum_list

    def clear(self):
        self.cards = []

    def __len__(self):
        return len(self.cards)
