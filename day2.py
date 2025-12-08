'''
Part 2
def solution(x):
    strX = str(x)
    length = len(strX)
    if length == 1:
        return "ValidShort"
    for i in range(0,int(length/2)):
        if length % (i+1) == 0: #subsequence of length i+1
            repetition = int(length/(i+1)) #subsequence repeated length/(i+1) times
            subsequence = strX[0:i+1]
            numOfEquality = 0
            for j in range(1,repetition):
                if strX[j*(i+1):(j+1)*(i+1)] == subsequence:
                    numOfEquality += 1
            if numOfEquality == repetition - 1:
                return "Invalid"
    return "Valid"

with open("adventofcode/D2/day2.txt", "r") as f:
    givenInput = f.readline()
    inputArray = givenInput.split(',')
    ans = 0
    for ranges in inputArray:   
        rangeArray = ranges.split('-')
        for i in range(int(rangeArray[0]), int(rangeArray[1]) + 1):
            if solution(i) == "Invalid":
                ans += i
    print(ans)
'''



"""
Part 1
def solution(x):
    strX = str(x)
    length = len(strX)
    if length % 2 == 0:
        midpoint = int(length/2)
        if strX[:midpoint] == strX[midpoint:]:
            return "Invalid"
        else:
            return "Valid2"
    else:
        return "Valid"

with open("adventofcode/D2/day2.txt", "r") as f:
    givenInput = f.readline()
    inputArray = givenInput.split(',')
    ans = 0
    for ranges in inputArray:   
        rangeArray = ranges.split('-')
        for i in range(int(rangeArray[0]), int(rangeArray[1]) + 1):
            if solution(i) == "Invalid":
                ans += i
    print(ans)
"""