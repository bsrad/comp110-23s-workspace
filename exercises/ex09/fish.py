"""File to define Fish class."""


class Fish:
    """Fish."""

    age: int

    def __init__(self):
        """Init."""
        self.age = 0
        return None
    
    def one_day(self):
        """One day."""
        self.age += 1
        return None