class PartyAnimal:
    def __init__(self, name):
        self.x = 0
        self.name = name
        print(self.name, 'Constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)


# a = PartyAnimal('Elvis')
# a.name
# print(a.party())
