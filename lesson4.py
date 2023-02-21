# if value1:
#     commands
# elif value2:
#    commands
# else:
#     commands

#t=int(input("Input t:"))
#if t>18:
#    print("Shirt")
#elif t>=10 and t<=18:
 #   print("Skirt")
#elif t<10:
#    print("Jacket")

"""
#Дано два цілих числа A і B (при цьому A ≤ B). Виведіть всі числа від A до B включно.
a=int(input('Введіть число А: '))
b=int(input('Введіть число B: '))

for number in range(a, b + 1, 1):
    print(number)

for letter in "Python":
    print(letter,end="\t")
"""

#Дано два цілих числа A і В. Виведіть всі числа від A до B включно, в порядку зростання, якщо A <B, або в порядку спадання в іншому випадку.
a=int(input('Введіть число А: '))
b=int(input('Введіть число B: '))

if a<b:
    while a<=b:
        print(a,end="\t\a")

else:
    while a>=b:
        print(a,end="\t\a")
        a=a-1
    
    


