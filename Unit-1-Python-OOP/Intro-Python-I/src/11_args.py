# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.


def f1(x, y):
    """ Takes two integer positional arguments and returns
    the sum. This is what you'd consider to be a regular, normal function.

    x, y - int
    """
    result = x+y

    return result


print(f1(1, 2))

# Write a function f2 that takes any number of integer arguments and returns the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"


def f2(*args):
    result = sum([sum(arg) if type(arg) is list else arg for arg in args])

    return result


print(f2(1))                    # Should print 1
print(f2(1, 3))                 # Should print 4
print(f2(1, 4, -12))            # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

a = [7, 6, 5, 4]

# How do you have to modify the f2 call below to make this work?
print(f2(a))    # Should print 22
print(f2(a, a))

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.


def f3(a, b=1):
    """ Accepts either one or two arguments. If one argument,
    it returns that value plus 1. If two arguments, it returns the sum of the
    arguments.

    a - int
    b - int, 1 by default
    """
    result = a+b
    
    return result

print(f3(1, 2))  # Should print 3
print(f3(8))     # Should print 9


# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Note: Google "python keyword arguments".

def f4(**kwargs):
    for key, value in kwargs.items():
        print(f"key: {key}, value: {value}")

# Should print
# key: a, value: 12
# key: b, value: 30
f4(a=12, b=30)

# Should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
f4(city="Berkeley", population=121240, founded="March 23, 1868")

d = {
    "monster": "goblin",
    "hp": 3
}

# How do you have to modify the f4 call below to make this work?
f4(monster=d['monster'], hp=d['hp'])