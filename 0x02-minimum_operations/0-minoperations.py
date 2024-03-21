#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n: int) -> int:
    """
    Minimum Operations needed to get n H characters

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The minimum number of operations needed to obtain n H characters,
             or 0 if it's impossible to achieve.
    """
    if n <= 1:
        return n  # If n is 0 or 1, no operations needed

    op = 0
    clipboard = 1  # Initial H character
    body = 1  # Initial H character

    while body < n:
        if n % body == 0:
            op += 2  # Copy All and Paste
            clipboard = body  # Update clipboard to current body
            body += clipboard  # Paste the current body
        else:
            op += 1  # Only Paste
            body += clipboard  # Paste the clipboard

    if body != n:
        return 0  # Impossible to achieve n H characters
    return op
