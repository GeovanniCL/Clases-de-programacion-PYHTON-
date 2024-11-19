"""
inicio_rango = int(input("Ingresa el inicio del rango: "))
final_rango = int(input("Ingresa el final del rango: "))

for n in range (inicio_rango , final_rango) :
    es_primo = 1
    for x in range (2, n):
        if n % x == 0 :
            es_primo = 0
            break
    if es_primo:
        print(n, "es un numero primo ")
        
"""
#Ejercicio 2 FizzBuzz

for n in range(1, 100 + 1):
    if n % 3 == 0 and  n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print ("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)