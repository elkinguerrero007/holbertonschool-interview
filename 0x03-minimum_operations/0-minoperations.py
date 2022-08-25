#!/usr/bin/python3
"""
Calculates the minimum operations
"""


def minOperations(n):
    """
    calculates the fewest number of operations needed to result in exactly n
    H characters in the file
    :param n: the number of characters to be printed
    :return: the minimum number of operations
    """
    if type(n) is not int or n < 2:
        return 0
    number = n
    result = 0
    while number % 2 == 0:
        number = number / 2
        result += 2
    for i in range(3, int(number ** (1 / 2)) + 1, 2):
        while number % i == 0:
            result = result + i
            number = number / i
    if number > 2:
        result += number
    return int(result)
