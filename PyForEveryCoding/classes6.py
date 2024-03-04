from classes import PartyAnimal


class CricketFan(PartyAnimal):
    def __init__(self, name):
        super().__init__(name)
        self.points = 0

    def six(self):
        self.points = self.points + 6
        self.party()
        print(self.name, 'points', self.points)


s = PartyAnimal('Sally')
s.party()
j = CricketFan('JimmyBoi')
j.party()
j.six()
j.six()
d = CricketFan('Dan')
d.six()
print(dir(d))
