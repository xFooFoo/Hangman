# Python 3.8.6
# hidden words read from word.txt randomized by number of words
# push all letters of hidden word into a list
# if guessed letter is in the list, present the correct letters, and display the results alongside letters guessed
# if wrong then remove a life and show letters guessed so far
# Invalid validation: make sure user can only guess a-z, use lower case cast on their guess

from PyDictionary import PyDictionary
from typing import List
import os
import time
import random

def Hangman_setup():
    file_path = os.path.dirname(os.path.abspath(__file__)) + "\words.txt"
    with open(file_path, "r") as file:
        content = file.read()
    words = content.split() #55900 words in txt
    Hangman(words)

def Hangman(words: List[str]):
    finished = False
    MAX_GUESSES = 10
    guessed = []
    n = random.randint(0, 55900)
    secret = words[n]
    #print(secret)
    while (MAX_GUESSES>0 or finished):
        ############Round message##############
        print(f"{MAX_GUESSES} guess(es) left.")
        print("You have guessed these letters so far:")
        print(guessed)
        finished = True
        
        print()
        for letter in secret:
            if letter in guessed:
                print(letter, end=' ')
            else:
                print('_', end=' ')
                finished = False
                
        print()
        
        #Only finishes early if all letters are guessed
        if finished == True:
            break
                
        ###################Guess logic####################
        
        guess = input("Guess a letter: ").lower()
        time.sleep(0.25)
        print()
        if guess in guessed:
            print(f"You have guessed \"{guess}\" already")
        elif guess not in letters:
            print(f"{guess} is not a valid letter.")
        else:
            guessed.append(guess)
            if guess in secret:
                print(f"\"{guess}\" is in the word :)")
            else:
                print(f"\"{guess}\" is not in the word :(")
                MAX_GUESSES -= 1
                
    ##############GAME END#####################################
    print()        
    time.sleep(0.25)
    if MAX_GUESSES > 0:
        print(f"GGS! You have guessed \"{secret}\" with {MAX_GUESSES} lives left!")
    else:
        print(f"Nice try.")
        print(f"The secret word was \"{secret}\".")
    print()
    dictionary1 = PyDictionary()
    def_dict = dictionary1.meaning(secret)
    try:
        key = next(iter(def_dict))
    except TypeError:
        print("We cannot find {secret} in the dictionary")
    else:
        print(f"{secret.upper()} ({key}):")
        for definition in def_dict[key]:
            print(definition)
    print()
    ##############RESTART#####################################
    if input("Play again (Y/N)? ").upper() == ("Y" or "YES"):
        print()
        print()
        print()
        Hangman(words)

letters = [chr(ord('a') + i) for i in range(26)]
Hangman_setup()