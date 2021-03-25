from colorama import Fore,Back,Style,init
from words import Words
import random
init()

# 1. Welcome
print("Welcome to the game of hangman in Python")

# 2. Function to get Words from words.py
def get_valid_word(Words):
  word = random.choice(Words)

# Choose a good word
  while '-' in word or ' ' in word: # While - or ' '
    word = random.choice(Words)
  return word

# Display word and its length with lines
my_word = get_valid_word(Words)
print(my_word + '\n',len(my_word))

# A feature that deploys _
# depending on the size of the word
# Example:
# A N O N Y M O U S
# _ _ _ _ _ _ _ _ _

for char in my_word:
  print(char, end=" ")
print("")
for char in my_word:
  print(Fore.CYAN + "_", end=" ")
print("")