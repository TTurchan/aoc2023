with open('day4test.txt') as f:
    lines = f.readlines()
    scratches = [1 for _ in range(len(lines))]

    have = []
    flag = False
    for line in lines:
        inp = line.split()
        temp = 0
        winning = set()
        for word in inp:
            if flag:
                if word in winning:
                    temp+=1
            else:
                if word.isnumeric():
                    winning.add(word)
            if word == '|':
                flag = True
        have.append(temp)
        flag = False
    tot = 0
    print(have)
    for point in have:
        if point>0:
            tot+=2**(point-1)
    for i in range(len(have)):
        newcards =have[i]
        k=1
        while(k<=newcards and (i+k)<len(scratches)):
            scratches[i+k] = scratches[i] + scratches[i+k]
            k+=1
    totScratch = 0
    for scratch in scratches:
        totScratch+=scratch
    print(totScratch)
    print(11412387298491859141893461550173538305232104966)
    print(scratches)




















#import re
#import numpy as np
#import os
#currentDirectory = os.path.dirname(os.path.abspath(__file__))
#day4test = os.path.join(currentDirectory,'day4test.txt')
#hailstones = []
#intersections=0
#
#def checkFuture(xinitial, xintercept,xvel):
#    if xintercept-xinitial > 0 and xvel >0:
#        return True
#    if xintercept-xinitial <0 and xvel <0:
#        return True
#    return False
#def checkWindow(xintercept,yintercept):
#    if xMin <= xintercept and xMax >= xintercept:
#        if yMin <= yintercept and yMax >= yintercept:
#            return True
#    return False
#xMin,yMin,xMax,yMax = 7,7,27,27
#
#a = np.array([[1,2],[1,-1]])
#b = np.array([51,1])
#print(np.linalg.solve(a,b))
#with open(day4test) as f:
#    lines = f.readlines()
#    for line in lines:
#        hailstones.append([int(s) for s in re.findall(r'-?\d+\b', line)])
#        hailstones[-1].append(hailstones[-1][4]/hailstones[-1][3])
#    for i in range(len(hailstones)):
#        for j in range(i+1,len(hailstones)):
#            mi = hailstones[i][4]/hailstones[i][3]
#            mj = hailstones[j][4]/hailstones[j][3]
#            a = np.array([[1,mi],[1,mj]])
#            if np.linalg.matrix_rank(a) == 2:
#                b = np.array([hailstones[i][1]-(mi*hailstones[i][0]),hailstones[j][1]-(mi*hailstones[j][0])])
#                c = np.linalg.solve(a,b)
#                print(a,b,c,hailstones[i],hailstones[j])
#                print((c[0] * hailstones[i][3]) + hailstones[i][0] )
#           # if hailstones[i][6]!=hailstones[j][6]:
#           #     if checkFuture(hailstones[i][0],xint,hailstones[i][3]):
#           #         dd
#           #         a+=1
#           #         print(a,'a')
#           #         if checkFuture(hailstones[j][0],xint,hailstones[j][3]):
#           #             b+=1
#           #             print(b,'b')
#           #             print(xint,yint)
#           #             if checkWindow(xint,yint):
#           #                 c+=1
#           #                 print(c,'c')
#           #         intersections+=1
#print(intersections)
