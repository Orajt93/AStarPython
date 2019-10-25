import os
import math
import operator
import copy

mapOrigin = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0],
             [5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0],
             [0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 5, 0, 0],
             [0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 5, 5, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 5, 0, 5, 5, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 5, 0, 5, 5, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 5, 0, 5, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5],
             [0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [5, 5, 5, 5, 5, 5, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#stworzenie kopii tabliy
workArea = copy.deepcopy(mapOrigin)

#deklaraja listy pól
fields = []


#Sprawdzenie czy zawiera się w zakresie tablicy
def check(x,y):
    if((x<0) or (x>19) or (y<0) or (y>19)):
        return False
    else:
        return True

#Definicja funkcji zwracającej pole o podanych współrzędnych x,y
def findField(x,y):
    for a in fields:
        if((a.x == x) and (a.y == y)):
           return a

#Deklaracja klasy
class Field():
    x = 0
    y = 0
    Rodzic = None
    Heurystyka = 0.0
    KosztDotarcia = 0
    Moc = 0.0
    KiedyDodany = 0

    def __init__(self,x,y,Rodzic,kolejnosc):
        self.x = x
        self.y = y
        if(Rodzic != None):
            self.KosztDotarcia = Rodzic.KosztDotarcia + 1
            self.Rodzic = Rodzic
            self.Heurystyka = math.sqrt((19-x)**2+(0-y)**2)
            self.Moc = self.Heurystyka + self.KosztDotarcia
            self.KiedyDodany = kolejnosc
        else:
            self.Moc=1000000
            self.KosztDotarcia=0

    def toString(self):
        return "x {} y{}".format(self.x,self.y)
    

#Główna funkcja latająca po polach
def workWithFields(fieldToCheck):
    tempx=fieldToCheck.x
    tempy=fieldToCheck.y
    workArea[tempx][tempy] = 2
    fields.remove(fieldToCheck)
    tempField = None
    if((check(tempx,tempy-1)) and (workArea[tempx][tempy-1] != 5) and (workArea[tempx][tempy-1] != 2)):
        if(workArea[tempx][tempy-1] == 1):
            tempField = findField(tempx,tempy-1)
            if(tempField.Rodzic.KosztDotarcia >= fieldToCheck.KosztDotarcia):
                findField(tempx,tempy-1).Rodzic = fieldToCheck
                findField(tempx,tempy-1).KosztDotarcia = fieldToCheck.KosztDotarcia + 1
        else:
            fields.append(Field(tempx,tempy-1,fieldToCheck,(len(fields)+1)))
            workArea[tempx][tempy-1] = 1;
    if((check(tempx,tempy+1)) and (workArea[tempx][tempy+1] != 5) and (workArea[tempx][tempy+1] != 2)):
        if(workArea[tempx][tempy+1] == 1):
            tempField = findField(tempx,tempy+1)
            if(tempField.Rodzic.KosztDotarcia >= fieldToCheck.KosztDotarcia):
                findField(tempx,tempy+1).Rodzic = fieldToCheck
                findField(tempx,tempy+1).KosztDotarcia = fieldToCheck.KosztDotarcia + 1
        else:
            fields.append(Field(tempx,tempy+1,fieldToCheck,(len(fields)+1)))
            workArea[tempx][tempy+1] = 1;
    if((check(tempx-1,tempy)) and (workArea[tempx-1][tempy] != 5) and (workArea[tempx-1][tempy] != 2)):
        if(workArea[tempx-1][tempy] == 1):
            tempField = findField(tempx-1,tempy)
            if(tempField.Rodzic.KosztDotarcia >= fieldToCheck.KosztDotarcia):
                findField(tempx-1,tempy).Rodzic = fieldToCheck
                findField(tempx-1,tempy).KosztDotarcia = fieldToCheck.KosztDotarcia + 1
        else:
            fields.append(Field(tempx-1,tempy,fieldToCheck,len(fields)+1))
            workArea[tempx-1][tempy] = 1;
    if((check(tempx+1,tempy)) and (workArea[tempx+1][tempy] != 5) and (workArea[tempx+1][tempy] != 2)):
        if(workArea[tempx+1][tempy] == 1):
            tempField = findField(tempx+1,tempy)
            if(tempField.Rodzic.KosztDotarcia >= fieldToCheck.KosztDotarcia):
                findField(tempx+1,tempy).Rodzic = fieldToCheck
                findField(tempx+1,tempy).KosztDotarcia = fieldToCheck.KosztDotarcia + 1
        else:
            fields.append(Field(tempx+1,tempy,fieldToCheck,len(fields)+1))
            workArea[tempx+1][tempy] = 1;

#utworzenie pola startowego
firstField = Field(0,19,None,0)
fields.append(firstField)
checkField = fields[0]

#status 1 - odwiedzone
#status 2 - zamkniete
workArea[0][19] = 1;
find=0
while((checkField.x != 19) or (checkField.y != 0)):
    find=0
    fields.sort(key=operator.attrgetter('Moc','KiedyDodany'))
    for z in fields:
        if(workArea[z.x][z.y]==1):
            find=1
            workWithFields(z)
            checkField = z
            break
        if(workArea[z.x][z.y]==2):
            fields.remove(z)
    if(find==0):
        break
print("Mapa odwiedzonych miejsc:")
print()
for i in workArea:
    print(" ".join(str(i)))
if(find==1):
    print()
    print("Najlepsza możliwa droga")
    print()
    while(checkField.Rodzic != None):
        mapOrigin[checkField.x][checkField.y]=3
        checkField=checkField.Rodzic
    mapOrigin[19][0] = 3;
    for i in mapOrigin:
        print(" ".join(str(i)))

else:
    print("Te je nie do przejścia")





