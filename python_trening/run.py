import time
import _datetime
import lib
import os


#Hello World*******************************************************************************************************
x = 10
print(x)
print(type(x))
print(x, end="") #end jest argumentem funkcji print, domyslnie po princie przechodzimy odo nowej lini(\n), endem definiujemy jak ma się zakonczyc linia, w tym wypadku nie przechodzic do nowej lini.


print("\n\n\n")
#typy zmiennych****************************************************************************************************
x+=5/2.5
print(x)
print(type(x))


print("\n\n\n")
#ciagi znakow******************************************************************************************************
x="ciag"
print(x)
print(type(x))
x+=" znakow"
print(x)


print("\n\n\n")
#wprowadzanie znaków**********************************************************************************************
#x=input()
print(x)
print(type(x))


print("\n\n\n")
#konwersja typów zmiennych******************************************************************************************
x=3
print(x)
print(type(x))

x=float(x)
print(x)
print(type(x))

x=str(x)
print(x)
print(type(x))


print("\n\n\n")
#dzialania na ciagach znakow*****************************************************************************************
x = "Ala ma kota, a kot ma Ale"
print(x)
print(x[0])
print(x[0:3]) #nie wlicza sie 3 wyraz ciagu
print(x[:3]) #to samo co wyzej, domyslnie od wyrazu 0
print(x[0:-3]) #ucinam trzy ostatnie znaki
print(x[-5]) #odczytuje piaty znak od konca

#instrukcje warunkowe************
#x = input()
#x = int(x)
x = 15
if x == 10:
    print("OK")
if x != 15:
    print("NIE 15")
if x <= 5:
    print("Male")
else:
    print("nie zdefiniowano")

x = 5 < 6
if x:
    print("TRUE")
else:
    print("FALSE")


print("\n\n\n")
#listy, tuple i slowniki*****************************************************************************************
#lista
produkty = ["ser","mleko","platki","mniam"]
print(produkty)
print(type(produkty))

print(produkty[0])
print(produkty[-1])

produkty.append("platki")
print(produkty)

x = produkty.count("platki")
print(x)


produkty.remove("ser")
print(produkty)

produkty.pop(2)
print(produkty)
print(type(produkty))

#tuple - nie mozna edytowac jak listy(innych roznic brak)
produkty = ("ser","mleko","platki","mniam")
print(produkty)
print(type(produkty))

#slowniki
osoba = {"wiek": 27,"imie": "Piotr","nazwisko": "Krolak"}
print(osoba)

print(osoba["imie"])
print(osoba["nazwisko"])
print(osoba["wiek"])

keys = osoba.keys()
wartosci = osoba.values()
items = osoba.items()
print(keys)
print(wartosci)
print(items)


print("\n\n\n")
#Petla While******************************************************************************************************
x = 10
while x:
    print("X = ",x)
    x-=1


print("\n\n\n")
#Petla FOR*********************************************************************************************************
literki = ["a","b","c","d","e"]

for i in literki:
    print(i)

for i in range(5,50,5): #range(od,do,krok)
    print(i)

#enumerate, format, break********
francuskie = ["Camir", "Panel8", "GKP"]

for pozycja_na_liscie, devices in enumerate(francuskie):
    print(pozycja_na_liscie)
    print(devices)

print("GO!")
for devices in francuskie:
    print(devices)
    if devices == "Panel8":
        break
print("END!")

#na dole, metoda format zastepuje swoimi argumettami nawiasy klamrowe w slowie formatowanym
x = "{} dobry, {} !!!".format("Dzien", "SWIECIE")
print(x)

for i in francuskie:
    print("Sprawdzam: {}".format(i))
    if i != i:
        print("Brak produktu!")
    print("{} Sprawny!".format(i))


#Pomijanie iteracji**************
#brake - przerywa np pętlę
#continue - przeskakujemy do następnej iteracji(w petlach)

x=francuskie
x.append("Ptr")
x.reverse()
print(x)

print("FOR:")
for i in francuskie:
    if i == "Ptr":
        print("Pomijam krok: 'Ptr'")
        continue
    if i == "Camir":
        break
    print(i)
print("Koniec FOR'a")


print("\n\n\n")
#Operatory logiczne*************************************************************************************************
# and, or, not

print(francuskie)
if "GKP" in francuskie:
    print("Znaleziono!")
else:
    print("Nie Znaleziono!")

#liczba = int(input())
liczba = 21
if liczba >= 20 and liczba <= 50:
    if liczba == 20 or liczba == 50:
        print("BORDER")
    else:
        print("TRUE")
else:
    print("FALS")
if liczba != 20 and liczba != 50:
    print(liczba)
