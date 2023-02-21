str1="Python"
str2="""JavaScript"""
str3='C++'
print(id(str1))
strNew=str1.capitalize()
# Виведення значення зміної
print(str1)
# Виведення адреси оперативної память, де зберігається str1
print(id(str1))

print(strNew)
print(id(strNew))

# Конкатенація або обєдання
str1=str1+str2
print(str1)
print("id(str1) =",id(str1))

print("Hello"*3)
# Вирізати із str1 "PythonJavaScript" підрядок "Java"
print("str1=",len(str1))
strAboutJava=str1[6:10:2]
print(strAboutJava)
print(strAboutJava[::-1])
print("first symbol =",str1[0])
print("last symbol =",str1[-1])
print("last symbol =",str1[len(str1)-1])

# Повернути код в ascii таблиці сомволів від 'a' до'z'
for symbol in 'abcdef'.upper():
    print(ord(symbol),end='\t')

print()
# Вивести символи кодів ascii таблиці від 20 до 100
for kod in range(20,101):
    print(chr(kod),end='\t')

print()

# Визначити чи слово "Java" є у введеному рядку
inputStr=input("Ввудіть рядок:")
if (inputStr.find("Java")>=0):
    print("string 'Java' is finded")
else:
    print("string 'Java' isn`t finded")