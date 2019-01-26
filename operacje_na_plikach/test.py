txt = "data.txt"
csv = "data.csv"

#operacje na plikach tekstowych

tekst = open(csv).read()
#print(tekst)

linie = [row for row in open(csv)] # wpisuje do listy pojedyncze linie z pliku
#print(linie[41]) #wypisuje pojedyncza linie czytanego dokumentu

# rozdzielenie wyrazow w lini
dataset = linie[5].strip().split(',')   # strip() - pozbywa sieznakow bialych np. konca lini
print(dataset)                          # split(',') - rozbija linie rozpoznajac separator ','
                                        # problemm jest taki ze to dalej sa stringi
