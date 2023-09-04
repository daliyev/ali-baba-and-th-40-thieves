import random

maydon = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
]
maydon[9][9] = "X"


class Player:
    def __init__(self, jon, qurol, dx, dy):
        self.jon = jon
        self.qurol = qurol
        self.dx = dx
        self.dy = dy

    def set_joylashuv(self):
        y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        x = [0, 1, 2, 3]
        self.dx = random.choice(x)
        self.dy = random.choice(y)

    def get_joylashuv(self):
        joyi = [0, 0]
        joyi[0] = self.dx
        joyi[1] = self.dy
        return joyi

    def update_joylashuv(self, a, b):
        maydon[self.dx][self.dy] = "."
        self.dy += a
        self.dx += b

    def jon(self):
        return self.jon

    def set_qurol(self,kuch):
        self.qurol = kuch

    def get_qurol(self):
        return self.qurol


class Dushman(Player):
    def __init__(self, jon, qurol, dx, dy):
        super().__init__(jon, qurol, dx, dy)

    def set_joylashuv(self):
        y = [4, 5, 6, 7, 8, 9]
        x = [4, 5, 6, 7, 8, 9]
        self.dx = random.choice(x)
        self.dy = random.choice(y)
        while self.dx == 9 and self.dy == 9:
            y = [6, 7, 8, 9]
            x = [6, 7, 8, 9]
            self.dx = random.choice(x)
            self.dy = random.choice(y)

    def set_jon(self):
        self.jon = random.randint(10, 60)

    def set_qurol(self):
        self.qurol = random.randint(10, 60)
    def get_qurol(self):
        return self.qurol

    def update_joylashuv(self):
        maydon[self.dx][self.dy] = "."

class QurolAnjomlar:
    def __init__(self,plus,minus,dx,dy):
        self.plus = plus
        self.minus = minus
        self.dx = dx
        self.dy = dy

    def get_plus(self):
        return self.plus

    def get_minus(self):
        return self.minus

    def set_joylashuv(self):
        y = [4, 5, 6, 7, 8, 9]
        x = [4, 5, 6, 7, 8, 9]
        self.dx = random.choice(x)
        self.dy = random.choice(y)
        while self.dx == 9 and self.dy == 9:
            y = [6, 7, 8, 9]
            x = [6, 7, 8, 9]
            self.dx = random.choice(x)
            self.dy = random.choice(y)

    def get_joylashuv(self):
        joyi = [0, 0]
        joyi[0] = self.dx
        joyi[1] = self.dy
        return joyi

    def update_joylashuv(self):
        maydon[self.dx][self.dy] = "."

def chiz():
    j = p1.get_joylashuv()
    dj = d1.get_joylashuv()
    dori_j = dori.get_joylashuv()
    maydon[dori_j[0]][dori_j[1]] = "+"
    maydon[dj[0]][dj[1]] = "D"
    maydon[j[0]][j[1]] = "P"
    if j[0]==dj[0] and j[1]==dj[1]:
        p1.jon -= d1.qurol
        d1.jon -= p1.qurol
        if p1.jon <= 0:
            p1.jon = 0
        if d1.jon <= 0:
            d1.jon = 0
    for i in range(10):
        for j in range(10):
            print(maydon[i][j], end="    ")
        print("\n")
    print(f"Player joni: {p1.jon}            Dushman joni: {d1.jon}")
    print(f"Player qurol kuchi: {p1.qurol}     Dushman zarba kuchi: {d1.qurol}")
    print(" ")


qilich = QurolAnjomlar(0,10,0,0)
dori = QurolAnjomlar(15,0,0,0)
p1 = Player(10, qilich.get_minus(), 0, 0)
d1 = Dushman(0, 0, 0, 0)


p1.set_joylashuv()
d1.set_joylashuv()
d1.set_jon()
d1.set_qurol()
qilich.set_joylashuv()
dori.set_joylashuv()

def yutdikmi():
    dj = p1.get_joylashuv()
    if maydon[dj[0]] == 9 and maydon[dj[1]] == 9:
        d1.set_joylashuv()
    j = p1.get_joylashuv()
    return j[0] == 9 and j[1] == 9


# def jang():


chiz()
while True:
    yurish = int(input("Yuring( <4/6>  v2/8^ ) > "))
    yurishlar = [2, 4, 6, 8]
    while yurish not in yurishlar:
        print("Xato yurish! Qayta kiriting.")
        yurish = int(input("Yuring( <4/6>  v2/8^ ) > "))

    if yurish == 4:
        if p1.jon <= 0:
            print("Afsus yutqazdingiz!")
            break
        d1.update_joylashuv()
        d1.set_joylashuv()
        p1.update_joylashuv(-1, 0)
        if yutdikmi() == 1:
            print("Yutdingiz! Tamom.")
            break
        chiz()
    elif yurish == 6:
        if p1.jon <= 0:
            print("Afsus yutqazdingiz!")
            break
        d1.update_joylashuv()
        d1.set_joylashuv()
        p1.update_joylashuv(1, 0)
        if yutdikmi() == 1:
            print("Yutdingiz! Tamom.")
            break
        chiz()
    elif yurish == 2:
        if p1.jon <= 0:
            print("Afsus yutqazdingiz!")
            break
        d1.update_joylashuv()
        d1.set_joylashuv()
        p1.update_joylashuv(0, 1)
        if yutdikmi() == 1:
            print("Yutdingiz! Tamom.")
            break
        chiz()
    elif yurish == 8:
        if p1.jon <= 0:
            print("Afsus yutqazdingiz!")
            break
        d1.update_joylashuv()
        d1.set_joylashuv()
        p1.update_joylashuv(0, -1)
        if yutdikmi() == 1:
            print("Yutdingiz! Tamom.")
            break
        chiz()