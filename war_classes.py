import random

from war_constants import suits, ranks, values


class Card:
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self):
        # self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        self.card = []
        for suit in suits:
            for rank in ranks:
                self.card.append(Card(suit, rank))


    def shuffle(self):
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
        self.shuffle()
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

    def deal_one(self):
        return self.card.pop()


class Player:
    def __init__(self, deck_cards: dict, player_input: str):
        self.deck_cards = deck_cards
        self.player_input = player_input
        self.player_deck = deck_cards[player_input]

    def take_cards(self, cards: list):
        self.player_deck.extend(cards)

    def remove_card(self)-> Card:
        if self.player_deck:
            return self.player_deck.pop(0)

    def __str__(self):
        return f'{self.player_input} has: {len(self.player_deck)} cards left.'



