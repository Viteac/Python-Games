import random
import os
from time import sleep

va = 'eyuioa'
cons = 'qwrtpsdfghjklzxcvbnm'

ban = '''   ___                               __    __              _
  / _ \_   _  ___  ___ ___    __ _  / / /\ \ \___  _ __ __| |
 / /_\/ | | |/ _ \/ __/ __|  / _` | \ \/  \/ / _ \| '__/ _` |
/ /_\\| |_| |  __/\__ \__ \ | (_| |  \  /\  / (_) | | | (_| |
\____/ \__,_|\___||___/___/  \__,_|   \/  \/ \___/|_|  \__,_|
ver. 0.9 by Viteac '''


def rand_word():
    animal = ('koala', 'kangaroo', 'alligator', 'sheep', 'hippopotamus', 'crocodile', 'chicken', 'duck')
    fruit = ('banana', 'apple', 'watermelon', 'berry', 'pineapple', 'peach', 'kiwi')
    kinds = {'animals': animal, 'fruits': fruit}
    kind = random.choice(tuple(kinds.keys()))
    word = random.choice(kinds[kind])
    return word, kind


def agai(ca, gu, this, gue=0, pi=0, mis=0):
    os.system('clear')
    print(ban)
    print()
    bon = len(gu) - gue - mis
    if mis == 0:
        bon += 5
    pi = pi + this + bon
    print(f'Category: {ca.capitalize()}, Word: {gu}, Guesses: {gue} \nThis round points: {this} Bonus:{bon} Total: {pi}')
    while True:
        try:
            choice = input('Another round Y/N \n >>> ').lower()
            if choice not in ['y', 'n']:
                raise ValueError
        except ValueError:
            print('Try again. Make a choice')
        else:
            if choice == 'y':
                game(pi)
            elif choice == 'n':
                print('See you next time')
                sleep(2)
                exit()


def game(pi):

    word, kind = rand_word()
    mi = 0
    p = 0
    s = pi
    used = []
    disp = '#' * len(word)
    displi = list(disp)
    cnt = 0
    vow = sum(1 for x in word if x in va)
    co = sum(1 for x in word if x in cons)
    print(f'Your word is from category: {kind.capitalize()}')
    while cnt < len(word):
        sleep(2)
        os.system('clear')
        print(ban)

        print()
        print()
        print(word)
        print(f'Points: Total {s} This round: {p}')
        print('Category:', kind.capitalize(), 'Vowels:', vow, 'Consonants:', co, 'Your Guesses:', ''.join(displi))

        print('=' * 60)
        print(f'You have {len(word) - cnt} chances')

        guess = input('Enter a letter:\n >> ').lower()
        if guess == '':
            continue
        positive = [f'Great, {guess} is in a mystery word', f'Good man, there\'s "{guess}" in that word']
        negative = [f'Sorry buddy, there\'s no "{guess}" in that word', f'Nope, no "{guess}" in mystery word',
                    f'Wrong choice, no "{guess}" here ']
        if len(guess) > 1:
            if guess == word:
                cnt += 1

                print(f'BRAVO.\nYou\'ve guessed mystery word with {cnt} mistake.\n Mystery word\'s >>{word}<< and have {p} with 3 points bonus.')
                agai(kind, word, p, gue=cnt, pi=s)

            else:
                p -= 1

        elif guess in word:
            print(random.choice(positive))
            m = word.count(guess)
            p += m
            cnt += 1
            for i in range(len(word)):
                if word[i] == guess:
                    displi[i] = guess
        elif guess in used:
            print(f' You\'ve used letter {guess} already')
            cnt += 1
            mi += 1
        else:
            cnt += 1
            mi += 1
            print(random.choice(negative))

        if ''.join(displi) == word:
            print(f'BRAVO.\nYou\'ve guessed mystery word with {cnt} mistake.\n Mystery word\'s >>{word}<<')
            print(f'You got {p} points')
            agai(kind, word, p, mis=mi, gue=cnt)
    else:

        print('You\'ve used your limits.')
        p += len(word) - cnt
        print(f'You got {p} points.\n The mystery word was: {word}')
        again = input('Do you want to play again?\nY/N: ')
        if again.lower() == 'y':
            sleep(1)
            os.system('clear')
            return game(pi=p)


game(0)
