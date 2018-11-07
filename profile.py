from time import time
from functools import wraps

def profile(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print(f"Started {func.__name__}")
        t_start = time()
        result = func(*args, **kwargs)
        t_stop = time()
        print(f"Finished {func.__name__}, execution time: {t_stop - t_start}")
        return result
    return wrap
