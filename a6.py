"""
This Program outputs a variation of the popular game known as wordle. However this program selects a word(secret word) from a random list of words known to the program.
The program then compares the secret word to guesses at the word entered by the user (6 tries total). After each guess, the program outputs information regarding the letters of the guess (are they close to secret word? in wrong position? not part?). Duplicate words ignored.
Date: Nov 2022
"""

import random
def chooseWord():
    """
    This function chooses a word from a pre-defined list.
    Parameters:  None
    Return Value: a string representing the secret word
    """
    #DO NOT MODIFY THIS FUNCTION










    print("Welcome to wordle!")
    validWords = ["could", "smile", "ultra", \
              "beacon", "hearts", "cap", "wordle", \
              "computing", "python"]

    #random.randint(0, 5) will generate an integer between 0 and 5 (inclusive)
    #this is then used to select a value from the list validWords.
    
    wordPosition = random.randint(0,5)
    return validWords[wordPosition]


def checkLetters(secretWord, userWord):
    """
 This function checks the letters guessed by the user against the secret
    word and informs the user as to which letters are in the correct location,
    which letters are in the word but not in the correct location and which
    letters are not in the word.
    Paramters:   secretWord, userWord - strings
    Returns:  None
    """
    


    
    for i in range(len(userWord)): #this is so that the for loop can iterate through all the characters in the word
        if userWord[i].casefold() == secretWord[i].casefold(): #if the characters within i aka if the letter is in the correct place "the letter () is in the correct place" will be printed
            print("The letter " + userWord[i] + " is in correct place")
        elif userWord[i] != secretWord[i] and userWord[i] in secretWord: #if the letter is in the secretWord but is not in the right position. the statement " The letter () is in the word but not in the correct place currently speaking" is printed.
            print("The letter " + userWord[i] + " is in the word but not in the correct place currently speaking")
        else: #if the letter is not in the secretWord the statement "The letter() is not in the word" is printed.
            print("The letter " + userWord[i] + " is not in the word")


def checkForDuplicates(userWord):
    """
This function checks the user's word for duplicate letters.
    If there are duplicate letters, the function returns True, otherwise, False.
    Parameters:  userWord - string
    Return:  Boolean
    """

    for i in userWord.casefold(): #for loop for i in the word entered by user
        if len(set(userWord.casefold())) == len(userWord.casefold()): #this for loop will run and identify the duplicate characters (if applicable) and ask user to try to guess again(if guesses available).
            duplicate_characters = False
        else:
            duplicate_characters = True
    else:
        return duplicate_characters

def play(secretWord):
    """
This function allows the user to play the game, entering up to 6 words to
    try to guess the secret word. When the correct word is guessed, the play
    stops and the user is congratulated.
    Parameters: string representing the secretWord
    Return Value:  None
    """





    
    winning_state = 0 #winning state set to zero
    for guess in range(0,6): #so that there can only be upto 6 guesses available to the user
        userWord = input("Enter your guess: ")
        while checkForDuplicates(userWord): #checkForDuplicates function is called here: if there is a duplicate. User asked to guess again (if guesses still available).
            userWord = input("Your guess has duplicates in it try again: ")
        if userWord.casefold() == secretWord.casefold(): #if the user guesses the correct word. The next 3 lines run and then print a congratulatory message for the user. Game ends.
            winning_state = 1
            print("Congratulations You have guessed the correct word!")
            break
        else:
            checkLetters(secretWord, userWord)
    if winning_state == 1:
        print("You have won the game!") #program will also print this statement if the user is able to guess correctly within their given 6 attempts.
    else:
        print("Aw, you didn't guess the word correctly. Better luck next time!") #if the user is not able to succeed after 6 tries, the message below that they didn't guess the word correctly, better luck next time and thanks for playing this game will be printed.
        print("Thanks for playing this game!")

def main():

    """
This implements the user interface for the program.
    """


    
    secretWord = chooseWord() #the main function calls some of the other functions mentioned above such as: def play(secretWord). It also allows printing of statements saying the length/amount of letters in secretWord and the secretWord itself. 
    print(f"The secret word has {len(secretWord)} letters")
    print("The secret word is", secretWord)
    play(secretWord)
main() #call to main function
