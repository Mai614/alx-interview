#!/usr/bin/python3
""" Minimum Operations
    """


def minOperations(n: int) -> int:
    """ Minimum Operations needed to get n H characters """
    if n <= 1:
        return n  # If n is 0 or 1, no operations needed

    op = 0
    clipboard = 'H'
    body = 'H'

    while len(body) < n:
        if n % len(body) == 0:
            op += 2  # Copy All and Paste
            clipboard = body  # Update clipboard to current body
            body += clipboard  # Paste the current body
        else:
            op += 1  # Only Paste
            body += clipboard  # Paste the clipboard

    if len(body) != n:
        return 0  # Impossible to achieve n H characters
    return op
