from deck import Deck
from player import Player


def initialize():
    player = Player()
    dealer = Player()
    return player, dealer


def player_win(player, bet_size):
        print("You won!")
        player.chip += bet_size
        print(f"Now you have {player.chip}")


def draw_match(player=None, bet_size=0):
        print("This match is draw.")


def player_lose(player, bet_size):
    print("You lost.")
    player.chip -= bet_size
    print(f"Now you have {player.chip}")


def play_blackjack(player, dealer):
    deck = Deck()

    # betting round
    print(f"You have {player.chip}. How much do you bet?")
    bet_size = int(input())

    # process exception
    while bet_size > player.chip:
        print("bet size must be smaller than your total amount of chips")
        print(f"You have {player.chip}. How much do you bet?")
        bet_size = int(input())
    
    # clear previous game
    player.hand.clear()
    dealer.hand.clear()

    for i in range(2):
        player.draw_card(deck)
        dealer.draw_card(deck)

    print(f"your hand is {player.hand.cards[0]} and {player.hand.cards[1]}")
    print(f"dealer's hand is {dealer.hand.cards[0]} and one downed card")

    # proccess blackjack
    print(player.hand.return_sum_list()[-1])
    if player.hand.return_sum_list()[-1] == 21:
        if not dealer.hand.return_sum_list()[-1] == 21:
            print("Blackjack!!")
            player.chip += bet_size * 3 //2
            print(f"You won {bet_size*3//2} and have {player.chip}")
            return
        else:
            print("Dealer has also blackjack, it's chop")


    print("Which do you want, 'Hit' or 'Stand'?")
    option = input()

    # process exception
    while not option in ["Hit", "Stand", "hit", "stand"]:
        print("You must input, 'Hit' or 'Stand'")
        option = input()


    while option in ["Hit", "hit"]:
        player.draw_card(deck)
        print(f"You drawed {player.hand.cards[-1]}")
        
        if min(player.hand.return_sum_list()) > 21:
            print("You busted!!")
            player_lose(player, bet_size)
            return
        
        else:
            print(f"Your hand is {player.hand.cards}")
            print("Which do you want, 'Hit' or 'Stand'?")

            option = input()
            while not option in ["Hit", "Stand", "hit", "stand"]:
                print("You must input, 'Hit' or 'Stand'")
                option = input()
    

    # This and below is functionalized only when "Stand" is selected
    print("dealer's hand is {}, {}".format(dealer.hand.cards[0], dealer.hand.cards[1]))
    print("Sum is {}".format(dealer.hand.return_sum_list()))

    while max([sum for sum in dealer.hand.return_sum_list() if sum <= 21]) <= 16:
        dealer.draw_card(deck)
        print("Dealer drawed {}".format(dealer.hand.cards[-1]))
        print("Sum is {}".format(dealer.hand.return_sum_list()))

        if min(dealer.hand.return_sum_list()) > 21:
            print("Dealer busted!!")
            player_win(player, bet_size)
            return

    # Compare hand strength
    player_strength = max([sum for sum in player.hand.return_sum_list() if sum <= 21])
    dealer_strength = max([sum for sum in dealer.hand.return_sum_list() if sum <= 21])

    print(f"Your sum is {player_strength}")
    print(f"Dealer's sum is {dealer_strength}")

    if player_strength > dealer_strength:
        player_win(player, bet_size)

    elif player_strength == dealer_strength:
        draw_match(player, bet_size)

    else:
        player_lose(player, bet_size)

        
player, dealer = initialize()

while True:
    play_blackjack(player, dealer)
    print("Do you want to continue? y/n")
    ans = input()
    if ans == "n":
        exit()
