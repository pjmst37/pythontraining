numbers = [4, 3, 2, 1]

print(numbers[3:22])

the_data = [0, .0, True]

print(the_data.index(True))


answers = (True, True, False)
selection = answers[3:]
print(selection)
print(selection[-2:])
points = 0
for answer in selection[-2:]:
    if answer:
        points += 1

print(points)
