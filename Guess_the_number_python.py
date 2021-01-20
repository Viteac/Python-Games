import random

guess_limit = 3


def game():
    secret_number = random.randint(1, 9)
    print(secret_number)
    guess_count = 0
    while guess_count < guess_limit:
        try:
            print('guess the number')
            guess = int(input('>'))
        except ValueError:
            pass
        else:
            guess_count += 1
            if guess == secret_number:
                print('Great you won')
                print(f' You guest the number in {guess_count} guesses')
                ask = input('Want to play again? Y/N').upper()
                if ask == 'Y':
                    return game()
    else:
        print(f'you had your limits the secret number was {secret_number}')

    ask = input('Want to play again? Y/N').upper()
    if ask == 'Y':
        return game()


game()
