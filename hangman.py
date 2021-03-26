from colorama import Fore,Back,Style,init
from words import Words
from hangmanpics import HANGMANPICS
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

my_word = get_valid_word(Words)
print(my_word + '\n',len(my_word))

for char in my_word:
  print(char, end=" ")
print("")
for char in my_word:
  print(Fore.CYAN + "_", end=" ")
print("")
    


def Hangman_Game():
  guesses =''
  Lives = 0
  while Lives < 6:
      guess = input("Begin.guess a Letter:") 
      guesses += guess       
      failed = 0
      for char in my_word:    
          if char in guesses:    
            print(char,end=" ")    
          else:
            print ("_",end=" ")     
            failed += 1 
      print("")
      if failed == 0:        
          print ("Winner")  
          break                                 
      if guess not in my_word:    
          Lives+=1        
          print("Faile. ")    
          print(HANGMANPICS[Lives])
          if Lives == 6:           
              print ("Game Over")       
            
Hangman_Game()