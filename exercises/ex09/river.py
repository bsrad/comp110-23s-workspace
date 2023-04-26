"""File to define River class."""

__author__ = "730487901"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """River."""

    day: int
    bears: list
    fish: list

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Check ages."""
        survived_fish: list[str] = []
        survived_bear: list[str] = []
        for fish in self.fish:
            if fish.age <= 3:
                survived_fish.append(fish)
        self.fish = survived_fish
        for bear in self.bears:
            if bear.age <= 5:
                survived_bear.append(bear)
        self.bear = survived_bear
        return None

    def bears_eating(self):
        """Bear eating."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Check hunger."""
        surviving_bears: list = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None
        
    def repopulate_fish(self):
        """Repopulate fish."""
        for x in self.fish:
            x: int = (len(self.fish) // 2) * 4
            self.fish.append(x)
        return None

    def repopulate_bears(self):
        """Repopulate bears."""
        x: int = len(self.bears) // 2
        self.bears.append(x)
        return None

    def remove_fish(self, amount: int):
        """Remove fish."""
        x: int = 0
        while x < amount:
            self.fish.pop(x)
            x += 1

    def view_river(self):
        """View river."""
        x: int = self.day
        y: int = len(self.fish)
        z: int = len(self.bears)
        print(f"~~~ Day: {x} ~~~")
        print(f"Fish population: {y}")
        print(f"Bear population: {z}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """One river week."""
        x: int = 0
        while x < 7:
            self.one_river_day()
            x += 1