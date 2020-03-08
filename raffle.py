#! /usr/bin/python3

import random

tickets = [
    ('Ayrenn', 100),
    ('Emeric', 75),
    ('Jorunn', 25),
]

lots = [
    "100K Gold",
    "Recipe: Psijic Ambrosia",
    "25x Dubious Camoran Throne",
    "6 Sealed Blacksmithing Writs",
]

def raffle(tickets, lots):
    """Run a raffle, producing a list of randomly selected winners.

    Arguments:
    tickets -- a list containing (name, number of tickets purchased) tuples
    lots -- a list of lots available to be won

    Each ticket can only win once, but people purchasing multiple tickets
    can win multiple times.

    There must be at least as many tickets purchased as there are lots.
    """
    return zip(random.sample([x for (x,n) in tickets for i in range(n)], len(lots)), lots)

def show(outcome):
    """Print out the raffle results in a human readable format."""
    for i, (winner, item) in enumerate(outcome):
        print("Lot #{} ({}) won by {}".format(i, item, winner))

def main():
    show(raffle(tickets, lots))

if __name__ == '__main__':
    main()
