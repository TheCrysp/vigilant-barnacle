from functools import update_wrapper, lru_cache

class Count:
    def __init__(self, func) -> None:
        update_wrapper(self,func)
        self.func = func
        self.cnt = 0

    def __call__(self, *args, **kwds):
        self.cnt += 1
        print(f"Current Count: {self.cnt}")
        result = self.func(*args, **kwds)
        return result
@lru_cache(maxsize=None)
@Count
def fib(n):
    if n<2:
        return n
    else:
        return fib(n-1) + fib(n-2)

fib(10)
