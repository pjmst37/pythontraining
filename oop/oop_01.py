class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def name(self):
        return self._name

    def age(self):
        return self._age

    def shout(self):
        print(f'My name is {self._name}!')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Luther', num1 + num2)

    @staticmethod
    def adding_mult_things(*values):
        return sum(values)

    def run(self):
        print(f'Run {self._name}!!')

    def speak(self):
        print(f'My name is {self._name}, and I am {self._age} years old.')


player1 = PlayerCharacter('Jethro', 34)
print(player1.name())
print(player1.age())

player1.run()

print(player1.adding_things(5, 2))
print(player1.speak())
