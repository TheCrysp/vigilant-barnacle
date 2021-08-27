from time import perf_counter

def timer(func):
    i = 1
    def wrapper(*args, **kwargs):
        nonlocal i
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        duration = end - start
        arg = str(*args)
        print(f"{i} {func.__name__} ({arg}) = {result} => {duration:.8f}")
        i = i+1
        return result
    return wrapper
@timer
def fib(n):
    '''return fib of nth'''

    if n<2:
        return n
    else:
        return fib(n-1) + fib(n-2)


fib(15)
