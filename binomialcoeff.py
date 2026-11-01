"""
Dynamic Programming (DP) is an algorithm design technique that solves complex problems by breaking them into smaller overlapping subproblems and storing their results to avoid repeated calculations.

It is particularly useful when a problem has:
1. Overlapping Subproblems: The same subproblems are solved multiple times.
2. Optimal Substructure: The solution to a larger problem can be constructed using solutions to smaller subproblems.

What are Binomial Coefficients?
Binomial coefficients represent the number of ways to select r objects from n objects without considering the order.


It is represented as:

ⁿCᵣ or C(n, r)

Formula:

C(n, r) = n! / [r! × (n-r)!]

Example:

C(5, 2) = 5! / (2! × 3!) = 10

"""


def binomial_coefficients(n):

    # Create DP table
    dp = [[0 for j in range(n + 1)] for i in range(n + 1)]

    # Generate binomial coefficients
    for i in range(n + 1):

        for j in range(i + 1):

            if j == 0 or j == i:
                dp[i][j] = 1

            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    # Display binomial coefficients
    print("\nBinomial Coefficients:")

    for i in range(n + 1):

        for j in range(i + 1):
            print(dp[i][j], end=" ")

        print()


# Main Program
print("===== Binomial Coefficients using DP =====")

n = int(input("Enter the number of rows: "))

binomial_coefficients(n)
