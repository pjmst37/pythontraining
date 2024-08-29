# functions
# map
# filter
# zip
# reduce
# lambda


from functools import reduce

# lambda param: function(param)  lambda param: action(param)

my_list = [1, 2, 3]


def multiply_by(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)

    return new_list


def mult2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


def accumalator(acc, item):
    print(acc, item)
    return acc + item


print(list(map(mult2, my_list)))
print(list(map(lambda item: item*2, my_list)))
print(list(filter(only_odd, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(accumalator, my_list, 0))
print(reduce(lambda acc, item: acc + item, my_list))
