# list set dictionary
# list comprehensions


# This is a list or set comprehension here .. swap out the `{}` with `[]`
# for list comprehension

my_list = {char for char in 'hello'}
my_list2 = {num for num in range(0, 100)}
my_list3 = {num**2 for num in range(0, 100)}

# for char in 'hellloo':
#     my_list.append(char)

my_list4 = {num for num in my_list3 if num % 2 == 0}


print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

simple_dict = {
    'a': 1,
    'b': 2
}

# Dictionary comprehension
my_dict = {
    key: value**2 for key, value in simple_dict.items() if value % 2 == 0
}

my_dict2 = {
    num: num*2 for num in [1, 2, 3]
}

print(my_dict)
print(my_dict2)
