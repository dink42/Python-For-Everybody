class PartyAnimal:
    def __init__(self):
        self.x = 0

    def party(self):
        self.x = self.x + 1
        print('So far %s' % self.x)


an = PartyAnimal()
print('Type %s' % type(an))
print('Dir %s' % dir(an))
print('Type %s' % type(an.x))
print('Type %s' % type(an.party))
