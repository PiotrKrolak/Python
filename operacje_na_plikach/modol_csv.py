# praca z modulem CSV

import csv
from datetime import datetime # dodanie modulu czasu zeby ustawic typ zmiennej czas jako czas

#print(dir(csv)) # wyświetlenie directory modułu żeby zobaczyć jakie metody i klasy zawiera

path = "data.csv"

file = open(path, newline='') # owarcie pliku csv; newline='' umozliwia miedzyplatformowe otwarcie pliku bez rozjerzdzania
reader = csv.reader(file)

naglowki = next(reader) # wpisuje pierwsza linie do zmiennej naglowki


#wpisanie lini do listy w jednej linijce
dane = [linia for linia in reader] # do listy(tablicy) dane wpisuje linia po lini informacje

print(naglowki)
print(dane[0:4]) # drukuje piec linii danych
