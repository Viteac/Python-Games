import random

wins = [0,0]


def random_deal():
    rand_cards = random.choices([1, 2, 3, 4, 5 ,6, 7, 8, 9, 10], k=3)
    return rand_cards


def calc(who,cards):
    cards_sum = sum(cards)
    print(who,str(cards_sum)+",",'Cards:', end = ' ')
    print(*cards,sep=',')
    return cards_sum


while True:
    print('=' * 20)
    user = input('Game on y/n \n >>')
    if user == 'y':
        Computer= calc('Computer:', random_deal())
        You = calc('You:', random_deal())

        positive = ['Great, You won', 'You won', 'You were lucky, you won']
        negative = ['You won, Computer', 'Sorry, you lost', ' You\'re out of luck this time']
        if You > Computer:
            print(random.choice(positive))
            wins[0] += 1
        elif You == Computer:
            print('Draw')
        else:
            print(random.choice(negative))
            wins[1] += 1
    elif user == 'n':
        break
    else:
        print(' Try again buddy')

print(f' The final Score is: You: {wins[0]} Computer: {wins[1]}')