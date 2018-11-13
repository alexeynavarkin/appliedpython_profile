from time import time
from functools import wraps
from types import FunctionType


def profile_class(klass):
    for attr_name in klass.__dict__:
        attr = getattr(klass, attr_name)
        if callable(attr):
            attr = profile_method(attr)
            setattr(klass, attr_name, attr)
    return klass


def profile_method(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        print(f"`{type(self).__name__}.{method.__name__}` started")
        t_start = time()
        result = method(self, *args, **kwargs)
        t_stop = time()
        print(f"`{type(self).__name__}.{method.__name__}` finished in {round(t_stop - t_start, 2)}s")
        return result
    return wrapper


def profile_function(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f"`{func.__name__}` started")
        t_start = time()
        result = func(self, *args, **kwargs)
        t_stop = time()
        print(f"`{func.__name__}` finished in {round(t_stop - t_start, 2)}s")
        return result
    return wrapper


def profile(obj):
    if isinstance(obj, FunctionType):
        obj = profile_function(obj)
    elif isinstance(obj, type):
        obj = profile_class(obj)
    return obj
