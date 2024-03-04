class PartyAnimal:
    def __init__(self):
        self.x = 0

    def party(self):
        self.x = self.x + 1
        print('So far %s' % self.x)


an = PartyAnimal()
an.party()
an.party()
an.party()
an.party()
