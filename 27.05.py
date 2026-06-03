# word=input("vvedite slovo")

    
    
# def reversed1(word):
#     if word==word[::-1]:
#         print("slovo polidrom")
#     else:
#         print("slovo ne polidrom")

# reversed1(word)

# while True:
#     print("1. Add")
#     print("2. Delete")
#     print("3. Pokazat spisok")
#     print("4. Ochistit")
#     print("5. Exit")
#     choise=input("Choose (1/2/3/4/5): ")
#     spisok=["xleb","arbuz","baklachan"]
    
#     if choise=="1":
#         spisok=input("vvedite tovar")
#     if choise=="2":
#         k=input("vvedite index tovara kotorui xotite udalit")
#         if k==0:
#             del spisok[0]
#         if k==2:
#             del spisok[2]
#         if k==1:
#             del spisok[1]
#         if k==3:
#             del spisok[3]
#     if choise=="3":
#         print(spisok)
#     if choise=="4":
#         spisok.clear()
#     if choise=="5":
#         break
k = 0

# p = input("vvedite parol")
# p1 = int(input("vvedite parol chislami"))

# if p1 > 9999999:
#     k = k + 1

# if len(p) > 0:
#     k = k + 1

# if p1 != 0:
#     k = k + 1

# if k == 3:
#     print("nadechno")
# elif k < 3:
#     print("slabui parol")


# for i in range(1,51):
#     if i %3==0 and i %5==0:
#          print("FizzBuzz")
     
#     elif i %5==0:
#          print("Buzz")
#     elif i %3==0:
#          print("Fizz")
#     else:
#          print(i)



# while True:
#     p=input("chtoto tam vvedite")
#     if p=="privet":
#         print("Privet!")
#     elif p=="kak dela":
#         print("xorosho")
#     elif p=="poka":
#         break
#     else:
#         print("ya ne ponyal soobchenie")
# import random

# while True:
#     p = input("vedite deistvie (kamen/nochnicu/bumaga): ")

#     if p not in ["kamen", "nochnicu", "bumaga"]:
#         print("normalno igrai")
#         continue

#     l = random.choice(["kamen", "nochnicu", "bumaga"])

#     print("komputer:", l)

#     if p == l:
#         print("nichya")

#     elif (
#         (p == "kamen" and l == "nochnicu") or
#         (p == "nochnicu" and l == "bumaga") or
#         (p == "bumaga" and l == "kamen")
#     ):
#         print("ti pobedil")

#     else:
#         print("komputer pobedil")

from random import choice


# цифры
chisla = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# маленькие буквы
bukvy = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]

# специальные символы
simvoly = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=']
parol=chisla+ bukvy+ simvoly
result=""
for i in range(10):
    result+=choice(parol)
print(result)