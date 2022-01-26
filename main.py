from fib import fibanacci
from gird_traveller import gridTraveller, gridTravellerUsingMemoization
from can_sum import can_sum_bruteForce, can_sum_memoization
if __name__=="__main__":
    
    # print(fibanacci(50))
    # grid travellers
    # print(gridTraveller(1,1)) # 1
    # print(gridTraveller(0,1)) # 0
    # print(gridTraveller(1,0)) # 0
    # print(gridTraveller(2,3)) # 3
    # print(gridTraveller(18,18)) 

    # print(gridTravellerUsingMemoization(1,1)) # 1
    # print(gridTravellerUsingMemoization(0,1)) # 0
    # print(gridTravellerUsingMemoization(1,0)) # 0
    # print(gridTravellerUsingMemoization(2,3)) # 3
    # print(gridTravellerUsingMemoization(18,18))

    # print(can_sum_bruteForce(7, [2,3]))
    # print(can_sum_bruteForce(7, [5,3,4,7]))
    # print(can_sum_bruteForce(7, [2,4]))
    # print(can_sum_bruteForce(300, [7,14])) # this will take extra time
    

    print(can_sum_memoization(7, [2,3]))
    print(can_sum_memoization(7, [5,3,4,7]))
    print(can_sum_memoization(7, [2,4]))
    print(can_sum_memoization(300, [7,14])) # thisshould finish quickly after memoization.
    

