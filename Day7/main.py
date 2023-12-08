'''
Ranking of cards:
    2 < 3 < 4 < 5 < 6 < 7 < 8 < 9 < T < J < Q < K < A
    (T = 10, J = Jack, Q = Queen, K = King, A = Ace)
A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2

5 Cards:
    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Five of a kind: Five cards of the same value.
    
Rank each hand from strongest to weakest. 
You can determine the total winnings of this set of hands by adding up the 
result of multiplying each hand's bid with its rank.
'''

import numpy as np
from collections import Counter

filename = "C:\\Users\\Mohammed\\Documents\\VisualStudioCode\\AdventCode\\Day7\\adventday7input.txt"
testfilename = "C:\\Users\\Mohammed\\Documents\\VisualStudioCode\\AdventCode\\Day7\\day7biggertestinput.txt"

cardranks = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
test_cards = [['32T3K',765], ['T55J5',684],['KK677',28],['KTJJT',220],['QQQJA',483]]

def givescore(cards):
    for i, card in enumerate(cards):
        card.append(0)
        if 'J' in card:
            counts = Counter(card)
            del counts['J']
            most_common_card = counts.most_common(1)[0][0]
            card[i] = card.count(max(card))
    return cards

def replaceJ(card):
    for i in range(len(card)):
        if 'J' in card:
            counts = Counter(card)
            del counts['J']
            card[i] = card.count(max(card))
        
            
        
        
def workoutranking(cards):
    for card in cards:
        newcard = list(card[0])
        for i in range(len(newcard)):
            if newcard[i] == 'T':
                newcard[i] = 10
            elif newcard[i] == 'Q':
                newcard[i] = 11
            elif newcard[i] == 'K':
                newcard[i] = 12
            elif newcard[i] == 'A':
                newcard[i] = 13
            elif newcard[i] == 'J':
                newcard[i] = 1
            else:
                newcard[i] = int(newcard[i])
        if newcard.count(max(newcard, key=newcard.count)) == 5:
            card[2] = [14]
            card[2].extend(newcard)
            #print(card[2])
            #print("Five of a kind")
        elif newcard.count(max(newcard, key=newcard.count)) == 4:
            if newcard.count(1) == 1:
                card[2] = [12]
                card[2].extend(newcard)
                #print(card[2])
                #print("Four of a kind")
            card[2] = [13]
            card[2].extend(newcard)
            #print(card[2])
            #print("Four of a kind")
        elif newcard.count(max(newcard, key=newcard.count)) == 3:
            print(newcard)
            print(newcard.count(max(newcard)))
            if newcard.count(1) >= 2:
                return
            threeofakind = max(newcard,key=newcard.count)
            newcard2 = newcard.copy()
            newcard = list(filter((threeofakind).__ne__, newcard))
            if newcard.count(max(newcard, key=newcard.count)) == 2:
                card[2] = [5]
                card[2].extend(newcard2)
                #print(card[2])
                print("Full House")
            else:
                card[2] = [4]
                card[2].extend(newcard2)
                print(card[2])
                print("Three of a kind")
        elif newcard.count(max(newcard, key=newcard.count)) == 2:
            print(newcard)
            firstpair = max(newcard,key=newcard.count)
            newcard2 = newcard.copy()
            newcard3 = list(filter((firstpair).__ne__, newcard))
            #print(newcard3.count(max(newcard3)))
            if newcard3.count(max(newcard3, key=newcard.count)) == 2:
                card[2] = [3]
                card[2].extend(newcard2)
                #print(card[2])
                #print("Two Pairs")
            else: 
                card[2] = [2]
                card[2].extend(newcard2)
                #print(card[2])
                print("One Pair")
            #card[2] = pow(max(newcard,key=newcard.count),2) + sum((list(filter((max(newcard,key=newcard.count)).__ne__, newcard)))) 
        else:
            print(newcard.count(max(newcard, key=newcard.count)))
            print(newcard)
            print("High Card")
            if newcard.count(1) >= 1:
                card[2] = [14]
                card[2].extend(newcard)
            card[2] = [1]
            card[2].extend(newcard)
        card.remove(card[0])
        print()
    
    #print(cards)
    return cards

def main(cards):
    givescore(cards)
    workoutranking(cards)
    sum = 0
    cards = [[x[0], x[1] if isinstance(x[1], list) else [x[1]]] for x in cards]
    sortedcards = sorted(cards, key=lambda x: x[1], reverse=False)
    index = 1
    for card in sortedcards:
        print(card)
        sum += int(card[0])*index
        print(card[0]," x ",index," += ",sum)
        index += 1
    print(sum)


with open(testfilename, "r") as cards:
    cards = cards.read().splitlines()
    cards = [x.split() for x in cards]

main(cards)