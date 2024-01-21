"""
Rock scissor paper
Create a rock scissor paper game
Player vs Computer
input: r, s, p
3 rounds
2 out of 3 wins
report score
"""
from rich import print
import random
hand = random.choices(["rock", "scissor", "paper"])
print(hand)