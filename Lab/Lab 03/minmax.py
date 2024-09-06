
def minmax(state:list, depth, min_or_max):
    if depth==0 or state==None:
        if min_or_max==1:
            return float('-inf')
        else:
            return float('inf')
    
    if min_or_max==1: # maximizing turn
        maxeval = float('-inf')
        for child in state:
            teval = minmax(child, depth-1, -1) # now each child is a new state, since choosing 1 so depth decreasing, it was already max node so sending -1
            maxeval = max(maxeval,teval)
        return maxeval

    if min_or_max==-1: # minimizing turn
        mineval = float('inf')
        for child in state:
            teval = minmax(child, depth-1, 1) # since it's a min node so sending 1 so the next one is max node
            mineval = min(mineval, teval)
        return mineval
    

