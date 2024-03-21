def minOperations(n):
    if n <= 1:
        return n

    oper = 0
    remaining = n
    clip = 1  # Initial H character

    while remaining > 1:
        if remaining % clip == 0:
            oper += 1
            remaining //= clip  # Update remaining count
        else:
            # If not, copy all and paste
            oper += 2
            clip = remaining

        remaining -= clip

    oper += remaining
    return oper
