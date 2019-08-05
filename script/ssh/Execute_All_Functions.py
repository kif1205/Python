import inspect
import sys


def f1():
    print("f1")


def f2():
    print("f2")


def some_magic(mod):
    all_functions = inspect.getmembers(mod, inspect.isfunction)
    for key, value in all_functions:
        if str(inspect.signature(value)) == "()":
            value()

if __name__ == '__main__':
    some_magic(sys.modules[__name__])