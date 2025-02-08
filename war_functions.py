from war_classes import Deck, Player, Card


def compare_cards(card1: [Card], card2: [Card]):
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


game_on = True
deck1 = Deck().split_deck2()
player1 =  Player(deck1, 'player1')
player2 = Player(deck1, 'player2')

poppers = player1.remove_card()
emp_list = [poppers]

while game_on:
    cards_on_table = []
    
    