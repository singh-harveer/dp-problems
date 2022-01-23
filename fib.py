# Optimize using memoization
def fibanacci(n, memo = {}):
    if n in memo:
        return memo[n]

    if n <=2:
        return 1

    memo[n] = fibanacci(n-1, memo) + fibanacci(n-2, memo)
    
    return memo[n]
