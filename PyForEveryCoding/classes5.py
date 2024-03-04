class PartyAnimal:
    def __init__(self, name):
        self.x = 0
        self.n = name
        print(self.n, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.n, 'party count', self.x)

    def __del__(self):
        print(self.n, 'I am destructed', self.x)


s = PartyAnimal('Sally')
d = PartyAnimal('Dan')
j = PartyAnimal('JimmyBoi')
d.party()
j.party()
j.party()
s.party()
j.party()
d.party()
s.party()
