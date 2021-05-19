import random
from time import sleep

guess_limit = 4  # Set the guesses limit


def game():
    x = [random.randint(1, 10) for x in range(1, 40)] # Generate intro random numbers

    for val in x:
        print(val, end=' ', flush=True)
        sleep(0.1)
    secret_number = random.randint(1, 9) # Mystery Random Number
    guess_count = 1
    while guess_count < guess_limit:  # Ask for number till the guess counter is lower than guess limit
        try:
            print(f'\nCount: {guess_count}') 
            print('Guess the number')
            guess = int(input('>'))
        except ValueError:    # Pass if player enters no digit
            pass
        else:
            guess_count += 1  #Counter Increment
            if guess == secret_number:
                print('Great you won')
                print(f' You guest the number in {guess_count} guesses')
                ask = input('Want to play again? Y/N').upper()
                if ask == 'Y':
                    return game()
    else:
        print(f'You had your limits mate, the secret number was {secret_number}')
    ask = input('Want to play again? Y/N').upper()
    if ask == 'Y':
        return game()


game()
