#!/usr/bin/python3
#coding: utf-8

class Tondeuse(object):
    def __init__(self, x,y, o, limitX, limitY):
        '''position de départ et l'ensemble dans lequel elle se place'''
        self.x = x
        self.y = y
        self.o = o
        self.limitX = limitX
        self.limitY = limitY

    def position(self):
        return str(self.x), str(self.y), self.o

    def obeit(self, instruction="A"):
        if instruction == "A":
            self.avance()
        else:
            self.tourne(instruction)
        return self.position()

    def avance(self):
        if self.o == "S" and self.y > 0:
            self.y-=1
        elif self.o == "N" and self.y < self.limitY:
            self.y+=1
        elif self.o == "E" and self.x > 0:
            self.x-=1
        elif self.o == "W" and self.x < self.limitX:
            self.x+=1

        return

    def tourne(self, sens="D"):
        POS = ['N', 'E', 'S', 'W']
        curr_pos = POS.index(self.o)
        if sens == "G":
            #print("Tourne à gauche")
            try:
                self.o = POS[curr_pos+1]
            except IndexError:
                self.o ="N"
        else:
            #print("Tourne à droite")
            try:
                self.o = POS[curr_pos-1]
            except IndexError:
                self.o ="W"
        return self.position()

class Jardin(object):
    def __init__(self, line):
        '''le Jardin est en réalité l'espace où peut s'exprimer la tondeuse
        il faut representer simplement les limites du jardin
        comme les tondeuses sont séquentielles on a pas besoin de remplir
        l'espace de la pelouse et que chaque tondeuse donne sa position
        '''
        #self.pelouse = [[x,y, 0] for x,y in product(range(x),range(y))]
        self.limitX, self.limitY = line.split(" ")

    def installe(self, line):
        '''installons la tondeuse'''
        x,y,o = line.split(" ")
        self.t = Tondeuse(int(x),int(y), o, int(self.limitX), int(self.limitY))
        self.parcours = [(x, y, o)]
        return self.t

    def get_pos(self):
        ''' ou est ma tondeuse?'''
        return " ".join(self.t.position())

    def tond(self, instruction):
        '''execute les mouvements de tonte avancer et tourner'''
        for i in instruction:
            self.t.obeit(i)
            self.parcours.append(self.get_pos())
        return self

def lancer_les_tondeuses(data):
    positions = []
    for i,line in enumerate(data):
        line = line.strip()
        if line != "":
            if i == 0:
                j = Jardin(line)
            elif i % 2 != 0:
                if line in positions:
                    print("Il y a déjà une tondeuse à cette place!")
                else:
                    j.installe(line)
            else:
                #print(line)
                j.tond(line)
                #print (j.parcours)
                positions.append(j.get_pos())
    for p in positions:
        print(p)
    return

def read_file(afile):
    '''execute from a file'''
    with open(afile, "r") as f:
        data = f.read().split("\n")

    lancer_les_tondeuses(data)
    return

def chaining():
    '''execute in cmd by piping it'''
    data = sys.stdin.readlines()
    lancer_les_tondeuses([line.strip() for line in data])
    return

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        afile = sys.argv[-1]
        read_file(afile)
    else:
        chaining()
