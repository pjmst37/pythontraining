# Error handling

while True:
    try:
        age = int(input('What is your age? '))
        10/age
        raise ValueError
    except ValueError:
        print('Please enter a valid number')
        continue
    except ZeroDivisionError:
        print('Please enter age higher than 0 (zero)')
        break
    else:
        print('Thank you old timer!')
    finally:
        print('Ok, I\'m finally done!')
    print('can you hear me?')


# def sum(num1, num2):
#     try:
#         return num1 + num2
#     except (TypeError, ZeroDivisionError) as err:
#         print(err)


# print(sum('1', 2))
