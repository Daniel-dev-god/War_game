from war_classes import Deck, Player
from war_functions import check_if_winner, compare_cards

def play_game():
    game_on = True
    war_on = False

    deck1 = Deck().split_deck2()
    player1 = Player(deck1, 'player1')
    player2 = Player(deck1, 'player2')

    # In the main game loop
    round_number = 1  # Counter for round numbers
    while game_on:
        print(f"--------------------- ROUND {round_number} ---------------------")
        if check_if_winner(player1, player2):
            break

        print("Shuffling Player 1's hand...")
        player1.shuffle_hand()
        print("Shuffling Player 2's hand...")
        player2.shuffle_hand()

        # Correctly pass method references
        player1_card = player1.remove_card()
        player2_card = player2.remove_card()
        cards_on_table = [player1_card, player2_card]

        card1 = cards_on_table[0]
        card2 = cards_on_table[1]

        print(f"Player 1 plays: {card1}")
        print(f"Player 2 plays: {card2}")
        response = compare_cards(card1, card2)
        print(f"{response} wins the fight!")
        print(f"End of Round {round_number}")
        round_number += 1

        if response == 'Player 1':
            player1.take_cards(cards_on_table)
            print(player1)
        elif response == 'Player 2':
            player2.take_cards(cards_on_table)
            print(player2)
        elif response == "Tie":
            war_on = True
            print("PLAYERS AT WAR! Both cards have the same value.")
            print("Each player will add the next 5 cards to the war pile...")

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
                print(f"Player 1 adds {player1_card} to the war pile.")

            for num in range(5):
                player2_card = player2.remove_card()
                cards_on_table.append(player2_card)
                print(f"Player 2 adds {player2_card} to the war pile.")

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

    print(f"Game Over! {player1} {player2}")


if __name__ == '__main__':
    play_game()

