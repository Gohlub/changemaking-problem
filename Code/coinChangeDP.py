def coinChangeDP(coins, amount):
    """return the minimum amount of coins needed for the sum (amount), the operation order
       and the number of possible solutions using a dynamic programming approach (faster)"""
    result = []

    def solve(coins, target, curr_path, dp):
        """a dynamic recursive function that solves for the minimum coins needed and stores some of the viable paths
           (until it starts calculating with already computed values)"""
        minCoins = float("inf")  # a reference point; it is always infinite until a solution is found
        nonlocal result

        if target == 0:
            result.append(curr_path) # upon reaching a viable recursive descent (a solution), append the path to results
            return 0                 # a 0 means a solution was found, hence will help increment the minCoins

        key = str(target) + "separator"  # helps avoid collisions; 1 1 and 11 could compute the same hash value

        if key in dp:               # check for the recursive tree branch, if it exists, it skips going further
                                    # and simply returns the completed calculation
            return dp[key][0]

        for c in coins:             # we try every possible combination recursively, though our dictionary
                                    # allows us to use already computed tree branches in our calculations
            if target - c >= 0:     # if condition is met, we descend further into the recursive tree
                # coin in question is subtracted from the already decreasing target until we reach 0 (or not)
                numOfCoins = solve(coins, target - c, curr_path + str(c) + " + ", dp) + 1
                # if a better solution exists, numOfCoins will always be less than min, which is infinite, or worse than
                # other viable solutions)
                minCoins = min(minCoins, numOfCoins)

        dp[key] = (minCoins, curr_path) # here, we just add the solution and recursive path to the dictionary
        return minCoins

    minCoinsFinal = solve(coins, amount, "", dict())
    if minCoinsFinal == float("inf"):                # here we just test if there is a solution
        return -1                                    # if not, we return -1
    else:
        return minCoinsFinal, len(result)
