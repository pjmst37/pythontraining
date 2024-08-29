my_list = [5, 4, 3]

# print a squared list
print(list(map(lambda item: item ** 2, my_list)))

# list sort
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
# sort based on the 2nd value of the tuple
a.sort(key=lambda item: item[1])
print(a)
