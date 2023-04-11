"""Testing the utility functions from ex05."""

__author__ = "730487901"


from exercises.ex05.utils import only_evens, concat, sub


def test_evens() -> None:
    """Returning only the even ints."""
    test_list: list[int] = [4, 7, 6]
    assert only_evens(test_list) == [4, 6]


def test_all_even() -> None:
    """All ints are even, returning the even ints."""
    test_list: list[int] = [10, 10, 10]
    assert only_evens(test_list) == [10, 10, 10]


def test_empty_evens() -> None:
    """List is empty."""
    test_list: list[int] = ()
    assert only_evens(test_list) == []
    

def test_concat() -> None:
    """Concatenating two lists."""
    test_list: list[int] = [1, 2, 3, 4]
    test_list1: list[int] = [5, 6, 7, 8]
    assert concat(test_list, test_list1) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_concat1() -> None:
    """Concatenating two lists."""
    test_list: list[int] = [20, 40, 60]
    test_list1: list[int] = [60, 40, 20]
    assert concat(test_list, test_list1) == [20, 40, 60, 60, 40, 20]


def test_empty_concat() -> None:
    """One list is empty."""
    test_list: list[int] = [50, 100, 50]
    test_list1: list[int] = ()
    assert concat(test_list, test_list1) == [50, 100, 50]


def test_sub() -> None:
    """Subset of given list with range."""
    test_list: list[int] = [10, 20, 30, 40]
    start: int = 1
    end: int = 3
    assert sub(test_list, start, end) == [20, 30]


def test_negative() -> None:
    """Start index is negative, start from beginning of list."""
    test_list: list[int] = [5, 10, 15, 20]
    start: int = -1
    end: int = 2
    assert sub(test_list, start, end) == [5, 10]


def test_empty_sub() -> None:
    """List is empty."""
    test_list: list[int] = ()
    start: int = 2
    end: int = 3
    assert sub(test_list, start, end) == []