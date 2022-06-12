#Autor: Zbigniew Przybyła
#Program: temperatury

import os
import matplotlib.pyplot as pp

#Stwórz listę z temperaturami do posortowania
temps = []
#Stwórz kopię listy która nie będzie sortowana
tempscpy = []

#Zacznij czytać plik demofile.txt
with open('demofile.txt') as f:
    #Każdy zbiór wartości znajduje się w nowej linice
    for line in f:
        #Przekonwertuj wartości typu string na int
        #Każda wartość oddzielana jest przecinkiem
        day = [int(elt.strip()) for elt in line.split(',')]
        #Dodaj wartości do tablicy
        temps.append(day)

with open('demofile.txt') as f:
    #Każdy zbiór wartości znajduje się w nowej linice
    for line in f:
        #Przekonwertuj wartości typu string na int
        #Każda wartość oddzielana jest przecinkiem
        day = [int(elt.strip()) for elt in line.split(',')]
        #Dodaj wartości do tablicy
        tempscpy.append(day)

#Posortuj tablicę (Gnome Sort)
ti = 0

while ti < len(temps):
    i = 0
    while i < len(temps[ti]):
        if i == 0:
            i += 1
        if temps[ti][i] >= temps[ti][i-1]:
            i += 1
        else:
            temp = temps[ti][i]
            temps[ti][i] = temps[ti][i-1]
            temps[ti][i-1] = temp
            i -= 1
    ti += 1

print(tempscpy)

ti = 0
MAX = temps[0][23]
MIN = temps[0][0]

#Znajdź najmniejsze i największe wartości w posortowanej tablicy
while ti < len(temps):
    if MAX < temps[ti][len(temps)-1]:
        MAX = temps[ti][len(temps)-1]
    if MIN > temps[ti][0]:
        MIN = temps[ti][0]
    ti += 1


ti = 0

#Przeszukaj nieposortowaną tablicę w celu znalezienia pozycji minimalnych i maksymalnych wartośći
while ti < len(temps):
    i = 0
    while i < len(tempscpy[ti]):
        if MIN == tempscpy[ti][i]:
            print("Minimalna temperatura: ", MIN, " odnotowana ", ti+1, " dnia o godzinie ", i+1)
        if MAX == tempscpy[ti][i]:
            print("Maksymalna temperatura: ", MAX, " odnotowana ", ti+1, " dnia o godzinie ", i+1)
        i+=1
    ti += 1

#Pokaż wykres z średnią temperaturą wszystkich dni
Average = []
ti = 0
while ti < len(tempscpy):
    Average.append(sum(tempscpy[ti])/len(tempscpy[ti]))
    ti +=1

print(Average)
rng = range(0,7)
pp.plot(rng, Average)
pp.title("Średnia temperatur w tygodniu")
pp.show()