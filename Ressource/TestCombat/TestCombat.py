class Player:
    def __init__(self, name):
        self.pv = 50
        self.name = name
    def play(self):
        print(self.name + ' play')
    def defense(self):
        self.pv -= 5

def fight(listPlayers):
    listPlayers[0].play()
    listPlayers[1].defense()
    for i in listPlayers:
        if i.pv <= 0:
            return
    j = listPlayers.pop(0)
    listPlayers.append(j)
    fight(listPlayers)

players = [Player('1'), Player('2')]
fight(players)
print('End of fight')