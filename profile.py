from time import time
from functools import wraps
from types import FunctionType


def profile_class(klass):
    for attr_name in klass.__dict__:
        attr = getattr(klass, attr_name)
        if callable(attr):
            attr = profile_function(attr, class_name=klass.__name__)
            setattr(klass, attr_name, attr)
    return klass


def profile_function(method, class_name=None):
    @wraps(method)
    def wrapper(*args,**kwargs):
        if class_name:
            print(f"`{class_name}`.", end="")
        print(f"`{method.__name__}` started")
        t_start = time()
        result = method(*args, **kwargs)
        t_stop = time()
        if class_name:
            print(f"`{class_name}`.", end="")
        print(f"`{method.__name__}` finished in {round(t_stop - t_start, 2)}s")
        return result
    return wrapper


def profile(obj):
    if isinstance(obj, FunctionType):
        obj = profile_function(obj)
    elif isinstance(obj, type):
        obj = profile_class(obj)
    return obj
