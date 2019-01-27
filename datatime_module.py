import datetime

#print(dir(datetime)) # wyswietla zawartosc metod modulu datetime
#help('datetime') # wyswietla opis mazdego modulu(dokumentacja)

ptr = datetime.date(1990, 1, 17)
print(ptr)
print(ptr.year)
print(ptr.month)
print(ptr.day)

print(ptr.strftime("%A, %B %d, %Y")) # formatowanie daty do stringa
                                     # %A - pelna nazwa dnia
                                     # %B - pelna nazwa miesiaca
                                     # %d - dzien(liczba)
                                     # %Y - pelny rok(%y - niepelny rok, ostatnie dwie cyfry)
message = "Pioter urodzil sie {:%A, %B %d, %Y}"
print(message.format(ptr))

# Pierwszy start rakiety Spacex
launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)

print(launch_date)
print(launch_time)
print(launch_datetime)


# pobieranie aktualnej daty
now = datetime.datetime.today()
print(now)

# konwertowanie stringa daty do zmiennej typu czas (strptime)
birthday = "17/01/1990"

birthday_datetime = datetime.datetime.strptime(birthday, '%d/%m/%Y')
print(birthday_datetime)
print(type(birthday_datetime))
