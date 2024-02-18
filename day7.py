#5 of kind 6, 4 of kind 5, full house 4, 3 of kind 3, 2 pair 2, 1 pair 1, high card 0 
from bisect import bisect
with open('day7input.txt') as f:
    lines = f.readlines()
    handList = []
    for line in lines:
        handList.append((line[:5],int(line[6:-1])))
    def typeOfHand(hand):
        handSet = set(hand)
        if len(handSet) == 5:
            return 0
        if len(handSet) == 4:
            return 1
        if len(handSet) == 3:
            maxCt = 1
            for card in handSet:
                ct = hand.count(card)
                maxCt = max(maxCt,ct)
            if(maxCt == 3):
                return 3
            return 2
        if len(handSet) == 2:
            maxCt = 1
            for card in handSet:
                ct = hand.count(card)
                maxCt = max(maxCt,ct)
            if maxCt == 4:
                return 5
            return 4
        return 6
    def typeOfHandWithJokers(hand):
        handSet = set(hand)
        counts = []
        for card in handSet:
            if card != 'J':
                counts.append(hand.count(card))
        jokers = hand.count('J')
        if jokers == 5:
            return 6
        counts.sort(key = lambda x : -x)
        counts[0]+=jokers
        if counts[0] == 5:
            return 6
        if counts[0] == 4:
            return 5
        if counts[0] == 3:
            if counts[1] == 2:
                return 4
            return 3
        if counts[0] == 2:
            if counts[1] == 2:
                return 2
            return 1
        return 0
        
    def valOfCard(card):
        return -'AKQT98765432J'.find(card)
    handList = sorted(handList, key = lambda x : (typeOfHandWithJokers(x[0]), valOfCard(x[0][0]),valOfCard(x[0][1]),valOfCard(x[0][2]),valOfCard(x[0][3]),valOfCard(x[0][4])))
    tot = 0
    for i in range(len(handList)):
        tot+= handList[i][1]*(i+1)

    print(tot)
    print(248217452)
