
uyin_hududi = [
        ['*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', 'xazena']
    ]

def hudud_pint():
    for i in uyin_hududi:
        print(i)

class Anjom:
    pass

class Dori(Anjom):
    def __init__(self,x,y,power):
        self.x=x
        self.y=y
        self.kuchi=power

Asperin=Dori(2,2,10)
uyin_hududi[Asperin.x][Asperin.y]="Dori"

class Qurol(Anjom):
    def __init__(self,x,y,kuchi):
        self.x=x
        self.y=y
        self.kuchi=kuchi
Nayza=Qurol(3,3,15)
uyin_hududi[Nayza.x][Nayza.y]="Qurol"
Avtomat=Qurol(2,3,20)
uyin_hududi[Avtomat.x][Avtomat.y]="Qurol"
Pichoq=Qurol(1,3,10)
uyin_hududi[Pichoq.x][Pichoq.y]="Qurol"

class Dushman:
    def __init__(self,x,y,player_soglig,kuchi):
        self.x=x
        self.y=y
        self.player_soglig=player_soglig    #player_soglig bu o'yinchini sogligini qanchaga kamaytirishi
        self.kuchi=kuchi  #kuchi bu qurol kamaytiradigan Dushmanning uzini kuchi

import random
fx=int(random.random()*4)
fy=int(random.random()*4)
Dushman1=Dushman(fx,fy,20,60)
uyin_hududi[Dushman1.x][Dushman1.y]="Dushman"

class Player:
    def __init__(self,health,x,y,qurollar=[]):
        self.sogligi=health
        self.x=x
        self.y=y
        self.qurollar=qurollar
    def go(self,dx,dy):
        self.x+=dx
        self.y+=dy

        # print(f"uyinchi pastga {dx} birlik masofaga yurdi: ")
        # print(f"uyinchi oldinga {dy} birlik masofaga yurdi: "

        if uyin_hududi[self.x][self.y]=="Dushman":
            if Player1.sogligi>=Dushman1.player_soglig and len(Player1.qurollar)>0:
                self.sogligi-=Dushman1.player_soglig
                print(f"Dushman uyinchi sogligini {Dushman1.player_soglig}  ga kamaytirdi:")
                print(f"Uyinchining quroli dushmanni {Avtomat.kuchi} ga kuchsizlantirdi :")
            else:
                if len(Player1.qurollar)==0:
                    print(" Sizda qurol yuqligi sababli yengildingiz: ")
                    self.x=100
                    return
                elif Player1.sogligi<Dushman1.player_soglig:
                    print(" Sizning sogligingiz yetarli bulmagan sababli yengildingiz:")
                    self.x=100
                    return

        if uyin_hududi[self.x][self.y]=="Qurol":
            Player1.qurollar.append(uyin_hududi[self.x][self.y])
            print(f"    Siz 1 oldingiz, sizgadi qurollar soni {len(Player1.qurollar)} ga teng:")

        if uyin_hududi[self.x][self.y]=="Dori":
            self.sogligi+=Asperin.kuchi
            print(f"Asprin dorisi qabul qilindi va Player sogligi {self.sogligi} buldi: ")

        if uyin_hududi[self.x][self.y] == 'xazena':
            print("Siz marraga yetib keldingiz xazena bilan tabriklaymiz! ")
            self.x=100
            return
        uyin_hududi[self.x][self.y]='p'

Player1=Player(100, 0, 0)
uyin_hududi[Player1.x][Player1.y]= 'p'
hudud_pint()
num=0
while num==0:
    y=int(input("Oldinga va orqagaga yurish 1,-1 yoki 0 : "))
    x = int(input("Pastga va tepaga yurish 1,-1 yoki 0 : "))
    Player1.go(x, y)
    hudud_pint()

    uyin_hududi[Dushman1.x][Dushman1.y]='*'
    fx = int(random.random() * 4)
    fy = int(random.random() * 4)
    Dushman1 = Dushman(fx, fy, 20, 60)
    uyin_hududi[Dushman1.x][Dushman1.y] = "Dushman"

    if Player1.x==100:
        print("  Xayer salomat buling!")
        num=1