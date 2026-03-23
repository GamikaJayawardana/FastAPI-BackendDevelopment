from typing import Callable, Any

# A decorator that accepts a function with specific argument types and return type
def decorator(func: Callable[[int, int], float]):
    pass

# A decorator that accepts a function with specific argument types and return type
def decorator2(func: Callable[[int, int], None]):
    pass

# A more general decorator that can accept any function with any arguments and return type
def decorator3(func: Callable[[Any], Any]):
    pass