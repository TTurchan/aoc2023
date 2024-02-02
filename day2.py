validID =0 
def findValidGames():
    with open('day2input.txt') as f:
        id = 1
        for line in f.readlines():
            for i in range(len(line)):
                if line[i] == ':':
                    line = line[i+1:]
                    break
            listed = line.split()
            valid = True
            for i in range(len(listed)//2):
                if int(listed[i*2]) >14:
                    valid = False
                    break
                if int(listed[i*2]) >13 and listed[(i*2)+1][0] in 'rg':
                    valid = False
                    break
                if int(listed[i*2]) > 12 and listed[(i*2)+1][0] in 'r':
                    valid = False
                    break
            if valid:
                validID +=id
            id+=1

def findMinCubes():
    powers = 0
    with open('day2input.txt') as f:
        for line in f.readlines():
            min = [0,0,0]
            for i in range(len(line)):
                if line[i] == ':':
                    line = line[i+1:]
                    break
            listed = line.split()
            for i in range(len(listed)//2):
                if listed[(i*2)+1][0] == 'r':
                    min[0] = max(min[0],int(listed[i*2]))
                if listed[(i*2)+1][0] == 'g':
                    min[1] = max(min[1],int(listed[i*2]))
                if listed[(i*2)+1][0] == 'b':
                    min[2] = max(min[2],int(listed[i*2]))
            powers+= (min[0]*min[1]*min[2])
    return powers

powers = findMinCubes()
print(powers)
