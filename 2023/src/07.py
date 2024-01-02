#!/usr/bin/env python3


import os
import re


test = 0
part = "1"
dia = "07"

if test:
    dia = dia + "_test"

path = os.path.join("data", dia)

with open(path) as f:
    arquivo = f.read().splitlines()

cards = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")
cards_2 = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(", ")

value_cards = { cards[c]: len(cards) - c for c in range(len(cards)) }
value_cards_2 = { cards_2[c]: len(cards_2) - c for c in range(len(cards_2)) }


hands = []
for line in arquivo:
    hand = line.split(" ")

    unique_cards = len(set(hand[0]))

    if unique_cards == 1:
        value = 6
    elif unique_cards == 2:
        if max( [ hand[0].count(v) for v in set(hand[0]) ] ) == 4:
            value = 5
        else:
            value = 4
    elif unique_cards == 3:
        if max( [ hand[0].count(v) for v in set(hand[0]) ] ) == 3:
            value = 3
        else:
            value = 2
    elif unique_cards == 4:
        value = 1
    else:
        value = 0

    v_cards = [ value_cards[v] for v in hand[0] ]
    hands.append( [ hand[0], int(hand[1]), value ] + v_cards )

hands.sort(key=lambda x: (x[2:]))

ans = 0
for i, v in enumerate(hands, 1):
    ans += i * v[1]

print("parte 1:", ans)


hands = []
for line in arquivo:
    hand, bid = line.split(" ")
    dict_hand = { v: hand.count(v)  for v in set(hand) }

    j = dict_hand.get("J", 0)
    if j:
        del dict_hand["J"]

    for h in dict_hand:
        dict_hand[h] += j

    unique_cards = len(dict_hand)
    if unique_cards <= 1:
        value = 6

    elif unique_cards == 2:
        if max( dict_hand.values() ) == 4:
            value = 5
        else:
            value = 4

    elif unique_cards == 3:
        if max( dict_hand.values() ) == 3:
            value = 3
        else:
            value = 2
    elif unique_cards == 4:
        value = 1
    else:
        value = 0


    v_cards = [ value_cards_2[v] for v in hand ]
    hands.append( [ hand, int(bid), value ] + v_cards )

hands.sort(key=lambda x: (x[2:]))


for h in hands:
    print(h)



ans = 0
for i, v in enumerate(hands, 1):
    ans += i * v[1]

print("parte 2:", ans)
