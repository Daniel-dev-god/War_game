from war_classes import Player, Card


def compare_cards(card1: Card, card2: Card):
    """
    Compares two cards to determine which one has the higher value.

    Parameters:
        card1 (Card): The first card to compare.
        card2 (Card): The second card to compare.

    Returns:
        str: 'Tie' if the cards have equal values, 
             'Player 1' if card1 is greater, 
             'Player 2' if card2 is greater.
    """
    if card1.value == card2.value:
        return 'Tie'
    elif card1.value > card2.value:
        return 'Player 1'
    else:
        return 'Player 2'


def check_if_winner(player1: Player, player2: Player) -> bool:
    """
    Determines if either player has won the game by running out of cards.

    Parameters:
        player1 (Player): The first player's object containing their deck.
        player2 (Player): The second player's object containing their deck.

    Returns:
        bool: True if there is a winner ('Player 1 Wins' or 'Player 2 Wins'), 
              False if both players still have cards in their decks.
    """
    if len(player1.player_deck) == 0:
        print('Player 2 Wins')
        return True
    elif len(player2.player_deck) == 0:
        print('Player 1 Wins')
        return True
    else:
        return False
