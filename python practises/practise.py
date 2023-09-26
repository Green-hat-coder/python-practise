# # -*- coding: utf-8 -*-
# """
# Created on Sun Sep 24 10:59:04 2023

# @author: khayr
# """

# #additional

# # ismlar = ["nemat", "holmat", 'azim', "kozim"]

# # for ism in ismlar:
# #     print(f"hello, {ism}")
# # print(f"code {len(ismlar)} marta takrorlandi")


# # cubes = list(range(9,101,2))

# # for cube in cubes:
# #     print(cube**3)
    
# # kinolar = []

# # for n in range(5):
# #     kinolar.append(input("Please enter your favourite movie? "))
# #     print(kinolar)
    
# # people = []
# # range_len = int(input("Nechta odamni bilasiz? "))
# # for n in range(range_len):
# #     people.append(input(f"{n+1} - odamning ismi? "))
    
# # print("well done!")
# # new = input("Please enter valid username: ")
# # lis = ["ali", "vali", "gani"]

# # if new in lis:
# #     print("Sorry this username has been taken!")
# # else:
# #     lis.append(new)
# #     print("Welcome")

# # cars = ["lacetti", "gm", "bmw", "ferrari"]
# # for car in cars:
# #     if car != "gm":
# #         print(car.title())
# #     else:
# #         print(car.upper())


# # admin = (input("Write your username? "))

# # user  = []

# # if admin.lower() == "anvar":
# #    print("Hey dude whats up there? ")
# # else:
# #     user.append(admin)
# #     print(f"hello new {admin}")
    
# # x = float(input("first number? "))
# # y = float(input("Second number? "))

# # if x == y:
# #     print("They are equal!")
# # elif x>y :
# #     print(x, "is bigger than", y)
# # elif y>x :
# #     print(y, "is bigger than", x)
# # else:
# #     print("No idea what you talking about! ")

# # so0n = int(input("number? "))

# # if son > 0 :
# #     print("positive")
# # elif son == 0:
# #     print("neither positive nor negative")
# # else:
# #     print("negative")

# # if son >0 :
# #     print(int(son**(1/2)))
# # else:
# #     print("Please enter positive number")

# # narh = 15000 # mijoz 15 so'mga ovqat oldi
# # choy = True
# # salat = False
# # non = True
# # kompot = True
# # assorti = False
# # #Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
# # if choy:   # agar choy olsa
# #     print("Mijoz choy oldi.")
# #     narh = narh + 3000
# # elif salat:  # agar salat olsa
# #     print("Mijoz salat oldi.")
# #     narh = narh + 5000
# # elif non:    # agar non olsa
# #     print("Mijoz non oldi.")
# #     narh = narh + 2000
# # elif kompot: # agar kompot olsa
# #     print("Mijoz kompot oldi.")
# #     narh = narh + 5000
# # else:
# #     print("Mijoz assorti oldi.")
# #     narh = narh + 15000
    
# # print(f"Jami {narh} so'm")

## menu = ["osh", "shorva", "manti"]

# # orders = ["osh", "olcha"]

# # for order in orders:
# #     if order in menu:
# #         print(f"Bizda bu {order} bor")
# #     else:
# #         print(f"bizda bu {order} yoq")

# num = int(input("Juft son kiriting: "))
# float
# if num % 2 == 0:
#     print(f"rahmat {num} juft son")
# else:
#     print("Iltimos juft son kiriting")
#     ]

# age = int(input("yosh? "))

# if age  <=4 or age >=60:
#     print("Free user!")
# elif age <=18:
#     print("10k")   
# elif age >= 18:
#     print("20k")

# products = ["olma", "anor", "behi", "anjir"]

# savat = []
# for n in range(5):
#     savat.append(input(f"Please enter the {n+1} - pruduct: "))
# for harid in savat:
#     if harid in products:
#         print(f"we do have {harid}")
#     else:
#         print(f"we dont have {harid}")

pruducts = ["qovun", "tarvuz", "olma", "anor", "behi" ]


savat = []
available = []
not_available = []
for n in range(5):
    savat.append(input("Enter the pruduct: "))
for mahsulot in savat:
    if mahsulot in pruducts:
        available.append(mahsulot)
    else:
        not_available.append(mahsulot)
    
if not_available:
    print("we do dont have the following pruducts")
    for mahsulot in not_available:
        print(mahsulot)
else:
    print("We have all the pruducts you want!")
