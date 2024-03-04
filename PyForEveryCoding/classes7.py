from classes import PartyAnimal


class FooBallFan(PartyAnimal):
    def __init__(self, name):
        super().__init__(name)
        self.points = 0

    def goal(self, points):
        self.points = points * (2 - self.points) + 1
        self.party()
        print(self.name, 'points', self.points)
        return self.number_goals(self.points)

    def number_goals(self, win):
        self.win = win
        for w in self.name:
            if w in 'JimmyBoi':
                self.name = w
                print(self.name, 'Wins', self.win)
        return self.win


s = PartyAnimal('Sally')
s.party()
j = FooBallFan('JimmyBoi')
j.party()
j.goal(1*2)
# print(dir(j))
