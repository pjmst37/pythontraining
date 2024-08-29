# Useful modules

from collections import Counter, defaultdict, OrderedDict

# Creates a dictionary on how many times each instances occurs
li = [1, 2, 3, 4, 5, 6, 7, 2]
print(Counter(li))

sentence = 'the quick brown fox jumps over the lazy dog'
print(Counter(sentence))

dictionary = defaultdict(lambda: 'value does not exist', {'a': 1, 'b': 2, })
# defaultdict returns a default value if an element doesn't exist
print(dictionary['c'])

# OrderedDict retains the order that you insert into a dictionary
d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d2 == d1)


d3 = {'c': 100}
d3['a'] = 1
d3['b'] = 2

d4 = {'c': 100}
d4['b'] = 2
d4['a'] = 1

print(d4 == d3)
