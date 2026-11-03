"""
The Knapsack Problem is an optimization problem in which we are given a bag with a fixed capacity and multiple items having different weights and values.Our objective is to select items to maximize the total value without exceeding the capacity of the bag
The special thing about Fractional Knapsack is:

You are allowed to take fractions (parts) of an item.

This is the special part of Fractional Knapsack.

If the entire item cannot fit, we take only the fraction that fits.

The additional profit is: RATIO*REMAINING_CAPACITY

Then:
- Capacity becomes zero.
- break stops the loop because the bag is full.

"""

n = int(input("Enter number of items: ")) #n stores the total number of items.

weight = [] #weight stores the weight of every item.
profit = [] #profit stores the profit of every item.
ratio = [] #ratio stores the profit-to-weight ratio.

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
#We are sorting items in descending order of their profit-to-weight ratio.
for i in range(n):
    for j in range(i + 1, n):

        if ratio[i] < ratio[j]: #If the current item's ratio is smaller than the next item's ratio, swap them.

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
    if weight[i] <= capacity: #If the item's weight is less than or equal to the remaining capacity, we take the entire item.
        total_profit += profit[i] #Add the item's complete profit.
        capacity -= weight[i] #Reduce the remaining capacity by its weight.

    # If only a fraction of item fits
    else:
        total_profit += ratio[i] * capacity
        capacity = 0
        break

# Display maximum profit
print("Maximum Profit:", total_profit)


"""
10. Why is this called a Greedy Algorithm?
Because at every step, we select the item that gives the maximum profit per unit of weight.

We don't consider all possible combinations.

Instead, we:
1. Calculate profit/weight ratio.
2. Select the item with the highest ratio.
3. Take as much as possible.
4. Move to the next item.
This is a locally optimal choice that gives an optimal solution for Fractional Knapsack.
"""
