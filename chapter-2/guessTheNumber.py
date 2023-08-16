import random, sys

print('Welcome to the guess the number game!\n\n')

print('Do you wish to play?')
userChoice = True
while (userChoice):
    print('Please enter your response (y/n) : ')
    userChoiceStr = input()
    if (userChoiceStr.lower() == 'y' or userChoiceStr.lower() == 'yes'):
        userChoice = True
    elif (userChoiceStr.lower() == 'n' or userChoiceStr.lower() == 'no'):
        print('goodbye')
        userChoice = False
        break
    else:
        print('You did not enter a valid response.')
        continue

    secretNumber = random.randint(1, 20)
    print('\nI am thinking of a number between 1 and 20. I will give you 6 guesses to figure out the number I guessed.')

    for guessesTaken in range(1, 7):
        print('Take a guess.')
        guess = int(input())
        if guess < secretNumber:
            print('\nYour guess is too low .')
        elif guess > secretNumber:
            print('\nYour guess is too high')
        else:
            break
        print("Guesses remaining: " + str(6 - guessesTaken))

    if guess == secretNumber:
        print('Good job! You guessed my number in ' + str(guessesTaken) + 'guesses!')
    else:
        print('Nope. The number I was thinking of was ' + str(secretNumber))

    print('\nDo you wish to play again?')