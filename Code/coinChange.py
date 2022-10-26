def coinChange(coins, amount):
    """return the minimum amount of coins needed for the sum (amount), the operation order
       and the number of possible solutions"""

    result = []

    def solve(coins, target, curr_path):
        """a recursive function that solves for the minimum coins needed and stores all viable paths
        (those that successfully lead to the target amount)"""
        minCoins = float("inf")  # a reference point; it is always infinite until a solution is found
        nonlocal result

        if target == 0:
            result.append(curr_path) # upon reaching a viable recursive descent (a solution), append the path to results
            return 0                 # a 0 means a solution was found, hence will help increment the minCoins

        for c in coins:              # we try every possible combination recursively, i.e. through brute-force
            if target - c >= 0:      # if condition is met, we descend further into the recursive tree
                # coin in question is subtracted from the already decreasing target until we reach 0 (or not)
                numOfCoins = solve(coins, target - c, curr_path + str(c) + "+") + 1
                # if a better solution exists, numOfCoins will always be less than min, which is infinite, or worse than
                # other viable solutions)
                minCoins = min(minCoins, numOfCoins)

        return minCoins

    minCoinsFinal = solve(coins, amount, "")  # once the most optimal solution is found (or not), we return it
    if minCoinsFinal == float("inf"):         # if no solution is found
        return -1                             # a -1 is returned
    else:
        # the second return argument finds the shortest path in our result list, and returns it
        return minCoinsFinal, min(result, key=len), len(result) # the second return argument
