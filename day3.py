def checkSurrounding(i,j,mat):
    for k in range(i-1,i+2):
        for l in range(j-1,j+2):
            if k >=0 and k <len(lines):
                if l >= 0 and l<len(lines[0])-1:
                    if mat[k][l] not in '.0123456789':
                        print(i,j,k,l,mat[k][l])
                        return True
    return False
with open('day3input.txt') as f:
    lines = f.readlines()
    total = 0
    flag = False
    temp = 0
    for i in range(len(lines)):
        temp = 0
        flag = False
        for j in range(len(lines[0])):
            if lines[i][j] in '0123456789':
                temp = temp*10 + int(lines[i][j])
                if not flag:
                    flag = checkSurrounding(i,j,lines)
            else:
                if temp !=0:
                    if flag:
                        print(temp)
                        total+=temp
                    temp = 0
                flag = False
print(total)

