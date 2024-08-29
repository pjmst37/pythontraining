class User():
    def sign_in(self):
        print('Logged in...')


class Wizard(User):
    def __init__(self, name, email, power):
        self.name = name
        self.email = email
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, email, num_arrows):
        self.name = name
        self.email = email
        self.num_arrows = num_arrows

    def attack(self):
        if self.num_arrows > 0:
            print(f'Attacking with arrows ({self.num_arrows})')
        else:
            print('You cannot attack!!  No arrows left!')

        self.num_arrows -= 1

    def run(self):
        print('ran really fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, email, power, arrows):
        Archer.__init__(self, name, email, arrows)
        Wizard.__init__(self, name, email, power)


hb1 = HybridBorg('Locutous', 'resistenceisfutile@outlook.com', 50, 100)
hb1.run()
print(hb1.attack())

wizard1 = Wizard('Merlin',  'merlin@gmail.com', 50,)
print(wizard1.email)
