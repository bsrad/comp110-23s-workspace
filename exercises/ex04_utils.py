"""Acheieving functionality using idiomatic Python."""

__author__ = "730487901"


def all(nums: list[int], all_int: int) -> bool: 
    """Indicate whether or not all ints in list are the same as given int."""
    x: int = 0
    playing = True
    if len(nums) == 0:
        # no empty lists
        playing = False
    while x < len(nums) and playing is True:
        if all_int == nums[x]:
            x += 1
            # incrementing x to check each index of the list
        else: 
            playing = False
            # false if they do not match
            x += 1
    return playing


def max(input: list[int]) -> int: 
    """Find the max int in a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    check_idx: int = 0
    look_idx: int = 0
    playing2 = True
    while check_idx < len(input) and look_idx < len(input) and playing2 is True:
        # variables must be smaller than len of list
        if input[check_idx] > input[look_idx]:
            look_idx += 1
            # incrementing to isolate largest number
        else:
            check_idx += 1
            # number is smaller, move on to next index
    return input[look_idx]


def is_equal(equal1: list[int], equal2: list[int]) -> bool: 
    """Check to see if two lists are exactly equal."""
    idx_check: int = 0
    playing3 = True
    if len(equal1) != len(equal2):
        # lists must be equal in length
        playing3 = False
    while idx_check < len(equal1) and idx_check < len(equal2) and playing3 is True:
        # variables must be smaller than length of list
        if equal1[idx_check] == equal2[idx_check]:
            # each list must be equal at every index, variable can increment the same for both
            idx_check += 1
        else: 
            playing3 = False
    return playing3