#modoly(biblioteki)

def test(tekst):
    print("Test: ", end="")
    print(tekst)

def make_fun(heh):
    int(heh)
    for i in range(heh):
        print("heh")

def odczyt():
    f = open("tekst.txt", "r")

    for linia in f.readlines():
        print(linia.rstrip()) # metoda rstrip wypisuje całą linię ale bez znaków białych

    f.close()

