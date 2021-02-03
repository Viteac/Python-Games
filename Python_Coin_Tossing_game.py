import random

scores = [0,0]
for u in range(100):
    toss =  random.choice(0,1)
    scores[toss] +=1
print(f' Heads: {scores[0]} | {scores[1]} Tails')
