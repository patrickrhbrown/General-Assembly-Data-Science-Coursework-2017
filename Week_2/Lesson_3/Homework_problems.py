import itertools
import doctest
import numpy as np
from itertools import chain


def sort_rows(mat):
    '''
    INPUT: 2 dimensional list of integers (matrix)
    OUTPUT: 2 dimensional list of integers (matrix)

    Use list comprehension to modify each row of the matrix to be sorted.

    Example:
    >>> M = [[4, 5, 2, 8], [3, 9, 6, 7]]
    >>> sort_rows(M)
    >>> M
    [[2, 4, 5, 8], [3, 6, 7, 9]]
    '''
    pass


def average_rows1(mat):
    '''
    INPUT: 2 dimensional list of integers (matrix)
    OUTPUT: list of floats

    Use list comprehension to take the average of each row in the matrix and
    return it as a list.

    Example:
    >>> average_rows1([[4, 5, 2, 8], [3, 9, 6, 7]])
    [4.75, 6.25]
    '''
    pass


def average_rows2(mat):
    '''
    INPUT: 2 dimensional list of integers (matrix)
    OUTPUT: list of floats

    Use map to take the average of each row in the matrix and
    return it as a list.

    Example:
    >>> average_rows1([[4, 5, 2, 8], [3, 9, 6, 7]])
    [4.75, 6.25]
    '''
    pass


def word_lengths1(phrase):
    '''
    INPUT: string
    OUTPUT: list of integers

    Use list comprehension to find the length of each word in the phrase
    (broken by spaces) and return the values in a list.

    Example:
    >>> word_lengths1("Welcome to Zipfian Academy!")
    [7, 2, 7, 8]
    '''
    pass


def word_lengths2(phrase):
    '''
    INPUT: string
    OUTPUT: list of integers

    Use map to find the length of each word in the phrase
    (broken by spaces) and return the values in a list.

    Example:
    >>> word_lengths2("Welcome to Zipfian Academy!")
    [7, 2, 7, 8]
    '''
    pass


def even_odd1(L):
    '''
    INPUT: list of integers
    OUTPUT: list of strings

    Use list comprehension to return a list of the same length with the strings
    "even" or "odd" depending on whether the element in L is even or odd.

    Example:
    >>> even_odd1([6, 4, 1, 3, 8, 5])
    ['even', 'even', 'odd', 'odd', 'even', 'odd']
    '''
    pass


def even_odd2(L):
    '''
    INPUT: list of integers
    OUTPUT: list of strings

    Use map to return a list of the same length with the strings
    "even" or "odd" depending on whether the element in L is even or odd.

    Example:
    >>> even_odd2([6, 4, 1, 3, 8, 5])
    ['even', 'even', 'odd', 'odd', 'even', 'odd']
    '''
    pass


def shift_on_character(string, char):
    '''
    INPUT: string, string
    OUTPUT: string

    Find the first occurence of the character char and return the string witth
    everything before char moved to the end of the string. If char doesn't
    appear, return the same string.

    This function may use more than one line.

    Example:
    >>> shift_on_character("zipfian", "f")
    'fianzip'
    '''
    pass


def is_palindrome(string):
    '''
    INPUT: string
    OUTPUT: boolean

    Return whether the given string is the same forwards and backwards.

    Example:
    >>> is_palindrome("rats live on no evil star")
    True

    >>> is_palindrome("the moon waxes poetic in sunlight")
    False
    '''
    pass
