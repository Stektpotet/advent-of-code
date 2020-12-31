from copy import deepcopy
from sys import stdin
from collections import deque

if __name__ == '__main__':
    starting_decks = [
        deque(map(int, a)) for p1, p2 in [tuple(stdin.read().replace('\r', '').split('\n\n'))]
        for a in (p1.split()[2:], p2.split()[2:])
    ]
    deck_size = sum(len(d) for d in starting_decks)
    # Part 1
    decks = deepcopy(starting_decks)
    while len(decks[0]) > 0 and len(decks[1]) > 0:
        cards = tuple(d.popleft() for d in decks)
        winner = cards[0] < cards[1]                # is card 1 higher rank
        decks[winner].extend(cards[::1-winner*2])   # append cards in order; winning first, losing second
    print(sum(i*c for i, c in ((deck_size - i, c) for i, c in enumerate(decks[len(decks[1]) > 0]))))

    # Part 2
    decks = starting_decks

    def recursive_combat_game(decks):
        previous_decks = set()
        while len(decks[0]) > 0 and len(decks[1]) > 0:
            deck_hashes = tuple(hash(tuple(d)) for d in decks)
            if any(d in previous_decks for d in deck_hashes):
                return 0
            previous_decks.update(deck_hashes)

            cards = tuple(d.popleft() for d in decks)
            if all(cards[i] <= len(decks[i]) for i in range(2)):  # if both players have larger decks than both card ranks
                winner = recursive_combat_game(
                    tuple(deque(decks[player][i] for i in range(cards[player])) for player in range(2))
                )
            else:
                winner = cards[0] < cards[1]  # is card 1 higher rank
            decks[winner].extend(cards[::1 - winner * 2])  # append cards in order; winning first, losing second
        return len(decks[1]) > 0  # player 1 wins game ?

    winner = recursive_combat_game(decks)
    print(sum(i * c for i, c in ((deck_size - i, c) for i, c in enumerate(decks[winner]))))


    # draw cards
