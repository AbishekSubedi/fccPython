"""
This module provides a function to compute the power of a base raised to an exponent
using a recursive approach.

The function `pingala_power` uses the divide-and-conquer method to compute the power
efficiently. If the exponent is even, it recursively computes the power of half the
exponent and squares the result. If the exponent is odd, it multiplies the base with
the square of the power of half the exponent.
"""

def pingala_power(base, exponent):
    """
    Computes the power of a base raised to an exponent using a recursive approach.

    This function uses the divide-and-conquer method to compute the power efficiently.
    If the exponent is even, it recursively computes the power of half the exponent
    and squares the result. If the exponent is odd, it multiplies the base with the
    square of the power of half the exponent.

    Parameters:
    base (int or float): The base number.
    exponent (int): The exponent to which the base is raised. Must be a non-negative integer.

    Returns:
    int or float: The result of base raised to the power of exponent.
    """
    if exponent == 0:
        return 1
    aux = pingala_power(base, exponent // 2)
    if exponent % 2 == 0:
        return aux * aux
    return base * aux * aux

print(pingala_power(2, 10))
