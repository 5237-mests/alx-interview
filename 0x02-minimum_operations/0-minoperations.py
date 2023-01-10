#!/usr/bin/python3
"""Module for minOP func
"""


def minOperations(n: int) -> int:
    number_of_char_H = 1
    number_of_clipboard = 1
    number_of_operations = 0

    while(number_of_char_H < n):
        number_of_operations += 1     # cp first
        number_of_char_H += number_of_clipboard  # first pasted
        number_of_operations += 1
        if (number_of_char_H == n):
            return number_of_operations

        if(n % number_of_char_H == 0):
            if(number_of_char_H * 2 == n):
                number_of_operations += 1
                number_of_char_H *= 2
                number_of_operations += 1
                return number_of_operations
            else:
                number_of_operations += 1
                number_of_char_H += number_of_clipboard  # second pasted
                number_of_clipboard = number_of_char_H  # second copy inside if
        else:
            number_of_char_H += number_of_clipboard
            number_of_operations += 1
            number_of_clipboard = number_of_char_H  # second copy

    return number_of_operations
