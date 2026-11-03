"""The 0/1 Knapsack problem is an optimization problem in which we select items to maximize profit without exceeding the capacity of the knapsack.

Each item has:
- Weight
- Value / Profit
In this problem, we have only two choices:
- 1 → Select the complete item.
- 0 → Do not select the item.
We cannot take fractions of an item.
"""


"""
Dynamic Programming Strategy:
1. Create a DP array to store maximum profit.
2. Initially, all values are zero.
3. Consider each item one by one.
4. Check whether the item can fit into the current capacity.
5. If it fits, compare taking and not taking the item.
6. Store the maximum profit.
"""


# 0/1 Knapsack using Dynamic Programming
n = int(input("Enter number of items: "))

weight = []
profit = []

# Accept item weights and profits
for i in range(n):
    w = int(input("Enter weight: "))
    p = int(input("Enter profit: "))

    weight.append(w)
    profit.append(p)

capacity = int(input("Enter knapsack capacity: "))



"""
Dynamic Programming is a technique that breaks a problem into smaller subproblems, solves them, and stores their results to avoid repeated calculations.

Here, we create a 2D table to store the maximum profit for different combinations of items and capacities.

Why 2D?

Because we need to track two things:
- Rows → Number of items considered.
- Columns → Available knapsack capacity.
"""

# Create DP table initialized with 0
dp = [[0 for j in range(capacity + 1)]
      for i in range(n + 1)]

# Fill the DP table
for i in range(1, n + 1):

    for j in range(1, capacity + 1):

        # If item weight is less than or equal to capacity
        if weight[i - 1] <= j:

            # Maximum of including or excluding the item
            dp[i][j] = max(
                profit[i - 1] + dp[i - 1][j - weight[i - 1]],
                dp[i - 1][j]
            )

        else:
            # Exclude the item
            dp[i][j] = dp[i - 1][j]

# Display maximum profit
print("\nMaximum Profit:", dp[n][capacity])