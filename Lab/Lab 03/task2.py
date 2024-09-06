import random


def minmaxAB(state, item, depth, alpha, beta, min_or_max, c):
    if depth == 0:
        return state[item]

    if min_or_max == 1:
        maxeval = float('-inf')
        for child in [2*item+1, 2*item+2]:
            teval = minmaxAB(state, child, depth - 1, alpha, beta, 0, c)
            maxeval = max(maxeval, teval)
            alpha = max(alpha, teval)
            if beta <= alpha:
                break
        return maxeval

    if min_or_max == 0:
        mineval = float('inf')
        maxmagic = float('-inf')
        for child in [2*item+1, 2*item+2]:
            teval = minmaxAB(state, child, depth - 1, alpha, beta, 1, c)
            mineval = min(mineval, teval)
            if c!=-1:
                new = teval-c
                maxmagic = max(new, maxmagic)
                mineval = max(mineval,maxmagic)
            beta = min(beta, mineval)
            if beta <= alpha:
                break
        return mineval
def pacman_game(c:int):
    state = [0,0,0,0,0,0,0,3,6,2,3,7,1,2,0]
    alpha = float('-inf')
    beta = float('inf')
    res = minmaxAB(state, 0, 3, alpha, beta, 1, c)
    print(f"When magic used: {res}")
    res = minmaxAB(state, 0, 3, alpha, beta, 1, -1)
    print(f"When magic not used: {res}")

c = int(input("Enter Cost: "))
pacman_game(c)