if not "heh" in francuskie: # jeżeli nie ma "heh" w liscie francuskie(nie ma) to:
    print("heh")
if not 6 == 6: #false - neguje wynik wiec jeszeli 6 == 6 to true ale negacja tego to false!
    print("TRUE")
else:
    print("FALSE")


print("\n\n\n")
#data i czas*******************************************************************************************************
#najpierw trzeba zaimportować biblioteke "time", to na samej gorze w 1 linijce!

#print("Start")
#time.sleep(1)
#print("Stop")

x = time.time() # zwraca ilosc sekund od 1 stycznia 1970
print(x)
#time.sleep(1)
x = time.time() - x
print(x)

#trzeba zaimportowac teraz biblioteke "datetime" zeby wyciagnac ktora jest godzina czy data
teraz = _datetime.datetime.now()
print(teraz)
print(teraz.strftime("%H:%M %d.%m.%Y")) # %H:%M %d.%m.%Y = hour : minuts days.mounght.year


print("\n\n\n")
#Funkcje************************************************************************************************************

def printme(liczba):
    x = "Test: " #input()
    print(x, end = "")
    print(liczba)

printme(5)
printme(10)
printme(15)


def mnozenie( pierwsza, druga):
    x = pierwsza * druga
    print(x)

mnozenie(2,5)


def dodaj(a,b):
    return a+b

print(dodaj(3,4))


def dzielenie(a,b):
    return a/b

wynik = dzielenie(3,4)
print(wynik)
wynik = dzielenie(b=4,a=3) # podaje tutaj argumenty w dowolnej polejnosci
print(wynik)


def odejmij(a,b=0): #jezeli tu definiuje b = 0 to znaczy ze jezeli nie wpisze argumentu b podcas wywolania to funkcja przyjmie argument b = 0
    return a-b

wynik = odejmij(7,4)
print(wynik)
wynik = odejmij(7) #nie podalem argumentu b, ale w definicji funkcij podalem jaka ma w takim razie przyjac wartosc domyslna(b=0
print(wynik)


print("\n\n\n")
#Moje moduly(biblioteki), import, from, as**************************************************************************
#podminamy na górze modol(lib) na samej gorze

lib.test("Hello World !")
lib.make_fun(4)

#można zaimportować sama funkcje i wywolac ja jak bylaby dodana w tym pliku - jak ponizej
from lib import make_fun#, test
#("Hello World!")
make_fun(5)

#moge tez zaimportowac wszystkie funkcje z pliku lib, jak ponizej
from lib import * #gwaizdka oznacza że wszystko importujemy
test("Hello World!")

#jezeli mam taka samoa nazwe funkcji w pliku main i lib to moge zaimportowac funkcje pod inna nazwa - jak ponizej
from lib import make_fun as heh
heh(2)


print("\n\n\n")
#obsluga plikow - tryby write, read*********************************************************************************

f = open("tekst.txt","a+")
f.write("zapis \n")
f.close()

f = open("tekst.txt","r")
print(f.read(7))
print(f.readline())
print(f.readline()) # tu odczytuje juz druga linie bo kursor po pierwszym urzyciu ustawil sie na poczaatku 2 lini

#ponizej funkcja zwypisuje CALY plik w formie listy!!!
print(f.readlines())

#for line in f.readlines():
#   print(line.rstrip()) #line.rstrip ta metoda wypisze nam całą linijke ale bez białych znaków!

f.close()

lib.odczyt() #zobacz w pliku lib.py


print("\n\n\n")
#Modul os, tworzenie plikow, listy plikow***************************************************************************
#import modolu "os" na gorze pliku!

print("lista plikow z katalogu: D:\Python_projekty")

lista = os.listdir("D:\Python_projekty")
print(lista)

for item in lista:
    if os.path.isfile(item): # jeżeli item jest plikiem
        print("{} jest plikiem".format(item))
    if os.path.isdir(item):
        print("{} jest folderem".format(item))

#os.mkdir("testowy folder") #tworzenie pliku
#os.rename("test.txt", "tekst.txt") # zmiana nazwy pliku pierwszego na drogi
#os.remove("tekst.txt") # usuniecie pliku
#os.rmdir("testowy folder") # usuwanie folderu!


path = "pliki/01/dane.txt"

print(path)
print("\n")

print(os.path.dirname(path)) # wypisuje wszystko do ostatniego ukośnika
print(os.path.basename(path)) # wypisuje wszystko przed ostatnim ukosnikiem
print(os.path.abspath(path)) # wypisuje absolutny path czyli jak mam w folderze to tez to co domyslnie jest nad D...


print("\n\n\n")
#Wyjatki - Exceptions************************************************************************************************
