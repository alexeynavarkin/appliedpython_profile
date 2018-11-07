from profile import profile

@profile
def test_simple_load_func(n):
    i = 0
    while i < n:
        i**i
        i += 1

@profile
def test_recursive_func(n):
    if n > 0:
        test_recursive_func(n-1)


test_simple_load_func(10000)
test_recursive_func(10)