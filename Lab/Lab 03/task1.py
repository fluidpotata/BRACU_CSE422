import random

def minmaxAB(depth, alpha, beta, min_or_max):
    if depth == 0:
        return random.choice([-1,1])

    if min_or_max == 1:
        maxeval = float('-inf')
        for child in range(2):
            teval = minmaxAB(depth - 1, alpha, beta, 0)
            maxeval = max(maxeval, teval)
            alpha = max(alpha, teval)
            if beta <= alpha:
                break
        return maxeval

    if min_or_max == 0:
        mineval = float('inf')
        for child in range(2):
            teval = minmaxAB(depth - 1, alpha, beta, 1)
            mineval = min(mineval, teval)
            beta = min(beta, teval)
            if beta <= alpha:
                break
        return mineval

inp = int(input('┌── Who starts first?\n|   "0" for Scorpion\n|   "1" for Sub Zero\n└─> '))
alpha = float('-inf')
beta = float('inf')
result = []
depth = random.randint(0,5)
for i in range(3):
    result.append(minmaxAB(depth, alpha, beta, inp))
    print(depth)
    if inp==0:
        inp=1
    elif inp==1:
        inp=0
res = 0
for i in result:
    res += i

data = {1:"Sub-Zero", -1:"Scorpion"}

if res>0:
    res = 1
else:
    res = -1

print(f"""Game Winner: {data[res]}
Total Rounds Played: 3
Winner of Round 1: {data[result[0]]}
Winner of Round 2: {data[result[1]]}
Winner of Round 3: {data[result[2]]}
""")