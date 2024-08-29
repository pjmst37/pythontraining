# higher order function (hoc)
# Functions that take functions as a parameter (think )

# Decorator
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('**********')
        func(*args, **kwargs)
        print('**********')
    return wrap_func


@my_decorator
def hello(greeting, emoji=';D'):
    print(greeting + ' ' + emoji)


@my_decorator
def bye():
    print('see you later!')


hello('whats up?!')
bye()

# the decorator is basically creating a function to call a function.  hence
# the use of defining the inner function `wrap_func`
#
# This can be written out as:
# a = my_decorator(hello)
# a()
#
# It adds a syntaxtically short-hand for that
