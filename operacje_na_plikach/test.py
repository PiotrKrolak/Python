import csv

txt = "data.txt"
csv = "data.csv"

#operacje na plikach tekstowych

tekst = open(csv).read()
#print(tekst)

linie = [row for row in open(csv)] # wpisuje do listy pojedyncze linie z pliku
print(linie[0]) #wypisuje pojedyncza linie czytanego dokumentu


#operacja na csvfile
"""
with open(tekst, 'r') as csvfile:
    # deklarujemy nasz *czytacz*
    # parametr *delimiter* jest opcjonalny i wskazuje jaki został w pliku użyty separator
    csvreader = csv.reader(csvfile, delimiter=',')
"""
