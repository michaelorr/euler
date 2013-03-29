#! /usr/bin/python

from collections import Counter

ranks = {'high_card': 0,
         'pair': 1,
         'two_pair': 2,
         'trips': 3,
         'straight': 4,
         'flush': 5,
         'full_house': 6,
         'quads': 7,
         's_flush': 8,
         'r_flush': 9}
values = {'2': 2,
          '3': 3,
          '4': 4,
          '5': 5,
          '6': 6,
          '7': 7,
          '8': 8,
          '9': 9,
          'T': 10,
          'J': 11,
          'Q': 12,
          'K': 13,
          'A': 14}

class Hand(object):

  def __init__(self, cards):
    self.cards = cards
    self.rank = self.rank()
    self.highcard = self.highcard()

  def __gt__(self, hand):
    if self.rank > hand.rank: return True
    elif self.rank == hand.rank: return self.highcard > hand.highcard
    else: return False

  def rank(self):
    if (self.r_flush()): return ranks['r_flush']
    if (self.s_flush()): return ranks['s_flush']
    if (self.quads()): return ranks['quads']
    if (self.full_house()): return ranks['full_house']
    if (self.flush()): return ranks['flush']
    if (self.straight()): return ranks['straight']
    if (self.trips()): return ranks['trips']
    if (self.two_pair()): return ranks['two_pair']
    if (self.pair()): return ranks['pair']
    return ranks['high_card']


  def highcard(self):
    return self.nums()[-1] 

  def two_pair(self):
    found_pair = False
    totals = Counter(self.nums())
    for num in totals:
      if totals[num] == 2 and found_pair: return True
      else: found_pair = True
    return False    

  def pair(self):
    totals = Counter(self.nums())
    for num in totals:
      if totals[num] == 2: return True
    return False    

  def s_flush(self):
    if (self.flush() and self.straight()): return True
    return False

  def r_flush(self):
    if (self.s_flush() and self.highcard == 'A'): return True
    return False

  def trips(self):
    totals = Counter(self.nums())
    for num in totals:
      if totals[num] == 3: return True
    return False

  def full_house(self):
    if (self.trips() and self.pair()): return True
    return False

  def quads(self):
    totals = Counter(self.nums())
    for num in totals:
      if totals[num] == 4: return True
    return False

  def flush(self):
    base_suit = self.cards[0][1]
    for card in self.cards:
      if card[1] != base_suit: return False
    return True
  
  def straight(self):
    try:
      for index, num in enumerate(self.nums()):
        if num + 1 != self.nums()[index + 1]:
          return False
      return True
    except (IndexError): pass

  def nums(self):
    return sorted([values[card[0]] for card in self.cards])


player1_score = 0

with open('data/054/test.txt') as fh:
  hands = [line.split() for line in fh.readlines()]

for hand in hands:
  """TODO: compare numbers on equals hands (pair of aces beats pair of 8s)"""
  """TODO: compare highcards on equals hands (high Q beats a high 8 with both have pair of 3s)"""
  hand1 = Hand([card for index, card in enumerate(hand) if index < 5])
  hand2 = Hand([card for index, card in enumerate(hand) if index >= 5])
  if hand1 > hand2:
    player1_score += 1

print player1_score
