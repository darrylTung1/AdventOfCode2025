'''
Part 2
arr = []
ans = 0
with open("adventofcode/D7/day7.txt", "r") as f:
    for line in f:
        line = line.strip()
        arr.append(line)
breadth = len(arr[0]) 
pos = [0 for _ in range(breadth)]
midpoint = int((breadth + 1)/2)
pos[midpoint-1] = 1
for i in range(2,len(arr),2):
    newpos = [0 for _ in range(breadth)]
    for j in range(len(arr[i])):
        if pos[j] > 0:
            if arr[i][j] == "^":
                newpos[j-1] += pos[j]
                newpos[j+1] += pos[j]
            else:
                newpos[j] += pos[j]
    pos = newpos[:]
for i in pos:
    ans += i
print(ans)
'''

'''
Part 1
arr = []
ans = 0
with open("adventofcode/D7/day7.txt", "r") as f:
    for line in f:
        line = line.strip()
        arr.append(line)
breadth = len(arr[0]) 
pos = [0 for _ in range(breadth)]
midpoint = int((breadth + 1)/2)
pos[midpoint-1] = 1
for i in range(2,len(arr),2):
    newpos = [0 for _ in range(breadth)]
    for j in range(len(arr[i])):
        if pos[j] == 1:
            if arr[i][j] == "^":
                ans += 1
                newpos[j-1] = 1
                newpos[j+1] = 1
            else:
                newpos[j] = 1
    pos = newpos[:]
print(ans)
'''