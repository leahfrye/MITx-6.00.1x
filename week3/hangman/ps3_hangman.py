# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "C:\projects\mitCourse6.00.1x\week3\hangman\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = loadWords()

# end of helper code
# -----------------------------------

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    guessedString = ""

    for letter in secretWord:
      if letter in lettersGuessed:
        guessedString += letter
      else:
        guessedString += "_" 

    if secretWord == guessedString:
      return True
    else:
      return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    string = ""
    for letter in secretWord:
      if letter in lettersGuessed:
        string += letter
      else:
        string += "_" 
    return string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = string.ascii_lowercase

    for letter in lettersGuessed:
      alphabet = alphabet.replace(letter, "")
    
    return alphabet

    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
        ## Add correct number of spaces to lettersGuessed list
    letterLength = len(secretWord)
    correctGuesses = []
    incorrectGuesses = []

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(letterLength) + " letters long")
    print("-------------")

    turn = 8;

    while turn > 0:
      print("You have " + str(turn) + " guesses left")
      print("Available letters: " + getAvailableLetters(correctGuesses + incorrectGuesses))
      guess = input("Please guess a letter: ")
      guess = guess.lower()

      wordSoFar = getGuessedWord(secretWord, correctGuesses)

      if isWordGuessed(secretWord, correctGuesses):
        print("Congratulations, you won!")
      
      else:

        if guess in incorrectGuesses or guess in correctGuesses:
          print("Oops! You've already guessed that letter: " + wordSoFar)

        elif guess not in secretWord:
          print("Oops! That letter is not in my word: " + wordSoFar);
          turn -= 1
          incorrectGuesses.append(guess)
        
        else:
          correctGuesses.append(guess)
          wordSoFar = getGuessedWord(secretWord, correctGuesses)
          print("Good guess: " + wordSoFar)
          
          if isWordGuessed(secretWord, correctGuesses):
            print("-------------")
            print("Congratulations, you won!")

      print("-------------")

    if "_" in wordSoFar:
      print("Sorry, you ran out of guesses. The word was " + secretWord + ".")


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
