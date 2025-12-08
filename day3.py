'''
Part 2
with open("adventofcode/D3/day3.txt", "r") as f:
    ans = 0
    for line in f:
        line = line.strip()
    # DP solution (O(2^n)) (don't use this)
    #     length = len(line)
    #     maxJoltage = 0
    #     dp = [[] for _ in range(length)]
    #     for i in range(length):
    #         if i == 0:
    #             dp[i].append(int(line[i]))
    #         else:
    #             dp[i] = dp[i-1][:]
    #             for j in dp[i-1]:
    #                 if j < 10 ** 11:
    #                     dp[i].append(j*10+int(line[i]))
    #             dp[i].append(int(line[i]))
    #     # print(dp)
    #     for i in dp[length-1]:
    #             if i > maxJoltage:
    #                 maxJoltage = i
    #     print(maxJoltage)
    #     ans += maxJoltage
    # print(ans)
        length = len(line)
        startPos = 0
        joltage = ''
        for x in range(11,-1,-1):
            largestDigit = -1
            for i in range(startPos,length-x):
                if int(line[i]) > largestDigit:
                    largestDigit = int(line[i])
                    j = i
            startPos = j+1
            joltage += str(largestDigit)
        joltage = int(joltage)
        ans += joltage
    print(ans)
'''

'''
Part 1
with open("adventofcode/D3/day3.txt", "r") as f:
    ans = 0
    for line in f:
        line = line.strip()
        length = len(line)
        maxJoltage = 0
        for i in range(length-1):
            for j in range(i+1,length):
                joltage = 10 * int(line[i]) + int(line[j])
                if joltage > maxJoltage:
                    maxJoltage = joltage
        ans += maxJoltage
    print(ans)
'''