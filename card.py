class Card:
    SUITS = ("h", "s", "d", "c")
    RANKS_STR = "A 2 3 4 5 6 7 8 9 T J Q K".split()
    RANKS_STR_TO_VALUE = {
        "A": 1,
        "K": 10,
        "Q": 10,
        "J": 10,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2
    }

    RANKS_INT_TO_STR = {
        14: "A",
        13: "K",
        12: "Q",
        11: "J",
        10: "T",
        9: "9",
        8: "8",
        7: "7",
        6: "6",
        5: "5",
        4: "4",
        3: "3",
        2: "2"
    }

    def __init__(self, value):
        self.suit = value[1]
        self.rank = value[0]
        self.value = self.RANKS_STR_TO_VALUE[value[0]]

    def __repr__(self):
        return self.rank + self.suit
