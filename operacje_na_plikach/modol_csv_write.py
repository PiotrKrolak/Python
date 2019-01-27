import csv
from datetime import datetime, date, time

data = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

file = open("potegowanie_dwojki.csv", 'w')
writer = csv.writer(file)

writer.writerow(["Wykladnik", "Wynik"])

for i in range(len(data)):
    writer.writerow([i, data[i]])
