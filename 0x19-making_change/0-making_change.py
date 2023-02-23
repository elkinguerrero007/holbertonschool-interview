#!/usr/bin/python3
"""
Funtion makeChange(coins, total) should be
implemented in the file 0-making_change.py
"""


def makeChange(coins, total):
    """
    Further instructions in the 0x19-making_change directory
    Arguments:
        - coins is a list of the values of the coins in your possession
        - total is the total amount of money to make change for
    Returns:
        - fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            change += 1
    return change if total == 0 else -1
