from functools import wraps
def my_deco(func):
    @wraps(func)
    def wrapper():
        print("Some4 Stuff that wraps!!")
        result = func()
        print(result)
        print("Ending Wrapping.......")
        return result
    return wrapper

@my_deco
def pfib():
    return "Fibonacci"

print(pfib.__name__)
