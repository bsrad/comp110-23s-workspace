"""Continue building list utility functions."""

__author__ = "730487901"


def only_evens(input: list[int]) -> list:
    """Given a list, return only even ints into a new list."""
    output: list[int] = list()
    for num in input:
        if num % 2 == 0:
            output.append(num)
    return output


def concat(list1: list[int], list2: list[int]) -> list:
    """Concatenate two lists into a new list."""
    concatput: list[int] = list()
    for char in list1:
        concatput.append(char)
    for digit in list2:
        concatput.append(digit)
    return concatput


def sub(a_list: list[int], start: int, end: int) -> list:
    """Given a list and a range, subset a new list between the range."""
    subput: list[int] = list()
    if start < 0:
        start = 0
    if end > len(a_list):
        end = len(a_list)
    for space in range(start, end):
        subput.append(a_list[space])
    if len(a_list) == 0 or start >= len(a_list) or end <= 0:
        subput = list()
    return subput