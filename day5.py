with open('day5input.txt') as f:
    seeds = []
    lines = f.readlines()
    seedLine = lines.pop(0)
    seedLine = seedLine.split()
    for w in seedLine:
        if w.isnumeric():
            seeds.append(int(w))
    

    seedRanges = []
    for i in range(len(seeds)//2):
        seedRanges.append([seeds[(i*2)],seeds[i*2]+seeds[(i*2)+1]])

    i=-1
    maps = [[]for _ in range(7)]
    for line in lines:
        if line[0].isnumeric():
            line = line.split()
            newTerm = []
            for w in line:
                newTerm.append(int(w))
            newTerm[-1] = newTerm[-2]+newTerm[-1]-1
            newTerm[0] = newTerm[0]-newTerm[1]
            maps[i].append(newTerm)
        elif len(line)>4: 
            i+=1
    
    for map in maps:
        for i in range(len(seeds)):
            seed = seeds[i]
            for j in range(len(map)):
                if seed<=map[j][2] and seed>=map[j][1]:
                    seeds[i] = seeds[i]+map[j][0]
                    break
    seeds.sort()
    for map in maps:
        newSeedRange = []
        while len(seedRanges)>0:
            seedRange = seedRanges.pop()
            lower = seedRange[0]
            upper = seedRange[1]
            for j in range(len(map)):
                if lower >=map[j][1] and upper <=map[j][2]:
                    newSeedRange.append([lower+map[j][0],upper+map[j][0]])
                    break
                if lower <= map[j][1] and upper <= map[j][2] and upper >= map[j][1]:
                    newSeedRange.append([map[j][1]+map[j][0],upper+map[j][0]])
                    seedRanges.append([lower,map[j][1]-1])
                    break
                if lower >= map[j][1] and upper >=map[j][2] and lower <=map[j][2]:
                    newSeedRange.append([lower+map[j][0],map[j][2]+map[j][0]])
                    seedRanges.append([map[j][2]+1,upper])
                    break
                if lower <=map[j][1] and upper >= map[j][2]:
                    newSeedRange.append([map[j][1]+map[j][0],map[j][2]+map[j][0]])
                    seedRanges.append([lower,map[j][1]-1])
                    seedRanges.append([map[j][2]+1,upper])
                    break
                if j == len(map)-1:
                    newSeedRange.append([lower,upper])
        seedRanges = newSeedRange    
    seedRanges.sort(key = lambda x: x[0])
    print(seedRanges[0])


    
            
