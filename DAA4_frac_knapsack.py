"""
The Knapsack Problem is an optimization problem in which we are given a bag with a fixed capacity and multiple items having different weights and values.Our objective is to select items to maximize the total value without exceeding the capacity of the bag

"""

n = int(input("Enter number of items: "))

weight = []
profit = []
ratio = []

# Accept weight and profit of each item
for i in range(n):
    w = float(input("Enter weight: "))
    p = float(input("Enter profit: "))

    weight.append(w)
    profit.append(p)

    # Calculate profit/weight ratio
    ratio.append(p / w)

capacity = float(input("Enter knapsack capacity: "))

# Sort items according to ratio in descending order
for i in range(n):
    for j in range(i + 1, n):

        if ratio[i] < ratio[j]:

            # Swap ratios
            ratio[i], ratio[j] = ratio[j], ratio[i]

            # Swap corresponding weights
            weight[i], weight[j] = weight[j], weight[i]

            # Swap corresponding profits
            profit[i], profit[j] = profit[j], profit[i]

# Calculate maximum profit
total_profit = 0

for i in range(n):

    # If complete item fits in knapsack
    if weight[i] <= capacity:
        total_profit += profit[i]
        capacity -= weight[i]

    # If only a fraction of item fits
    else:
        total_profit += ratio[i] * capacity
        capacity = 0
        break

# Display maximum profit
print("Maximum Profit:", total_profit)
