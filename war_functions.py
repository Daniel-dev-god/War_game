from war_classes import Deck, Player, Card


def compare_cards(card1: [Card], card2: [Card]):
    if card1.value == card2.value:
        return 'Tie'
    elif card1.value > card2.value:
        return 'Player 1'
    else:
        return 'Player 2'
    

deck1 = Deck().split_deck2()
player1 =  Player(deck1, 'player1')
player2 = Player(deck1, 'player2')

poppers = player1.remove_card()
emp_list = [poppers]
print(poppers)
print(player1)
print(emp_list)