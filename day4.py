'''
Part 2
def clear(arr,ans):
    length = len(arr[0])
    for i in range(length):
        for j in range(length):
            if arr[i][j] != '@':
                continue
            count = 0
            if i - 1 >= 0 and j - 1 >= 0 and arr[i-1][j-1] == '@':
                count += 1
            if i - 1 >= 0 and arr[i-1][j] == '@':
                count += 1
            if i - 1 >= 0 and j + 1 < length and arr[i-1][j+1] == '@':
                count += 1
            if j - 1 >= 0 and arr[i][j-1] == '@':
                count += 1
            if j + 1 < length and arr[i][j+1] == '@':
                count += 1
            if i + 1 < length and j - 1 >= 0 and arr[i+1][j-1] == '@':
                count += 1
            if i + 1 < length and arr[i+1][j] == '@':
                count += 1
            if i + 1 < length and j + 1 < length and arr[i+1][j+1] == '@':
                count += 1
            if count < 4:
                ans += 1
                arr[i][j] = '.'
    return arr,ans

arr = []
with open("adventofcode/D4/day4.txt", "r") as f:
    for line in f:
        line = line.strip()
        arr.append(list(line))
ans = 0
for i in range(1000):
    arr, ans = clear(arr,ans)
for i in arr:
    print(i)
print(ans)
'''

'''
Part 1
arr = []
with open("adventofcode/D4/day4.txt", "r") as f:
    for line in f:
        line = line.strip()
        arr.append(line)
length = len(arr[0])
ans = 0
for i in range(length):
    for j in range(length):
        if arr[i][j] != '@':
            continue
        count = 0
        if i - 1 >= 0 and j - 1 >= 0 and arr[i-1][j-1] == '@':
            count += 1
        if i - 1 >= 0 and arr[i-1][j] == '@':
            count += 1
        if i - 1 >= 0 and j + 1 < length and arr[i-1][j+1] == '@':
            count += 1
        if j - 1 >= 0 and arr[i][j-1] == '@':
            count += 1
        if j + 1 < length and arr[i][j+1] == '@':
            count += 1
        if i + 1 < length and j - 1 >= 0 and arr[i+1][j-1] == '@':
            count += 1
        if i + 1 < length and arr[i+1][j] == '@':
            count += 1
        if i + 1 < length and j + 1 < length and arr[i+1][j+1] == '@':
            count += 1
        if count < 4:
            ans += 1
for i in arr:
    print(i)
print(ans)
'''