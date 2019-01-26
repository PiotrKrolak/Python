# praca z modulem CSV

import csv
from datetime import datetime, date, time

#print(dir(csv)) # wyświetlenie directory modułu żeby zobaczyć jakie metody i klasy zawiera

path = "data.csv"
date_format = "%m/%d/%Y"

file = open(path, newline='') # owarcie pliku csv; newline='' umozliwia miedzyplatformowe otwarcie pliku bez rozjerzdzania
reader = csv.reader(file)

header = next(reader) # wpisuje pierwsza linie do zmiennej naglowki

data = []
for row in reader:
    # tworze listy do ktorych wpisuje wartosci z kolumn
    # rzutuje stringi na odpowiednie typy zmiennych
    # row = [Date, Open, High, Low, Close, Volume, Adk. Close] - tak wygląda linia
    date = datetime.strptime(row[0], date_format)
    open_price = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])

data.append([date, open_price, high, low, close, volume, adj_close]) # dodaje do listy pokoleji listy z zawartoscia poszczegolnych kolumn

print(data[0])
