import random
###Easy word list
wordDictionary1 = ['buzz','buff','cozy','fox','puff','quiz','bell','fish','list','fair','calm','love','note','huge','spot',
                    'lucky','kitty','annoy','curve','proud','rhyme','stomp','feast','focus','learn','early','letter','match',
                    'puzzle','ignore','prefer','invite','remind','leader','repeat','decide','report','listen','espect','measure']
###Hard word list
wordDictionary2=['affix','avenue','awkward','beekeeper','boggle','cobweb','cycle','disavow','duplex','equip','exodus','funny',
                 'galaxy','gossip','icebox','injury','ivory','jackpot','jelly','jockey','joking','joyful','jumbo','kayak',
                 'khaki','kiosk','lengths','lucky','luxury','lymph','nightclub','onyx','ovary','pajama','pneumonia','pshaw']
###Main function
def main():
    ###Prompt user to enter the game
    stillPlaying = input('Welcome to hangman! Ready to play?(y/n): ')
    while stillPlaying.strip().lower() !='n':
        print('-------------------------------------------------')
        ###Promt user to select level
        wordChoice = int(input('Pick a level(1-Easy/2-Hard): '))
        ###Choose a random word
        if wordChoice == 1:
            randomWord = random.choice(wordDictionary1)
        elif wordChoice == 2:
            randomWord = random.choice(wordDictionary2)
        game(randomWord)
        stillPlaying = input('Continue?(y/n): ')
    print('Thank you for playing :)')
### print hangman
def print_hangman(wrong):
    if (wrong == 0):
        print('\n +----+')
        print('      |')
        print('      |')
        print('      |')
        print('     ===')
    elif (wrong == 1):
        print('\n+----+')
        print('o    |')
        print('     |')
        print('     |')
        print('    ===')
    elif (wrong == 2):
        print('\n+----+')
        print('o    |')
        print('|    |')
        print('     |')
        print('    ===')
    elif (wrong == 3):
        print('\n +----+')
        print(' o    |')
        print('/|    |')
        print('      |')
        print('     ===')
    elif (wrong == 4):
        print('\n +----+')
        print(' o    |')
        print('/|\   |')
        print('      |')
        print('     ===')
    elif (wrong == 5):
        print('\n +----+')
        print(' o    |')
        print('/|\   |')
        print('/     |')
        print('     ===')
    elif (wrong == 6):
        print('\n +----+')
        print(' o    |')
        print('/|\   |')
        print('/ \   |')
        print('     ===')
###Return rightletters
def printWord(guessLetters,randomWord):
    counter = 0
    rightLetters = 0
    for char in randomWord:
        if (char in guessLetters):
            print(randomWord[counter], end=' ')
            rightLetters += 1
        else:
            print(' ', end=' ')
        counter += 1
    return rightLetters
###Print lines
def printLines(randomWord):
    print('\r')
    for char in randomWord:
        print('\u203E', end=' ')
###Game function
def game(randomWord):
    print(randomWord)
    ###Prompt the user how many letters in the word
    for x in randomWord:
        print('_', end=' ')
    length_of_word_to_guess = len(randomWord)
    amount_of_times_wrong = 0
    current_guess_index = 0
    ###List to collect the guessed letters
    current_letters_guessed = []
    current_letters_right = 0
###Stop while loop after 6 wrong guesses or guessed the correct word
    while (amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess):
        print('\nLetters guessed so far: ')
        for letter in current_letters_guessed:
            ###Display the guessed letters
            print(letter, end=' ')
        ### Prompt user to guess a letter
        letterGuessed = input('\nGuess a letter: ')
        ### user is right
        if letterGuessed in randomWord:
            print_hangman(amount_of_times_wrong)
            current_guess_index += 1
            current_letters_guessed.append(letterGuessed)
            current_letters_right = printWord(current_letters_guessed,randomWord)
            printLines(randomWord)
            ### user was wrong
        else:
            amount_of_times_wrong += 1
            current_letters_guessed.append(letterGuessed)
            ### print the increased step of hangman
            print_hangman(amount_of_times_wrong)
            ### count the number of right guessed letters
            current_letters_right = printWord(current_letters_guessed,randomWord)
            printLines(randomWord)
        print(f'Right:{current_letters_right},      Wrong:{amount_of_times_wrong}')

if __name__== '__main__':
    main()


