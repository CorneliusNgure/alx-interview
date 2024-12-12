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
    # sort the coins in descending order
    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        change += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return change
