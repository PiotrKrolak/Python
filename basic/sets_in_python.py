example = set() # pusty zestaw
#print(dir(example))

example.add(21)
print(example)

example.add(3.14)
print(example)

example.add(True)
print(example)

example.add('Hello')
print(example)

###
# usuwanie elementrow z zestawu
num_of_elements = len(example) # len return number of elements in set
                               # zwróci error jeżeli nie ma elementu
print(num_of_elements)

# num_of_elements.discard(50) # usuwa element z zzestawu ale jezeli nie ma go w zestawie to ne zwraca bledu
print(num_of_elements)
###

example.remove(21)
print(example)
##########################

odds = set([1,3,5,7,9])
events = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9, 10])

"""UNION - suma dwoch zbiorow"""
union = odds.union(events)
print(union)
union = primes.union(composites)
print(union)

"""INTERSECTION - czesc wspolna dwoch zbiorow"""
intersection = odds.intersection(primes)
print(intersection)
intersection = events.intersection(composites)
print(intersection)

"""
# Powinno zwracac True albo False...
print(2 in primes)
print(6 in odds)
print(9 not is events)
"""
