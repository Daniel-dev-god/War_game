from war_classes import Deck, Player, Card
from war_constants import war_on


def compare_cards(card1: Card, card2: Card):
    if card1.value == card2.value:
        return 'Tie'
    elif card1.value > card2.value:
        return 'Player 1'
    else:
        return 'Player 2'


def check_if_winner(player1: Player, player2: Player) -> str or None:
    """
    Checks if either player has no cards left in their deck.
    :param player1: Player object representing the first player.
    :param player2: Player object representing the second player.
    :return: str - 'Player 1 Wins', 'Player 2 Wins', or None if both have cards left.
    """
    if len(player1.player_deck) == 0:
        return 'Player 2 Wins'
    elif len(player2.player_deck) == 0:
        return 'Player 1 Wins'
    else:
        return None


def check_if_war(cards_on_table: list, war_on: bool = False):
    if not war_on:
        # Actually call remove_card() to get the card objects
        card1 = cards_on_table[0]()
        card2 = cards_on_table[1]()

        if compare_cards(card1, card2) == 'Player 1':
            player1.take_cards(emp_list)
        elif compare_cards(card1, card2) == 'Player 2':
            player2.take_cards(emp_list)
        elif compare_cards(card1, card2) == "Tie":
            war_on = True

    if war_on:
        # Similar correction for war scenario
        card1 = cards_on_table[-2]()
        card2 = cards_on_table[-1]()

        if compare_cards(card1, card2) == 'Player 1':
            player1.take_cards(emp_list)
        elif compare_cards(card1, card2) == 'Player 2':
            player2.take_cards(emp_list)


game_on = True
deck1 = Deck().split_deck2()
player1 =  Player(deck1, 'player1')
player2 = Player(deck1, 'player2')

poppers = player1.remove_card()
emp_list = [poppers]

# In the main game loop
while game_on:
    check_if_winner(player1, player2)
    # Correctly pass method references
    print(player1.remove_card(), player2.remove_card())
    player1_card = player1.remove_card()
    player2_card = player2.remove_card()
    cards_on_table = [player1_card, player2_card]
    check_if_war(cards_on_table)

    while war_on:
        player1_card = player1.remove_card()
        player2_card = player2.remove_card()
        cards_on_table.extend([player1_card, player2_card])
        check_if_war(cards_on_table)



# while game_on:
#     check_if_winner(player1, player2)
#     # logic here to handle what above code returns, otherwise broken winner checker
#
#     cards_on_table = [player1.remove_card, player2.remove_card]
#     check_if_war(cards_on_table)
#
#
#     while war_on:
#         cards_on_table.extend([player1.remove_card, player2.remove_card])


    
    