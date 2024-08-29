# Exercise Cats Everywhere

# Given the below class:

class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age
# SCROLL FOR ANSWERS


# 1 Instantiate the Cat object with 3 cats.
cat1 = Cat('Mr Whiskers', 3)
cat2 = Cat('Jezebel', 12)
cat3 = Cat('Tom', 6)

# 2 Create a function that finds the oldest cat.


def find_oldest_cat(cats):
    return max(cats)


oldest_cat_age = find_oldest_cat([cat1.age, cat2.age, cat3.age])
# 3 Print out: "The oldest cat is x years old.".
print(f'The old cat is {oldest_cat_age} years old')
# x will be the oldest cat age by using the function in #2
