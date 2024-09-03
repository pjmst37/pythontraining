
answ1 = 4/2+2**1
answ2 = 4/2-2**1
answ3 = 1**2-4//3
answ4 = 1//2+3*4

print(answ1)
print(answ2)
print(answ3)
print(answ4)

torque = 5
while torque > 0:
    torque -= 3
    print('*', end='')
else:
    print('*')

print(0 % 2)

angle = 1
# for i in range(2, 5):
#     if i % 2 == 1:
#         angle += 1
# else:
# angle -= 1
for i in range(2, 5):
    if 2 * i > 4:
        angle += 1
    print(f'Angle is now: {angle}')
else:
    print('satisfying the else...')
    angle -= 1


print(angle)

others = 0
for i in range(2):
    print(f'Index: {i}, Outer: {others}')
    for j in range(2):
        if i != j:
            others += 1
        print(f'Index: {j}, Inner: {others}')
else:
    print('Satisfying the else...')
    others += 1

print(others)

tuple1 = (1, 2, 3)
tuple2 = (3, 4, 5)
result = tuple1+tuple2
print(result)

answers = (True, False, True)
selection = answers[2:]
points = 0
for answer in selection[-1:]:
    if answer:
        points += 1
print(points)
