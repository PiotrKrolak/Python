# sortowanie

# help(list.sort)
# help(sorted) - mozna tak utworzyc posortowana tuple

kluby = ["Lechia", "Lech", "Jagielonia", "Miedz", "Legia"]

print(kluby)

kluby.sort()
print(kluby)

kluby.sort(reverse = True)
print(kluby)


liczby = [4, 2, 6, 8, 9, 5, 1, 10, 3, 7]
liczby_tupla = (4, 2, 6, 8, 9, 5, 1, 10, 3, 7)

posortowana_tupla = sorted(liczby_tupla)
print(posortowana_tupla)


##############################################
planety = [("Merkury". 2440, 3.43, 0.395), ("Wenus", 6052, 5.24, 0.723), ("Ziemia", 6378, 5.52, 1), ("Mars", 3396, 3.93, 1.53), ("Jowisz", 71492, 1.33, 5.210), ("Saturn", 60268, 0.069, 9.551), ("Uran", 25559, 1.27, 19.213), ("Neptun", 24764, 1.64,30.07)]

rozmiar = lambda planeta: planety[1]
najwieksze = planety.sort(key=rozmiar, reverse=True) # sortuje po od najwiekszej planety
print(najwieksze)
