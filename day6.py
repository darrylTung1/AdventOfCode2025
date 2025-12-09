'''
Part 2
arr = []
with open("adventofcode/D6/day6.txt", "r") as f:
    for line in f:
        line = line.strip('\n')
        arr.append(line)
height = len(arr)
breadth = len(arr[0])
sign = "Unknown"
total = 0
ans = 0
for i in range(breadth):
    num = ''
    blank = "True"
    for j in range(height):
        if arr[j][i] == "*":
            total = 1
            sign = "*"
            blank = "False"
        elif arr[j][i] == "+":
            total = 0
            sign = "+"
            blank = "False"
        elif arr[j][i] != ' ':
            num += arr[j][i]
            blank = "False"
    if blank == "True":
        ans += total
        total = 0
        continue
    if sign == "*":
        total *= int(num)
    elif sign == "+":
        total += int(num)
print(ans+total)
'''

'''
Part 1
arr = []
with open("adventofcode/D6/day6.txt", "r") as f:
    for line in f:
        line = line.strip()
        arr.append(line.split())
symbolList = arr.pop()
ans = 0
for i in range(len(arr[0])):
    if symbolList[i] == '*':
        total = 1
    elif symbolList[i] == '+':
        total = 0
    for j in range(len(arr)):
        if symbolList[i] == '*':
            total *= int(arr[j][i])
        elif symbolList[i] == '+':
            total += int(arr[j][i])
    ans += total
print(ans)
'''