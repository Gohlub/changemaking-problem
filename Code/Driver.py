from coinChange import coinChange
from coinChangeDP import coinChangeDP
import time

def BubbleSort(array, length):
    """return a sorted array using Bubble sort given the unsorted array and length of the array"""
    for m in range(length):
        for n in range(0, length - m - 1):  # last n elements (the largest ones) have already been changed,
                                            # so we reduce the pointer by one
            if array[n] > array[n + 1]:
                array[n], array[n + 1] = array[n + 1], array[n]  # so when condition is met, we just swap the values
    return array


def format_path(coins, amount, algorithm):
    """return the solved path (coins used) of the algorithm"""
    result = algorithm(coins, amount)
    min_coins, path, solutions = result
    path_1 = path.split("+")     # we just create an array out of the path string
    del path_1[-1]               # the last index is empty so we get rid of it
    path_2 = " + ".join(path_1)  # and we just create another string
    return min_coins, path_2, solutions


def timetaken(coins, amount, algorithm):
    """return the execution of an algorithm with 14 decimal digits"""
    dblStart = time.process_time()
    algorithm(coins, amount)
    intTime = "%.14f" % ((time.process_time() - dblStart))
    return intTime


def solutions(coins, amount):
    """return the solutions tabularly"""
    output_recursive = format_path(coins, amount, coinChange)
    print(f" The target amount is: {amount}")
    print(
        f" Recursive           : Coins = {coins},        Minimum number of coins needed = {output_recursive[0]}, Solution = {output_recursive[1]}, Unique paths taken = {output_recursive[2]}")
    output_recursiveDP = coinChangeDP(coins, amount)
    print(
        f" Recursive (DP)      : Coins = {coins},        Minimum number of coins needed = {output_recursiveDP[0]}, Solution = {output_recursive[1]}, Unique paths taken (DP) = {output_recursiveDP[1]}")
    sorted_coins = BubbleSort(coins, len(coins))
    output_recursiveDPSort = coinChangeDP(sorted_coins, amount)
    print(
        f" Recursive (DP sort) : Coins = {sorted_coins},       Minimum number of coins needed = {output_recursiveDPSort[0]},  Solution = {output_recursive[1]}, Unique paths taken (DP sort) = {output_recursiveDPSort[1]}")
    print("")
    print(f" Times taken for execution:")
    print(f" Recursion:                 {timetaken(coins, amount, coinChange)}")
    print(f" Recursion DP:              {timetaken(coins, amount, coinChangeDP)}")
    print(f" Recursion DP with sorting: {timetaken(sorted_coins, amount, coinChangeDP)}")


def main():
    coins = [11, 5, 13, 7]
    amount = 97
    solutions(coins, amount)


if __name__ == '__main__':
    main()
