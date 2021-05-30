import random
from time import sleep

guess_limit = 4  # Set the guesses limit


def game():

    def ask():  # Ask user if want to play again till he answers 'y','n'
        while True:
            again = input('Wanna play again Y/N?\n> ').lower()
            if again in 'yn':
                return again
            else:
                pass

    x = [random.randint(1, 10) for x in range(1, 20)] # Generate intro random numbers

    for val in x:
        print(val, end=' ', flush=True) # Flush intro x
        sleep(0.1)
        
    secret_number = random.randint(1, 11) # Mystery Random Number
    guess_count = 1
    while guess_count < guess_limit:  # Ask for number till the guess counter is lower than guess limit
        try:
            print(f'\nCount: {guess_count}') 
            print('Guess the number 1-10')
            guess = int(input('> '))
        except ValueError:    # Pass if player enters no digit
            pass
        else:
            if guess == secret_number:
                print('Great you won')
                print(f' You guest the number in {guess_count} guesses')
                if ask() == 'y':
                    return game()
            else:
                guess_count += 1  # Counter Increment
                if guess_count < guess_limit:
                    if guess < secret_number:
                        print('Too Low my. Try higher')
                    else:
                        print('Try higher')
    else:
        print(f'You had your limits mate, the secret number was {secret_number}')
    if ask() == 'y':
        return game()


game()
