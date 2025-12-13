'''
Part 2
arr = []
with open("adventofcode/D8/day8.txt", "r") as f:
    for line in f:
        line = line.strip()
        arr.append(line.split(','))
size = len(arr)
dis = []
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        distance = 0
        for k in range(3):
            coorDiff = (int(arr[i][k]) - int(arr[j][k])) ** 2
            distance += coorDiff
        dis.append((i,j,distance))
sortedDis = sorted(dis, key = lambda x: x[2])
count = 0
uniqueCircuits = 0
dic = {}
end = False
for i in sortedDis:
    if end == True:
        break
    if dic.get(i[0]) != None:
        x = dic.get(i[0])
        if dic.get(i[1]) != None:
            y = dic.get(i[1])
            for key,value in dic.items():
                if value == x:
                    dic[key] = y
        else:
            dic[i[1]] = dic.get(i[0])
    elif dic.get(i[1]) != None:
        x = dic.get(i[1])
        if dic.get(i[0]) != None:
            y = dic.get(i[0])
            for key,value in dic.items():
                if value == x:
                    dic[key] = y
        else:
            dic[i[0]] = dic.get(i[1])
    else:
        dic[i[0]] = uniqueCircuits
        dic[i[1]] = uniqueCircuits
        uniqueCircuits += 1
    count += 1
    track={}
    for key,value in dic.items():
        if value not in track:
            track[value]=1
        else:
            track[value]+=1
        if track[value] == size:
            print(int(arr[i[0]][0]) * int(arr[i[1]][0]))
            end = True
'''



'''
Part 1
arr = []
with open("adventofcode/D8/day8.txt", "r") as f:
    for line in f:
        line = line.strip()
        arr.append(line.split(','))
dis = []
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        distance = 0
        for k in range(3):
            coorDiff = (int(arr[i][k]) - int(arr[j][k])) ** 2
            distance += coorDiff
        dis.append((i,j,distance))
sortedDis = sorted(dis, key = lambda x: x[2])
count = 0
uniqueCircuits = 0
dic = {}
for i in sortedDis:
    if count >= 1000:
        break
    if dic.get(i[0]) != None:
        x = dic.get(i[0])
        if dic.get(i[1]) != None:
            y = dic.get(i[1])
            for key,value in dic.items():
                if value == x:
                    dic[key] = y
        else:
            dic[i[1]] = dic.get(i[0])
    elif dic.get(i[1]) != None:
        x = dic.get(i[1])
        if dic.get(i[0]) != None:
            y = dic.get(i[0])
            for key,value in dic.items():
                if value == x:
                    dic[key] = y
        else:
            dic[i[0]] = dic.get(i[1])
    else:
        dic[i[0]] = uniqueCircuits
        dic[i[1]] = uniqueCircuits
        uniqueCircuits += 1
    count += 1
track={}
for key,value in dic.items():
    if value not in track:
        track[value]=1
    else:
        track[value]+=1
ansarr = []
for key,value in track.items():
    ansarr.append((key,value))
sortedAns = sorted(ansarr, key = lambda x: x[1], reverse=True)
ans = 1
for i in range(3):
    ans *= sortedAns[i][1]
print(ans)
'''