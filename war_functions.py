from war_classes import Deck, Player, Card


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
        print('Player 2 Wins')
        return True
    elif len(player2.player_deck) == 0:
        print('Player 1 Wins')
        return True
    else:
        return False


game_on = True
war_on = False
deck1 = Deck().split_deck2()
player1 =  Player(deck1, 'player1')
player2 = Player(deck1, 'player2')


# In the main game loop
while game_on:
    if check_if_winner(player1, player2):
        game_on = False
        break

    player1.shuffle_hand()
    player2.shuffle_hand()

    # Correctly pass method references
    player1_card = player1.remove_card()
    player2_card = player2.remove_card()
    cards_on_table = [player1_card, player2_card]

    card1 = cards_on_table[0]
    card2 = cards_on_table[1]

    response = compare_cards(card1, card2)

    if response == 'Player 1':
        player1.take_cards(cards_on_table)
        print(player1)
    elif response == 'Player 2':
        player2.take_cards(cards_on_table)
        print(player2)
    elif response == "Tie":
        war_on = True
        print("PLAYERS AT WAR!")


    while war_on:
        if len(player1.player_deck) < 5:
            print('Player 2 Wins')
            game_on = False
            break
        elif len(player2.player_deck) < 5:
            print('Player 1 Wins')
            game_on = False
            break

        for num in range(5):
            player1_card = player1.remove_card()
            cards_on_table.append(player1_card)

        for num in range(5):
            player2_card = player2.remove_card()
            cards_on_table.append(player2_card)

        player1_card = cards_on_table[-6]
        player2_card = cards_on_table[-1]

        war_response = compare_cards(player1_card, player2_card)

        if war_response == 'Player 1':
            player1.take_cards(cards_on_table)
            war_on = False
            break
        elif war_response == 'Player 2':
            player2.take_cards(cards_on_table)
            war_on = False
            break
