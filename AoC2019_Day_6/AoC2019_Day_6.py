import pathlib;

def getInput():
    with open(str(pathlib.PurePath("C:/Users/Public", "AoC2019_D6_input.txt")), 'r') as f:
        x = f.readlines()

    for i in range(0, (len(x) - 1)):
        x[i] = x[i][:-1]

    return x


class Planet(object):
    
    def __init__(self, planet):
        self.name = planet
        self.drctOrbt = []
        self.indrctOrbt = []

    def getName(self):
        return self.name

    def addDirOrbit(self, orb):
        self.drctOrbt.append(orb)

    def addIndirOrbit(self, orb):
        self.indrctOrbt.append(orb)

def loadPlanets(orbits):
    planets = []
    flag = True
    for o in orbits:
        x = o.split(')')

        for p in planets:
            if(x[0] == p.getName()):
                p.addDirOrbit(x[1])
                flag = False

        if(flag):
            planet = Planet(x[0])
            planet.addDirOrbit(x[1])
            planets.append(planet)

        flag = True

    return planets

def findIndirectOrbits(planets, orbits):

    for p in planets:
        for d in p.drctOrbt:
            for p2 in planets:
                if(d == p2.name):
                    for i in p2.drctOrbt:
                        p.indrctOrbt.append(i)

    for p in planets:
        indirNum = len(p.indrctOrbt)
        updNum = 0
        while(indirNum != updNum):
            counter = 0
            indirNum = len(p.indrctOrbt)
            updNum = len(p.indrctOrbt)
            for i in p.indrctOrbt:
                for p2 in planets:
                    if(i == p2.getName()):
                        for dir in p2.drctOrbt:
                            if(dir not in p.indrctOrbt):
                                p.indrctOrbt.append(dir)
                                counter += 1
                        for dir in p2.indrctOrbt:
                            if(dir not in p.indrctOrbt):
                                p.indrctOrbt.append(dir)
                                counter += 1

            updNum += counter


    return planets

def planetLine(planets, you, destination):
    plntNum = 0
    youList = [you]
    sanList = [destination]

    dirNum = len(youList)
    updNum = 0
    while(dirNum != updNum):
        counter = 0
        dirNum = len(youList)
        updNum = len(youList)
        for p in planets:
            for d in p.drctOrbt:
                if(youList[len(youList) - 1] == d):
                    youList.append(p.getName())
                    counter += 1
        updNum += counter

    dirNum = len(sanList)
    updNum = 0
    while(dirNum != updNum):
        counter = 0
        dirNum = len(sanList)
        updNum = len(sanList)
        for p in planets:
            for d in p.drctOrbt:
                if(sanList[len(sanList) - 1] == d):
                    sanList.append(p.getName())
                    counter += 1
        updNum += counter

    frstDupFlag = True
    tempY = 0
    tempS = 0
    for y in range(0, len(youList)):
        for s in range(0, len(sanList)):
            if(youList[y] == sanList[s]):
                if(frstDupFlag):
                    tempY = y
                    tempS = s
                    frstDupFlag = False

    youList = youList[0:tempY]
    sanList = sanList[0:tempS]

    plntNum = len(youList) + len(sanList) - 2

    return plntNum

x = getInput()
"""x = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L"]"""
orbits = 0
jumps = 0

planets = []

planets = loadPlanets(x)
# planets = findIndirectOrbits(planets, x)
jumps = planetLine(planets, "YOU", "SAN")

for p in planets:
    orbits += len(p.drctOrbt)
    orbits += len(p.indrctOrbt)

'''
for p in planets:
    statement = ""
    statement += p.getName() + ":"
    for i in p.drctOrbt:
        statement += " " + i

    statement += ":"
    for i in p.indrctOrbt:
        statement += " " + i

    print (statement)
'''

print ("# of Orbits: %s" % (orbits))
print ("# of jumps: %s" % jumps)