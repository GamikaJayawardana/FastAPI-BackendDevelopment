
def fence(func):
    def wrapper():
        print("++++++++++")
        func()
        print("+" * 10)
    return wrapper

# Using the decorator
@fence
def log():
    print("decorated!")

log()