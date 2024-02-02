total = 0
with open('day1input.txt') as f:
    for line in f.readlines():
        first = -1
        last = -1
        minInd = float('inf')
        maxInd = -1
        digits = ['one','two','three','four','five','six','seven','eight','nine']

        for i in range(len(digits)):
            digit = digits[i]
            if line.find((digit)) !=-1:
                if line.find((digit))<minInd:
                    first = i+1
                    minInd = line.find((digit))
                if line.rfind((digit))>maxInd:
                    last = i+1
                    maxInd =line.rfind((digit))
        for i in range(10):
            digit = i+1
            if line.find(str(digit)) != -1:
                if line.find(str(digit)) <minInd:
                    first = digit
                    minInd = line.find(str(digit))
                if line.rfind(str(digit))>maxInd:
                    last = digit
                    maxInd = line.rfind(str(digit))
        if maxInd != -1:
            total+= 10*first + last
print(total)
