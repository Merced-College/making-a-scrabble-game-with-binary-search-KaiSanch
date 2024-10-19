#Edited by Kai Sanchez on 10-15-24
#Improvement: Allow the user to exchange one of their letters.
#The user is prompted to exchange one of their four letters before they enter a word.
#They can choose which letter to exchange, and it will be replaced by a random letter not already in their set of letters.

import random
from bisect import bisect_left

#word class
class Word:
    def __init__(self, text):
        self.text = text.lower()

    def __lt__(self, other):
        return self.text < other.text

    def __eq__(self, other):
        return self.text == other.text

    def __str__(self):
        return self.text

#Scrabble game class
class ScrabbleGame:
    def __init__(self, word_file):
        self.words = []  
        self.load_words(word_file)   

    #loads words from the file in the word list
    def load_words(self, word_file): 
        with open(word_file, 'r') as f:
            
            self.words = sorted([Word(line.strip()) for line in f])

    #binary search 
    def is_valid_word(self, word):
        
        i = bisect_left(self.words, Word(word))
        
        return i != len(self.words) and self.words[i] == Word(word)

    #this generates the four letters to start the game
    def generate_letters(self):
        return random.sample('abcdefghijklmnopqrstuvwxyz', 4)

    #improvement, where player can exchange letter if they want
    def exchange_letter(self, letters):
        print(f"Your letters are: {' '.join(letters)}")
        while True:
            try:
                letter_to_exchange = input("Would you like to exchange a letter? (y/n): ").lower()
                if letter_to_exchange == 'y':
                    letter = input(f"Which letter would you like to exchange? {letters}: ").lower()
                    if letter in letters:
                        letters.remove(letter)
                        # Get a new random letter that is not in the current letters
                        new_letter = random.choice('abcdefghijklmnopqrstuvwxyz')
                        while new_letter in letters:
                            new_letter = random.choice('abcdefghijklmnopqrstuvwxyz')
                        letters.append(new_letter)
                        print(f"You exchanged {letter} for {new_letter}. Your new letters are: {' '.join(letters)}")
                    else:
                        print("That letter is not in your current set of letters.")
                elif letter_to_exchange == 'n':
                    break
                else:
                    print("Please enter 'y' or 'n'.")
            except ValueError:
                print("Invalid input. Please try again.")
        return letters

    # Starts game
    def start_game(self):
        random_letters = self.generate_letters()
        print(f"Your letters are: {' '.join(random_letters)}")

        # Allow the player to exchange letter
        random_letters = self.exchange_letter(random_letters)

        
        user_word = input("Enter a word using these letters: ").lower()

        # Check if the user's word is valid by using the Word class for comparison
        if self.is_valid_word(user_word):
            print(f"'{user_word}' is a valid word!")
        else:
            print(f"'{user_word}' is not a valid word.")


# Initialize and start the game
if __name__ == "__main__":
    game = ScrabbleGame("CollinsScrabbleWords_2019.txt")
    game.start_game()
