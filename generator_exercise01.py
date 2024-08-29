# Fibonaci Generator

'''
Number is the index value of the Fibonaci sequence
'''


def fib(num):
    first_value = 0
    next_value = 1
    for i in range(num+1):
        yield first_value
        temp = first_value
        first_value = next_value
        next_value = temp + next_value


for i in fib(5):
    print(i)
