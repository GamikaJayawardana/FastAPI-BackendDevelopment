# Type hints in Python
text: str = "Hello, World!"
pert: int = 90
temp: float = 36.6

# Union type hints allow a variable to be of multiple types 
number: int | float = 12

#argument and return type hints 
def root(num: int | float) -> float:
    return pow(num, 0.5)

root_25: float = root(25)
print(f"The square root of 25 is {root_25}")

# Optional type hints indicate that a variable can be of a specific type or None
optional: str | None = None

# A function with an optional argument
def root_exp(num: int | float, exp: float | None) -> float:
    if exp is None:
        exp = 0.5
    return pow(num, exp)


# Using type hints with collections
digits: list[int] = [1, 2, 3, 4, 5]
table_5: tuple[int, ...] = (5, 10, 15)
city_temp: tuple[str, float] = ("New York", 22.5)  
shipment: dict[str, int] = {
    "apples": 10,
    "oranges": 20
    }

class City:
    def __init__(self, name, location):
        self.name = name
        self.location = location

hampshire = City("Hampshire", "UK")


