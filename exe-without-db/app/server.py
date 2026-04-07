from typing import Any, Callable
from urllib import response

# Simple routing mechanism for demonstration purposes
routes: dict[str, Callable[[Any], Any]] = {}

# Decorator to register a route
def route(path: str):
    def register_route(func):
        routes[path] = func
        return func
    return register_route

# Example route for shipment information
@route("/shipment")
def get_shipment():
    return "Shipment<1001, in transit>"


request: str = ""

# Simulate a simple command-line server
while request != "quit":
    request = input(">--")
    # Check if the request matches any registered route and call the corresponding function
    if request in routes:
        #response = routes[request]()
        print(response, end="\n\n")
    else:
        print("Not Found", end="\n\n")
