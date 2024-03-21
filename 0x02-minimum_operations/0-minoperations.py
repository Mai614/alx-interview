#!/usr/bin/python3
"""
Main file for testing
"""

# Importing the minOperations function from the 0-minoperations module
minOperations = __import__('0-minoperations').minOperations

# Testing the minOperations function with n = 4
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

# Testing the minOperations function with n = 12
n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
