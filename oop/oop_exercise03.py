class SuperList(list):

    def __len__(self):
        return 1000


sl = SuperList()
print(len(sl))
sl.append(5)
