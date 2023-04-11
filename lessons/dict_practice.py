"""Practice with dictionaries."""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
ice_cream["mint"] = 3
ice_cream.pop("mint")
print(ice_cream)
