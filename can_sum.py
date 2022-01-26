"""
bruteforce version
TC:- O(n^m)
SC :- O(m)
n = length of array
m = sum
"""
def can_sum_bruteForce(sum, arr):
    if sum == 0:
        return True
    if sum < 0:
        return False

    for num in arr:
        if can_sum_bruteForce(sum-num, arr):
            return True
    
    return False

"""
optimized version
TC:- O()
n = length of array
m = sum
"""
def can_sum_memoization(target_sum, arr, memo = {}):
    if target_sum in memo:
        return memo[target_sum]
    
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for num in arr:
        if can_sum_memoization(target_sum-num, arr, memo):
            memo[target_sum] = True
            return True

    memo[target_sum] = False

    return False
