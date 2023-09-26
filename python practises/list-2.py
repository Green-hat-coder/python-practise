# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 13:48:07 2023

@author: khayrullayev
"""

toys = ["teddy", "lizard", "lion", "monkey", "anaconda", "spider", "elephant"]

# print(toys)

# toys.sort()
# print(toys)
# toys.append("Bumblebee")
# toys.sort()
# print(toys)
# toys.sort(reverse=True)
# print(toys)

# print(sorted(toys))
# toys.sort()

# print(toys)

# print(sorted(toys, reverse = True))

# ages = [1,-4,7,4,3,0]

# print(ages)

# ages.sort()
# print(ages)

# ages.sort(reverse=True)
# print(ages)

# print(sorted(ages))
# print(sorted(ages, reverse=True))

# ages.reverse()
# print(ages)

# toys.reverse()
# print(toys)

# uzunlik = len(toys)
# print(uzunlik)

# sonlar = list(range(1,11))

# print(sonlar)


# just_sonlar = list(range(0,101,10))
# print(just_sonlar)

# toq_sonlar = list(range(1,100,2))
# print(toq_sonlar)


# arzon = min(sonlar)
# print(arzon)
# qimmat = max(sonlar)
# print(qimmat)
# umumiy = sum(sonlar)
# print(umumiy)

# cars = ["spark", "cobalt", "nexia", "Lamborgini", "Ferrari"]

# print(cars)
# print(cars[0:3])

# print(cars[0:])
# print(cars[:2])

# my_cars = cars[:]

# my_cars.append("lambo")

# print(my_cars)
# print(cars)


# names = ("john", "cena", "andrew", "tate")

# print(names)



# names = list(names)

# names.append("aziz")
# print(names)

# names = tuple(names)

# countries = ["USA", "Tailand", "UZB", "KZ", "England", "Syria"]
# print(countries)

# the_length = len(countries)
# print(the_length)

# print(sorted(countries))
# print(sorted(countries, reverse = True))

# countries.reverse()

# print(countries)
# countries.sort()

# print(countries)
# countries.sort(reverse=True)
# print(countries)

# numbers = list(range(120, 1201, 2))



# the_sum = sum(numbers)
# print(the_sum)

# the_max = max(numbers)

# print(the_max)

# the_min = min(numbers)

# print(the_min)

# equation = f" {the_max} - {the_min} = {the_max - the_min}" 

# print(equation)

# length = len(numbers)

# print(length)

# print(numbers[0:20])
# print(numbers[270:290])
# print(numbers[520:541])

meals = ["Pilav", "Soup", "Sasuages", "eggs", "Coffee"]

breakfast = meals[:]
breakfast.remove("Pilav")
del breakfast[0]
breakfast.append("Qaymoq")
breakfast.insert(0, "Choy")
breakfast[0] = "Issiq Non"
breakfast = tuple(breakfast)



print("Done")