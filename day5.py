'''
Part 2
arr = []
ans = 0
with open("adventofcode/D5/day5.txt", "r") as f:
    for line in f:
        if line == '\n':
            break
        line = line.strip()
        rangeArray = line.split('-')
        arr.append([int(rangeArray[0]),int(rangeArray[1])])
newarr = sorted(arr, key = lambda x:x[0])
ansarr = [newarr[0]]
for i in newarr:
    if i == newarr[0]:
        continue
    uniqueRange = "True"
    for j in ansarr:
        if i[0] <= j[1]:
            uniqueRange = "False"
            if i[1] > j[1]:
                j[1] = i[1]
    if uniqueRange == "True":
        ansarr.append(i)
for i in ansarr:
    ans += (i[1]-i[0]+1)
print(ans)
'''

'''
Part 1
arr = []
ans = 0
with open("adventofcode/D5/day5.txt", "r") as f:
    for line in f:
        if line == '\n':
            break
        line = line.strip()
        rangeArray = line.split('-')
        arr.append(rangeArray)
    for line in f:
        line = line.strip()
        for i in arr:
            if int(i[0]) <= int(line) <= int(i[1]):
                ans += 1
                break
print(ans)
'''