# Author: Kimberly Rojas
# GitHub username: kimberlyroj
# Date: 2/3/2022
# Description: A recursive function named multiply that takes two positive integers as parameteters and returns the product of those two numbers (the result from multiplying them together).

def multiply(integer1, integer2):
    """Returns the multiple of integer2 and integer2"""
    if(integer1 == 0):
        return 0
    else:
        return integer2+multiply(integer1-1,integer2)
