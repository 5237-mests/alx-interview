#!/usr/bin/python3
"""Module
"""


def isprime(n):
    """prime num"""
    if n > 1:
        for x in range(2, int(n**0.5) + 1):
            if n % x == 0:
                return False
        return True
    return False


def isWinner(x, nums):
    """prime winner"""
    if type(nums) is not list:
        return None
    if x > len(nums):
        return None
    primel = [1]
    mx = max(nums)
    for i in range(mx + 1):
        if isprime(i):
            primel.append(i)
    # print(primel, 'prime lists')  # prime nums

    Maria = 0
    Ben = 0

    for k in range(x):
        playnum = nums[k]
        if playnum == 1:
            Ben += 1
        else:
            each = []
            for numin in primel:
                if numin <= playnum:
                    each.append(numin)
            # print(each, 'for each num of list for', playnum)
            Bentmp = 0
            Mariatmp = 0
            if len(each) % 2 == 0:
                Mariatmp += 1
            if len(each) % 2 == 1:
                Bentmp += 1

            if Mariatmp > Bentmp:
                Maria += 1
            elif Mariatmp == Bentmp:
                Maria += 0
                Ben += 0
            else:
                Ben += 1
    if Maria == Ben:
        return None
    return 'Maria' if Maria > Ben else 'Ben'
