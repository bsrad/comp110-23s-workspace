def my_max(a: int, b: int) -> int:
    """Return the max number"""
    if a > b:
        return a
    else:
        return b

max: int = my_max(1,10)
print(my_max(1,100)*max)