# Changemaking problem

The change-making problem raises the question of finding the minimum number of coins that add up to a given sum of money. Though it might seem like a straight-up answer, and in some cases it is, it often gets tricky. It also a special case of the integer Knapsack problem, with applications going beyond just currency.

Suppose we have three coins with the following denominations: [1, 2, 3], and our target amount of money is 10 and suppose we can repeat any denomination more than one time. 

A simple yet inefficient way is to brute-force all the possible combinations of these numbers and see choose the one with least amount of coins. An intuitive and correct solution for the provided coin set is 3 + 3 + 3 + 1 = 10, meaning the minimum amount of coins would be 4. Though this solution did not necessitate any computation, the algorithm by which it was produces was greedy (addition of the largest coint denomination until we approach the sum, and then use the remainder coins to attempt and reach the sum) which does not always produce the most optimal solution (as it relies on individual locally optimal choices).

Suppose we then have a different coin set, namely [11, 5, 13, 7] and the target of 97. The "greedy" approach would be to multiply [13] by as many times untill we are near 97, which would in our case be 13 * 7 = 91. The issue now is that no other combination of coins can be added in order for us to reach our target, hence we are stuck.

It is at this stage that we introduce everyone's favorite programming tool; recursion. Suppose we have a function: 

```
𝑓(𝑛) = 1 + 2 + 3 + ⋯ + 𝑛
```
and a recursive function for this would look like this:

```

int fact(int n)
{
     if (n < = 1) // halting condition
        return 1;
    else
        return n*fact(n-1);
}

```
Now that we have introduced recursive functions, let us move ahead with demonstrating our first approach to the solution, and to demonstrate the recursive function, we will use a small coin set [2,3] and target [6]:
### (Figure 1.) Naive Recursion Tree for coins [2, 3] and target [6] 
<img src="https://i.imgur.com/ccBcX0x.png" alt="Recursive function" align = "middle" />


Though the solution to this might be obvious, computers cannot use intuition. The above recursive tries to find every possible combination (which sometime produces reduntant function calls) and takes then captures the minimum number of coins needed (through a series of comparisons) which is [2]. A larger coin set and target amount would necessitate a lot more of computational power.

A possible way to salvage this issue is to introduce the concept of dynamic programming, where intermediate steps (function calls) are all dynamically allocated to memory, and thus before every function call, the algorithm first detects whether that function call exists in memory. As you might already assume, this can dramatically reduce the computation power that this function takes, as repeating function calls down the recursive tree (amongst different branches) get cut and output is directly provided.

Let us then use complex input choices that will require long computation time and demonstrate the effectiveness of including a dynamic programming algorithm. The Driver.py file, which is used to run the main function and produce the output has these values included, though changing the source code is also possible: coin denomination = [11, 5, 13, 7] and target of 91. The reason behind this choice was that these are all primes and hence are not factors of each other.

<img src="https://i.imgur.com/5pHTuQj.png" alt="Output" align = "middle" />


Our naive recursive approach had needed to preform 1839894 function calls (unique paths) before finding the solution. Our dynamic programming recursive implementation had to only calculate 4 unique function calls (paths) before recycling them and finding the minimum number of solutions (which is 9).

The time of execution showcases slight difference of preformance with dynamic programming if we sort the coin set. It also reveals the drastic difference in computation time of dynamic vs. non-dynamic approach, the former requires half a millisecond while the latter requires 14 seconds (the difference in orders of magnitude is almost 3).


Computers can make millions of calculations per second – it took almost 14 seconds for our non-dynamic approach to come up with an answer. What was even more surprising was the dynamic approach; a simple dictionary system for keeping track of the calculations was enough to significantly decrease the computation time to microseconds.

Hope you have liked reading up on my project. I welcome any suggestions!


