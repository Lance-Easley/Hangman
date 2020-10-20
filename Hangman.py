import Hangman_words
import Hangman_graphic
from os import system, name

#used to clear screen
def clear():
    if name == 'nt': 
        _ = system('cls') 

#initialize variables
word = Hangman_words.rand_word
word = word.casefold()
number_of_letters = len(word)
score = 0
wrong_guess = 0
letters_used = ''
letter_1 = ''
letter_2 = ''
letter_3 = ''
letter_4 = ''
letter_5 = ''
letter_6 = ''
letter_7 = ''
letter_8 = ''
letter_9 = ''
letter_10 = ''
letter_11 = ''
letter_12 = ''
letter_13 = ''
letter_14 = ''
letter_15 = ''
#determine how many blanks we need
if number_of_letters == 8:
    letter_1 = "_"
    letter_2 = "_"
    letter_3 = "_"
    letter_4 = "_"
    letter_5 = "_"
    letter_6 = "_"
    letter_7 = "_"
    letter_8 = "_"
    word_display = word + "       "
elif number_of_letters == 9:
    letter_1 = "_"
    letter_2 = "_"
    letter_3 = "_"
    letter_4 = "_"
    letter_5 = "_"
    letter_6 = "_"
    letter_7 = "_"
    letter_8 = "_"
    letter_9 = "_"
    word_display = word + "      "
elif number_of_letters == 10:
    letter_1 = "_"
    letter_2 = "_"
    letter_3 = "_"
    letter_4 = "_"
    letter_5 = "_"
    letter_6 = "_"
    letter_7 = "_"
    letter_8 = "_"
    letter_9 = "_"
    letter_10 = "_"
    word_display = word + "     "
elif number_of_letters == 11:
    letter_1 = "_"
    letter_2 = "_"
    letter_3 = "_"
    letter_4 = "_"
    letter_5 = "_"
    letter_6 = "_"
    letter_7 = "_"
    letter_8 = "_"
    letter_9 = "_"
    letter_10 = "_"
    letter_11 = "_"
    word_display = word + "    "
elif number_of_letters == 12:
    letter_1 = "_"
    letter_2 = "_"
    letter_3 = "_"
    letter_4 = "_"
    letter_5 = "_"
    letter_6 = "_"
    letter_7 = "_"
    letter_8 = "_"
    letter_9 = "_"
    letter_10 = "_"
    letter_11 = "_"
    letter_12 = "_"
    word_display - word + "   "
elif number_of_letters == 13:
    letter_1 = "_"
    letter_2 = "_"
    letter_3 = "_"
    letter_4 = "_"
    letter_5 = "_"
    letter_6 = "_"
    letter_7 = "_"
    letter_8 = "_"
    letter_9 = "_"
    letter_10 = "_"
    letter_11 = "_"
    letter_12 = "_"
    letter_13 = "_"
    word_display = word + "  "
elif number_of_letters == 14:
    letter_1 = "_"
    letter_2 = "_"
    letter_3 = "_"
    letter_4 = "_"
    letter_5 = "_"
    letter_6 = "_"
    letter_7 = "_"
    letter_8 = "_"
    letter_9 = "_"
    letter_10 = "_"
    letter_11 = "_"
    letter_12 = "_"
    letter_13 = "_"
    letter_14 = "_"
    word_display = word + " "
elif number_of_letters == 15:
    letter_1 = "_"
    letter_2 = "_"
    letter_3 = "_"
    letter_4 = "_"
    letter_5 = "_"
    letter_6 = "_"
    letter_7 = "_"
    letter_8 = "_"
    letter_9 = "_"
    letter_10 = "_"
    letter_11 = "_"
    letter_12 = "_"
    letter_13 = "_"
    letter_14 = "_"
    letter_15 = "_"
    word_display = word
else:
    print("WordGenError")
clear()
#while loop that is active as long as the score is not maxed
while score != number_of_letters:
    #prints hangman drawing from hangman_graphic
    Hangman_graphic.graphic(wrong_guess)
    #prints the blank spaces that can later be filled
    print(letter_1, letter_2, letter_3, letter_4, letter_5, letter_6, letter_7, 
    letter_8, letter_9, letter_10, letter_11, letter_12, letter_13, letter_14, 
    letter_15, "\t\t", "score:", score)
    #gets input from user for choosing letter or word
    choice = input("Letter or word guess? ")
    choice = choice[0].lower()
    multi_letter = False
    #if user chooses letter:
    if choice == 'l':
        #shows user what letters they have already chosen before
        print("Letters used:", letters_used)
        #asks the user for a letter
        guess_letter = input("Which letter? ")
        #checks to make sure the input is acceptable
        if len(guess_letter) > 1:
            print("Only one letter please")
            multi_letter = True
            input()
        elif len(guess_letter) == 0 or " " in guess_letter:
            print("Please type a letter")
            input()
        elif guess_letter in letters_used:
            print("That letter is already used")
            input()
        #if input is valid, scan to see where that letter is found in the word
        elif guess_letter in word:
            if guess_letter == word_display[0]:
                letter_1 = guess_letter
                score += 1
            if guess_letter == word_display[1]:
                letter_2 = guess_letter
                score += 1
            if guess_letter == word_display[2]:
                letter_3 = guess_letter
                score += 1
            if guess_letter == word_display[3]:
                letter_4 = guess_letter
                score += 1
            if guess_letter == word_display[4]:
                letter_5 = guess_letter
                score += 1
            if guess_letter == word_display[5]:
                letter_6 = guess_letter
                score += 1
            if guess_letter == word_display[6]:
                letter_7 = guess_letter
                score += 1
            if guess_letter == word_display[7]:
                letter_8 = guess_letter
                score += 1
            if guess_letter == word_display[8]:
                letter_9 = guess_letter
                score += 1
            if guess_letter == word_display[9]:
                letter_10 = guess_letter
                score += 1
            if guess_letter == word_display[10]:
                letter_11 = guess_letter
                score += 1
            if guess_letter == word_display[11]:
                letter_12 = guess_letter
                score += 1
            if guess_letter == word_display[12]:
                letter_13 = guess_letter
                score += 1
            if guess_letter == word_display[13]:
                letter_14 = guess_letter
                score += 1
            if guess_letter == word_display[14]:
                letter_15 = guess_letter
                score += 1
        #adds the chosen letter to the letters_used list iff it is a single letter
        if guess_letter not in letters_used and multi_letter == False:
            letters_used += guess_letter + ' '
        #if chosen letter is not in the word, user looses a life
        if guess_letter not in word and multi_letter == False:
            wrong_guess += 1
    #if user chooses word:
    if choice == 'w':
        #ask the user what word they think it is
        guess_word = input("Guess the word: ")
        guess_word = guess_word.casefold()
        #if their input matches the word, they win
        if guess_word == word:
            print(word.capitalize(), "is correct!")
            #ends the while loop by setting score to max
            score = number_of_letters
            print("\t\t\t\t score:", score)
        #if the player is wrong, they loose a life
        else:
            print("Nope, that's not it")
            wrong_guess += 1
            input()
    #if player looses all 10 lives, end the game
    if wrong_guess == 10:
        clear()
        Hangman_graphic.graphic(wrong_guess)
        print("You lost...")
        print("The word was", word)
        input()
        exit()
    #failsafe win condtion
    if score == number_of_letters:
        print("You win!")
        input()
        exit()
    clear()