def gridTraveller(m, n):
    if m ==1 and n == 1:
        return 1
    
    if m == 0  or n == 0:
        return 0
    
    return gridTraveller(m-1, n) +  gridTraveller(m, n-1)


def gridTravellerUsingMemoization(m, n, memo = {}):
    key = str(m) + "," + str(n)

    if key in memo:
        return memo[key]
    elif m ==1 and n == 1:
        return 1
    elif m == 0  or n == 0:
        return 0
    
    memo[key] = gridTravellerUsingMemoization(m-1, n) +  gridTravellerUsingMemoization(m, n-1)
    
    return memo[key]

"""
point to remember for DP problems.
1- Make it work.
    Visulize problem as tree.
    Implement tree as recursions.
    Test it.

2- Then Make it efficient.
    Add memo object.
    Add base case to return memo values.
    Store return value into memo

 
"""
