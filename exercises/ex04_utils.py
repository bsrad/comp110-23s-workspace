"""Acheieving functionality using idiomatic Python."""

__author__ = "730487901"

def all(num: list[int], all_int: int) -> bool:
    x: int = 0
    playing = True
    while x < len(num) and playing is True:
        if all_int == num[x]:
            x += 1
        else: 
            playing = False
            x += 1
    return playing

def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    y: int = 0
    z: int = 0
    playing2 = True
    while y < len(input) and z < len(input) and playing2 is True:
        if input[y] > input[z]:
            z += 1
        else:
            y += 1
    return input[z]

def is_equal(equal1: list[int], equal2: list[int]) -> bool:
    xs: int = 0
    playing3 = True
    while xs < len(equal1) and xs < len(equal2) and playing3 is True:
        if equal1[xs] == equal2[xs]:
            xs += 1
        else: 
            playing3 = False
    return playing3

       
        


            
        



        

       
        
            
    



