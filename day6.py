from sympy import solve
from sympy.abc import x
import math
with open('day6input.txt') as f:
    lines = f.readlines()
    times = lines[0].split()[1:]
    dists = lines[1].split()[1:]
    sols = []
    print(times)
    def findRange(t,d):
        ranges = solve((x**2)-(t*x)+d,x)
        print(ranges)
        out = [0,0]
        out[0] = math.ceil(ranges[0])
        out[1] = math.floor(ranges[1])
        if out[0] == ranges[0]:
            out[0] = out[0]+1
        if out[1] == ranges[1]:
            out[1] = out[1]-1

        return out
    output = 1
    for i in range(len(times)):
        sols.append(findRange(int(times[i]),int(dists[i])))
        output*=((sols[-1][1]-sols[-1][0])+1)
    print(sols)
    print(output)

    time = ''
    dist = ''
    for i in range(len(times)):
        time+=times[i]
        dist+=dists[i]

    time = int(time)
    dist = int(dist)
    final = findRange(time,dist)
    print((final[1]-final[0])+1)

