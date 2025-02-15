import random

from war_constants import suits, ranks, values


class Card:
    """
    Represents a playing card with a suit, rank, and value.
    
    Attributes:
        suit (str): The suit of the card, e.g., 'Hearts', 'Diamonds', etc.
        rank (str): The rank of the card, e.g., 'Two', 'King', etc.
        value (int): The numerical value assigned to the card's rank (from values dictionary).
    """

    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    """
    Represents a standard deck of playing cards.
    
    Attributes:
        cards (list[Card]): A list of Card objects representing the deck.
    """

    def __init__(self):
        """
        Initializes a new deck of cards with all possible combinations
        of suits and ranks.
        """
        # self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        self.card = []
        for suit in suits:
            for rank in ranks:
                self.card.append(Card(suit, rank))

    def shuffle_deck(self):
        """
        Shuffles the cards in the deck in a random order.
        """
        random.shuffle(self.card)

    # def split_deck1(self)->dict:
    #     """
    #     Shuffles the deck and splits it into two parts.
    #     :return: dict{"player1": half_deck1, "player2": half_deck2}
    #     """
    #     self.shuffle()
    #     return {
    #         'player1': [str(card) for card in self.card[:26]],
    #         'player2': [str(card) for card in self.card[26:]]
    #     }
    def split_deck2(self):
        """
        Shuffles the deck and splits it into two equal parts for two players.
        
        Returns:
            dict: A dictionary with keys 'player1' and 'player2', 
                  each containing a list of 26 Card objects.
        """
        self.shuffle_deck()
        player1_deck = {'player1': []}
        player2_deck = {'player2': []}
        split_deck = {}

        for card in self.card[:26]:
            player1_deck['player1'].append(card)

        for card in self.card[26:]:
            player2_deck['player2'].append(card)
        split_deck['player1'] = player1_deck['player1']
        split_deck['player2'] = player2_deck['player2']

        return split_deck


class Player:
    """
    Represents a player in the card game, holding their deck of cards.

    Attributes:
        deck_cards (dict): A dictionary containing both players' cards.
        player_input (str): The name of the player, used as the key in deck_cards.
        player_deck (list[Card]): A list of Card objects representing the player's deck.
    """

    def __init__(self, deck_cards: dict, player_input: str):
        self.deck_cards = deck_cards
        self.player_input = player_input
        self.player_deck = deck_cards[player_input]

    def take_cards(self, cards: list):
        self.player_deck.extend(cards)

    def remove_card(self):
        if self.player_deck:
            return self.player_deck.pop(0)

    def shuffle_hand(self):
        random.shuffle(self.player_deck)

    def __str__(self):
        return f'{self.player_input} has: {len(self.player_deck)} cards left.'



