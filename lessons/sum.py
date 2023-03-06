"""Example function for unit tests."""

def sum(xs: list[float]) -> float:
    """return sum of all elements in xs"""
    sum_total: float = 0.0
    for item in xs:
        sum_total += item
    return sum_total