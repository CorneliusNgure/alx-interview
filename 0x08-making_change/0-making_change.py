#!/usr/bin/python3
"""Module solving the making change problem"""


def makeChange(coins, total):
    """
    Determine fewest number of coins needed to meet a given total.

    Args:
        coins (list): List of the values of coins available.
        total (int): The target amount.

    Returns:
        int: The fewest number of coins needed to meet the total,
             or -1 if the total cannot be met.
    """
    if total <= 0:
        return 0

    # Initialize a DP array where dp[i] is the fewest coins to make value i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make total of 0

    # Loop through each coin and update dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, total cannot be formed
    return dp[total] if dp[total] != float('inf') else -1
