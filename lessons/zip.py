"""Challenge question 4."""

def zip(list1: list = [str], list2: list = [int]) -> dict[str, int]:
    dict_return: dict[str, int] = {}
    x: int = 0
    while x < len(list1) and len(list1) == len(list2):
        dict_return[list1[x]] = list2[x]
        x += 1
    return dict_return
