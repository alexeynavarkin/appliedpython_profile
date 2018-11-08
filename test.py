from profile import profile

@profile
class TestClass():
    def __init__(self):
        pass

    def test_simple_load_func(self, n):
        i = 0
        while i < n:
            i ** i
            i += 1

    def test_recursive_func(self, n):
        if n > 0:
            self.test_recursive_func(n - 1)


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


test_simple_load_func(1000)
test_recursive_func(5)

t = TestClass()
t.test_simple_load_func(1000)
t.test_recursive_func(5)